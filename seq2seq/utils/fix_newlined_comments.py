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
import re


# The original Django dataset seemed to have been split wrong at certain comments
# Part of the previous comment ended up in the next comment, divided by three spaces
# this script loops over all sentences, and when it finds three spaces it adds them to 
# the previous comment
def fix_newlined_comments(): 
    with tf.Session() as sess:

        input_file = "../data/django/train/90pt.en"
        output_file = "../data/django/train/90pt.fixed.en"
        split_at = "   " # three spaces

        with tf.gfile.GFile(input_file, mode="r") as inp_file:
            with tf.gfile.GFile(output_file, mode="w") as outp_file:

                # get initial sentences
                input_sent = inp_file.readline()
                prev_sent = ""

                # loop while we haven't reached the EOF
                while(input_sent):

                    # split line at triple space, and add the first part to the previous line
                    line = input_sent.split("   ")
                    if (len(line) > 1):
                        prev_sent = prev_sent.rstrip() # remove the newline from the previous line
                        prev_sent = prev_sent + " " + line[0] + "\n"
                        input_sent = line[1]

                    # write to the output file and read the next line
                    if (prev_sent != ""):
                        outp_file.write(prev_sent)
                    prev_sent = input_sent
                    input_sent = inp_file.readline()    



                # because we write the previous line each time, we need to add the last line at the end
                outp_file.write(prev_sent)

        print "Done"

def main(_):
    fix_newlined_comments()


if __name__ == "__main__":
    tf.app.run()
