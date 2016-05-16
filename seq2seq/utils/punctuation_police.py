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


# this function adds spaces around all punctuation in the specified file, and writes it to the output file
def space_punctuation(): 
    with tf.Session() as sess:

        dev_file = "../data/django/dev/10pt.random.en"
        output_dv_file = "../data/django/dev/10pt.random.spaced.en"

        # open files
        with tf.gfile.GFile(dev_file, mode="r") as dev_file:
            with tf.gfile.GFile(output_dv_file, mode="w") as output_dev_file:

                # get initial sentences
                dev_sent = dev_file.readline()

                # loop while we haven't reached the EOF
                while(dev_sent):

                    # add spaces around punctuation
                    dev_sent = re.sub('([.,\'\"\[\]\{\}\(\)])', r' \1 ', dev_sent)
                    dev_sent = re.sub('\s{2,}', ' ', dev_sent)

                    # write the new lines to the files
                    dev_sent = dev_sent.rstrip()
                    output_dev_file.write(dev_sent + "\n")

                    # read new sentences
                    dev_sent = dev_file.readline()

        print ("Done. Police out.")


def main(_):
    space_punctuation()


if __name__ == "__main__":
    tf.app.run()
