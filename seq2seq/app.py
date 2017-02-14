# app.py

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from flask import Flask
from flask import Response
from flask import abort
from flask import make_response
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig

from translate import *

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

sess = None
model = None
code_vocab_path = None
en_vocab_path = None
code_vocab = None
rev_en_vocab = None
_buckets = [(5, 10), (10, 15), (20, 25), (40, 50), (250,100)]

tf.app.flags.FLAGS.num_layers = 3
FLAGS = tf.app.flags.FLAGS


def trans(sentence):
    if not model or not sess or not sentence:
        return None
    # Get token-ids for the input sentence.
    token_ids = data_utils.sentence_to_token_ids(tf.compat.as_bytes(sentence), code_vocab)

    # print (token_ids)

    # Which bucket does it belong to?
    bucket_id = min([b for b in xrange(len(_buckets))
                    if _buckets[b][0] > len(token_ids)])
    # Get a 1-element batch to feed the sentence to the model.
    encoder_inputs, decoder_inputs, target_weights = model.get_batch(
    {bucket_id: [(token_ids, [])]}, bucket_id)

    # Get output logits for the sentence.
    _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
    target_weights, bucket_id, True)
    # This is a greedy decoder - outputs are just argmaxes of output_logits.
    outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]

    # If there is an EOS symbol in outputs, cut them at that point.
    if data_utils.EOS_ID in outputs:
        outputs = outputs[:outputs.index(data_utils.EOS_ID)]
    # Print out French sentence corresponding to outputs.
    return " ".join([tf.compat.as_str(rev_en_vocab[output]) for output in outputs if output in rev_en_vocab])


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():

    if "key" not in request.values and request.values["key"] != app.config["APIKEY"]:
        return Response("Not authorized, please pass 'key' url parameter with APIKEY", 401)

    if "q" not in request.values:
        return Response("No q parameter", 500)

    res = trans(request.values["q"])

    if not res:
        res = "translation result"

    resp = make_response(res)

    return resp


if __name__ == '__main__':
    if not app.config["DEBUG"]:
        sess = tf.Session()
        model = create_model(sess, True, FLAGS)
        model.batch_size = 1  # We decode one sentence at a time.
        #
        # Load vocabularies.
        code_vocab_path = os.path.join(data_dir,
                                       "vocab%d.code" % FLAGS.code_vocab_size)
        en_vocab_path = os.path.join(data_dir,
                                     "vocab%d.en" % FLAGS.en_vocab_size)
        code_vocab, _ = data_utils.initialize_vocabulary(code_vocab_path)
        _, rev_en_vocab = data_utils.initialize_vocabulary(en_vocab_path)
        print("Tensorflow session ready")
    app.run()
