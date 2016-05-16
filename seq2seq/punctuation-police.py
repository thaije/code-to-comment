import tensorflow as tf
import os
import sys
import subprocess
import re

def space_punctuation(): 
    with tf.Session() as sess:

        dev_file = "data/django/dev/10pt.en"
        train_file = "data/django/train/90pt.en"
        output_dv_file = "data/django/dev/10pt.spaced.en"
        output_tr_file = "data/django/train/90pt.spaced.en"


        # open files
        with tf.gfile.GFile(train_file, mode="r") as train_file:
            with tf.gfile.GFile(dev_file, mode="r") as dev_file:
                with tf.gfile.GFile(output_tr_file, mode="w") as output_train_file:
                    with tf.gfile.GFile(output_dv_file, mode="w") as output_dev_file:

                        # get initial sentences
                        train_sent = train_file.readline()
                        dev_sent = dev_file.readline()

                        # loop while we haven't reached the EOF
                        while(train_sent and dev_sent):

                            # add spaces around punctuation
                            train_sent = re.sub('([.,\'\"\[\]\{\}\(\)])', r' \1 ', train_sent)
                            train_sent = re.sub('\s{2,}', ' ', train_sent)

                            dev_sent = re.sub('([.,\'\"\[\]\{\}\(\)])', r' \1 ', dev_sent)
                            dev_sent = re.sub('\s{2,}', ' ', dev_sent)

                            # write the new lines to the files
                            output_train_file.write(train_sent + "\n")
                            output_dev_file.write(dev_sent + "\n")

                            # read new sentences
                            train_sent = train_file.readline()
                            dev_sent = dev_file.readline()

        print ("Done. Police out.")


def main(_):
    space_punctuation()


if __name__ == "__main__":
    tf.app.run()
