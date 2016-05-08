# comment-generation
Set of (Tensorflow) implementations which generate comments from code. Thesis for the B.sc. AI. 

# How to execute:
## Seq2seq: 
- Enter tf: source ~/tensorflow/bin/activate
- Execute code: python translate.py --size=256 --num_layers=3 --steps_per_checkpoint=50 --bleu
- Or interactive mode (only works when the model has been trained): python translate.py --size=350 --num_layers=3 --step_per_checkpoint=50 --decode

### Options
- add --evaluate to see the score with a trained model on the development file (default False)
- add --size=XX to change size of LSTM layer to XX (default 256)
- add --num_layers=XX to change number of LSTM layers to XX (default 2)
- add --steps_per_checkpoint=XX to change amount of steps per evaluation output to XX(default 200)
- add --code_vocab_size=XX to change the code vocabulary size to XX (default 3000)
- add --en_vocab_size=XX to change the English vocabulary size to XX (default 3000)


# Results:
## Seq2seq 

With 4 buckets, vocabulary=3000, layers=2 and size=256
global step 10400 learning rate 0.5000 step-time 0.23 perplexity 1.09
  eval: bucket 0 perplexity 2.31
  eval: bucket 1 perplexity 2.22
  eval: bucket 2 perplexity 8.32
  eval: bucket 3 perplexity 24.29
BLEU = 14.19, 39.1/20.1/11.3/4.6 (BP=1.000, ratio=1.071, hyp_len=41721, ref_len=38963)

