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
import random


# this function adds spaces around all punctuation in the specified file, and writes it to the output file
def gen_random_dataset(): 
    with tf.Session() as sess:

        input_code_file = "../data/django/all.code"
        input_en_file = "../data/django/all.en"
        output_dev_en_file = "../data/django/dev/10pt.random.en"
        output_dev_code_file = "../data/django/dev/10pt.random.code"
        output_train_code_file = "../data/django/train/90pt.random.code"
        output_train_en_file = "../data/django/train/90pt.random.en"



        # read the original files
        with open(input_code_file) as f:
            code_file = f.readlines()
        with open(input_en_file) as g:
            en_file = g.readlines()

        # create a list with 0-18805 shuffled
        indices = random.sample(range(0, 18805), 18805)

        # open the dev files
        with tf.gfile.GFile(output_dev_en_file, mode="w") as dev_en_file:
            with tf.gfile.GFile(output_dev_code_file, mode="w") as dev_code_file:
                    
                # write 1805 random lines to the dev files
                for x in xrange(0,1805):
                    dev_en_file.write(en_file[indices[x]])
                    dev_code_file.write(code_file[indices[x]])

        print ("Dev files created.")

        # open the train files
        with tf.gfile.GFile(output_train_en_file, mode="w") as train_en_file:
            with tf.gfile.GFile(output_train_code_file, mode="w") as train_code_file:

                # write 17000 random lines to the train files
                for x in xrange(1805,18805):
                    train_en_file.write(en_file[indices[x]])
                    train_code_file.write(code_file[indices[x]])

        print ("Train files created.")
        print ("Done.")


def main(_):
    gen_random_dataset()
    # os.system("python punctuation_police.py")




if __name__ == "__main__":
    tf.app.run()
