# -*- coding: utf-8 -*-
"""Filter comments from Python code and save the corresponding code"""

from os.path import basename, splitext



def print_comments(source, module='<string>'):
    """ Loop through the source code and filter comments and
    their correspondig code. """

    # open the file
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()

    print "Source:\n" , source
    source = source.splitlines()
    normalComments = 0
    inlineComments = 0

    # check each line for comments
    for i in xrange(len(source)):
        line = source[i]

        # check if the line starts with an comment, if so 
        # get the comment and code, and skip to the correct line after
        # the comment
        if line.strip()[:2] == "# ":
            i = filterComment(source, i) - 1
            print "Returned line number:" , i
            normalComments += 1
            continue

        # check if we have an comment at the end of the line
        if "# " in line.strip():
            parts = line.split("# ")
            
            if len(parts) != 2:
                print "Something is not right, skipping comment"
            else:
                code = parts[0].strip()
                comment = parts[1].strip()
                inlineComments += 1

                print "Comment:" , comment
                print "Code: \n" , code



    print "Total comments found: " , normalComments + inlineComments
    print "Normal comments: ", normalComments
    print "Inline comments: ", inlineComments



def filterComment(source, startLine):
    """ Find the comment at line i in the list source. When found check for 
    a multiline comment and get the corresponding code """

    comment = ""
    indentation = -1
    currIndent = -1
    code = []

    # loop through all the lines in the source, get the comment 
    # and the corresponding code
    for i in xrange(startLine, len(source)):
        line = source[i]

        # Continue if we have an divider row
        if line.replace("#", "").strip() == "":
            continue

        # check if it is an comment, and if so add it to the comment
        if line.strip()[:2] == "# ":
            comment += line.strip().replace("# ", "") + " "
            continue


        # if we get here, it means we are not in the comment anymore
        # First get the indentation level of the current line of code
        currIndent = len(line) - len(line.lstrip())

        print "Current indentation:" , currIndent

        # If it is the first line of code, set our indentation level
        if indentation == -1:
            indentation = currIndent
            print "Set indentation for first time"

        # if we hit an empty line or go to an parent piece in the code
        # return the gathered code
        if line.strip() == "" or indentation > currIndent: 

            print "Ending code"
            code = "\n".join(code)
            print "Comment is:" , comment
            print  "Code is:\n" , code
            return i

        # add the line to our code if all is well
        code.append(line)




if __name__ == '__main__':
    import sys
    
    with open(sys.argv[1]) as fp:
        print_comments(fp)