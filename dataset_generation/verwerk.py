
# Find filepaths to files containing a string, such as: "# "
# grep -r -l --include \*.py "# " 
# grep -r -l --include \*.py '"""' 

import subprocess
import sys
import getDocStrings
import getComments
import fileinput
import re


directories = ["edx-platform-master", "django-master", "pandas-master", 
				"pylearn2-master", "salt-develop", "scikit-learn-master"]
originalPath = "original/"
processedPath = "processed/raw/"
trainingFile = "processed/trainingFormat/"
readableFile = "processed/readableFormat/"

commentCodeExt = ".commentCode"
commentExt = ".comment"
docstringCodeExt = ".dsCode"
docstringExt = ".ds"

# the largest bucket, no need to get code-comment pairs larger than this
maxBucket = [40,50]

# retrieve a file list of files with comments and docstrings in the directory
def getFileList(directory):
    try:	
        # get lists of all files with comments in the directory
        comments = subprocess.check_output(["grep -r -l --include \*.py '# ' " + directory], shell=True)
        files_w_comments = comments.splitlines()
        print "Found %d files with comments" % len(files_w_comments)

        # get a list of all files with doc strings
        doc_strings = subprocess.check_output(["grep -r -l --include \*.py '\"\"\"' " + directory], shell=True)
        files_w_doc_strings = doc_strings.splitlines()
        print "Found %d files with doc strings" % len(files_w_doc_strings)
    except:
        print "Unexpected error, most likely no doc strings or comments found. Does the directory exist? \n The error:", sys.exc_info()[0]
        sys.exit(0)

    return (files_w_comments, files_w_doc_strings)


# get the block comment - code pairs
def getCommentPairs(files_w_comments, directory):

    # set file names and empty files
    codeFile = processedPath + directory +  commentCodeExt
    commentFile = processedPath + directory + commentExt
    open(codeFile, 'w').close()
    open(commentFile, 'w').close()

    counter = 0

    # loop through all files with block comments
    print "\nBlock comments:"
    normalComments = 0
    inlineComments = 0
    rejectedComments = 0
    for file in files_w_comments:
		
        # print "File " , counter, ":", file
        counter += 1

        with open(file) as fp:
            (x, y, z) = getComments.generate_pairs(fp, codeFile, commentFile, maxBucket)
            normalComments += x
            inlineComments += y
            rejectedComments += z

    print "Total comments found: " , normalComments + inlineComments + rejectedComments
    print "Normal comments: ", normalComments
    print "Inline comments: ", inlineComments
    print "Rejected comments: ", rejectedComments


# Get the docstring-code pairs
def getDocStringPairs(files_w_doc_strings, directory):
    counter = 0

    # set file names and empty files
    codeFile = processedPath + directory +  docstringCodeExt
    commentFile = processedPath + directory + docstringExt
    open(codeFile, 'w').close()
    open(commentFile, 'w').close()

    # loop through all files with docstrings
    print "\nDocstrings:"
    normalDocStrings = 0
    rejectedDocStrings = 0
    for file in files_w_doc_strings:
		
        # print "File " , counter, ":", file
        counter += 1

        with open(file) as fp:
            (x,y) = getDocStrings.generate_pairs(fp, codeFile, commentFile, maxBucket)
            normalDocStrings += x
            rejectedDocStrings += y

    print "Total docstrings found: " , normalDocStrings + rejectedDocStrings
    print "Normal docstrings: ", normalDocStrings
    print "Rejected docstrings: ", rejectedDocStrings


# loop through the directory list and extract all comment-code pairs
def createCCPair():
    for directory in directories:
        print "\n"
        print "-" * 50
        print "Directory:" , directory
        print "-" * 50

        # get file list
        (files_w_comments, files_w_doc_strings) = getFileList(originalPath + directory)

        # extract code-comment pairs
        getCommentPairs(files_w_comments, directory)
        getDocStringPairs(files_w_doc_strings, directory)


# convert the raw newline seperated data into a readable format 
def createReadableFormat(file, codeF, commentF, counter):
    with open(file, "a") as file:
        for directory in directories:

            codeFile = processedPath + directory +  codeF
            commentFile = processedPath + directory + commentF

            # read the lines and do some string / list conversion stuff
            codeLines =  open(codeFile, "r").readlines()
            codeLines = "".join(codeLines)
            codeLines = codeLines.split("!@#$%!@#$%!@#$%!@#$%!@#$%")
            commentLines = open(commentFile, "r").readlines()
            commentLines = "".join(commentLines)
            commentLines = commentLines.split("!@#$%!@#$%!@#$%!@#$%!@#$%")


            # loop through the lines
            for i in xrange(len(codeLines)):

                if "Parameters ----------" in commentLines[i]:
                    commentLines[i] = commentLines[i].split("Parameters ----------")[0].strip()

                if codeLines[i].strip() != '' and commentLines[i].strip() != '':
                    file.write("Pair : " + str(counter) + "\n")
                    file.write("Comment:" + commentLines[i].strip() + "\n")
                    file.write("Code:\n" + codeLines[i].rstrip() + "\n\n")
                    counter += 1

    return counter


# convert the raw newline seperated data into training files
def createTrainingFile(eFile, cFile, codeFileExtension, commentFileExtension, counter, directory):
    with open(eFile, "a") as enFile:
        with open(cFile, "a") as codeFile:

            # get the processed files in raw format
            codeFileName = processedPath + directory +  codeFileExtension
            commentFileName = processedPath + directory + commentFileExtension

            # read the lines and remove annoying spaces / enters and stuff
            codeLines =  open(codeFileName, "r").readlines()
            codeLines = "".join(codeLines)
            codeLines = " ".join(codeLines.split())
            codelines = "".join(codeLines)
            codeLines = codeLines.split("!@#$%!@#$%!@#$%!@#$%!@#$%")
            commentLines = open(commentFileName, "r").readlines()
            commentLines = "".join(commentLines)
            commentLines = commentLines.split("!@#$%!@#$%!@#$%!@#$%!@#$%")

            # loop through the lines
            for i in xrange(len(codeLines)):

                # any(x in a for x in b)

                if "Parameters ----------" in commentLines[i]:
                    commentLines[i] = commentLines[i].split("Parameters ----------")[0].strip()

                if codeLines[i].strip() != '' and commentLines[i].strip() != '':
                    codeFile.write(codeLines[i].strip().replace("\n","") + "\n")
                    enFile.write(commentLines[i].strip().replace("\n","") + "\n")
                    counter += 1

    return counter

def createSeperateTrainingFiles():
    for directory in directories:
        enFile = trainingFile + directory + ".en"
        codeFile = trainingFile + directory + ".code"

        # empty files
        open(enFile, 'w').close()
        open(codeFile, 'w').close()

        counter = 0 
        # convert the docstring-code pairs and comment-code pairs into two large files 
        counter = createTrainingFile(enFile, codeFile, commentCodeExt, commentExt, 1, directory)
        createTrainingFile(enFile, codeFile, docstringCodeExt, docstringExt, counter, directory)


def concatenateTrainingFiles():
    enFileAll = trainingFile + "all.en"
    codeFileAll = trainingFile + "all.code"

    # Conctatenate all seperate trainingsfile into a single file
    with open(enFileAll, 'w') as enFileAll:
        with open(codeFileAll, 'w') as codeFileAll:
            for directory in directories:
                # get seperate training files of this directory
                enFile = trainingFile + directory + ".en"
                codeFile = trainingFile + directory + ".code"

                # write the comments to the comment file
                with open(enFile) as enFile:
                    for line in enFile:
                        enFileAll.write(line)

                # write the code to the code file
                with open(codeFile) as codeFile:
                    for line in codeFile: 
                        codeFileAll.write(line)


if __name__ == '__main__':    
    print "Creating Code-Comment pairs.."
    createCCPair()
    print "-" * 50
 
    print "Converting into readable format.."
    # empty file
    file = readableFile + "readable.txt"
    open(file, 'w').close()
    counter = createReadableFormat(file, commentCodeExt, commentExt, 1)
    createReadableFormat(file, docstringCodeExt, docstringExt, counter)

    print "Converting into seperate training files.."
    createSeperateTrainingFiles()

    print "Converting into single training file.."
    concatenateTrainingFiles()
