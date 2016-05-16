import tensorflow as tf
import os
import sys
import subprocess

def calc_bleu(): 
    with tf.Session() as sess:

        src_file = "../../data/django/dev/10pt.spaced.en"
        trans_file = "../../data/django/dev/translated.en"
        temp_ref = "bleu_test_data/ref_temp.txt"
        temp_trans = "bleu_test_data/trans_temp.txt"
        bl_file = "bleu.txt"


        # open files
        with tf.gfile.GFile(src_file, mode="r") as source_file:
            with tf.gfile.GFile(trans_file, mode="r") as translated_file:
                with tf.gfile.GFile(bl_file, mode="w") as bleu_file:

                    # get initial sentences
                    sent_src = source_file.readline()
                    sent_trans = translated_file.readline()
                    counter = 0

                    # loop while we haven't reached the EOF
                    while(sent_src and sent_trans):

                        sys.stdout.write('Calculating: %d ' % counter)
                        sys.stdout.flush()
                        counter += 1

                        # write the current two lines to two temp files
                        with tf.gfile.GFile(temp_ref, mode="w") as ref_temp:
                            with tf.gfile.GFile(temp_trans, mode="w") as trans_temp:
                                ref_temp.write(sent_src)
                                trans_temp.write(sent_trans)

                        # us the two files to calc the bleu score
                        bleu_file.write("Original: " + sent_src)
                        bleu_file.write("Translation: " + sent_trans)
                        output = os.popen("perl multi-bleu.perl " + temp_ref + " < " + temp_trans).read()
                        bleu_file.write(output + "\n")


                        sent_src = source_file.readline()
                        sent_trans = translated_file.readline()



def main(_):
    calc_bleu()


if __name__ == "__main__":
    tf.app.run()
