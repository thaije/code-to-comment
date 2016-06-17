###########################################################################################################
# Author: Tjalling Haije
# Project: code-to-comment 
# For: Bsc AI, University of Amsterdam
# Date: May, 2016
###########################################################################################################

import tensorflow as tf
import os
import sys
import subprocess


# This function calculates the bleu score of each translated sentence individually, and dislays them
# together with the reference code line, reference comment, and generated comment
def calc_bleu(): 
    with tf.Session() as sess:

        src_file = "../../data/django/dev/best-so-far/10pt.random.spaced.en"
        # trans_file = "../../data/django/dev/best-so-far/translated.en"
        trans_file = "bleu_test_data/translated.en"
        cd_file = "../../data/django/dev/best-so-far/10pt.random.code"
        temp_ref = "bleu_test_data/ref_temp.txt"
        temp_trans = "bleu_test_data/trans_temp.txt"
        bl_file = "bleu2.txt"



        counter = 0
        equal = 0

        # open files
        with tf.gfile.GFile(src_file, mode="r") as source_file:
            with tf.gfile.GFile(trans_file, mode="r") as translated_file:
                with tf.gfile.GFile(cd_file, mode="r") as code_file:
                    with tf.gfile.GFile(bl_file, mode="w") as bleu_file:

                        # get initial sentences
                        sent_src = source_file.readline()
                        sent_trans = translated_file.readline()
                        sent_code = code_file.readline()
                        counter = 0

                        # loop while we haven't reached the EOF
                        while(sent_src and sent_trans and sent_code):

                            # check accuracy
                            if ("".join(sent_src.split()) == "".join(sent_trans.split())):
                                equal += 1


                            sys.stdout.write('Calculating: %d ' % counter)
                            sys.stdout.flush()
                            counter += 1

                            # write the current two lines to two temp files
                            with tf.gfile.GFile(temp_ref, mode="w") as ref_temp:
                                with tf.gfile.GFile(temp_trans, mode="w") as trans_temp:
                                    ref_temp.write(sent_src)
                                    trans_temp.write(sent_trans)

                            # use the two files to calc the bleu score

                            # bleu_file.write("Original comment: " + sent_src)
                            bleu_file.write("// " + sent_trans)
                            bleu_file.write("Code line %d: %s" % (counter,sent_code))
                            output = os.popen("perl multi-bleu.perl " + temp_ref + " < " + temp_trans).read()
                            bleu_file.write(output + "\n\n")


                            sent_code = code_file.readline()
                            sent_src = source_file.readline()
                            sent_trans = translated_file.readline()

        accuracy = 0.00
        if(equal != 0):
            accuracy = (equal / float(counter))
        print ("\nAccuracy is: %s" % accuracy )

def main(_):
    calc_bleu()


if __name__ == "__main__":
    tf.app.run()
