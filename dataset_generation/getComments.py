# -*- coding: utf-8 -*-
""" Open a file, find all hashtag comments in the file and get the corresponding code"""

from os.path import basename, splitext
import sys
commentList = ["# ", "#!"]


def generate_pairs(source, codeFile, commentFile, module='<string>'):
    """ Loop through the source code and filter comments and
    their correspondig code. """

    # open the file
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()

    # print "Source:\n" , source
    source = source.splitlines()
    normalComments = 0
    inlineComments = 0
    rejectedComments = 0

    i = -1
    count = 0 

    # check each line for comments
    while i < len(source):
        # print "Current i:", i
        line = source[i]

        # print "line " , i

        # print "Source length:" , len(source)
        # print "Last sentence:" , source[len(source) - 1]

        # print ">Current line in general loop:" , line

        # check if the line starts with an comment, if so 
        # get the comment and code, and skip to the correct line after
        # the comment
        if line.strip()[:2] in commentList:
            # print ">Current line in general loop:" , line
            # print ">Found comment, going into comment loop"
            (i, success) = filterComment(source, i, codeFile, commentFile)
            # print ">Returned line number:" , i, " with Success:", success

            if count != 0 and i == count:
                # print "Error, looping at line ", i, " in getComments in file:" , filename
                sys.exit(0)

            count = i

            # only increment the count if there was no error
            if success:
                normalComments += 1
            else:
                rejectedComments += 1
            continue

        # check if we have an inline comment
        # if "# " in line.strip():
        #     parts = line.split("# ")
            

        #     if len(parts) != 2:
        #         pass
        #         # print ">Something is not right, skipping comment"
        #     else:
        #         code = parts[0].strip()
        #         comment = parts[1].strip().replace("#")

        #         if comment != "" and code != "":
        #             inlineComments += 1

        #             with open(commentFile, "a") as commentF:
        #                 commentF.write(comment + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")

        #             with open(codeFile, "a") as codeF:
        #                 codeF.write(code.strip() + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")
        #                 # codeF.write(" ".join([x.strip() for x in code]) + "\n")

        #             # print ">Comment:" , comment
        #             # print ">Code: \n" , code

        # increment by one
        i += 1

    # print "Total comments found: " , normalComments + inlineComments + rejectedComments
    # print "Normal comments: ", normalComments
    # print "Inline comments: ", inlineComments
    # print "Rejected comments: ", rejectedComments
    return (normalComments, inlineComments, rejectedComments)



def filterComment(source, startLine, codeFile, commentFile):
    """ Find the comment at line i in the list source. When found check for 
    a multiline comment and get the corresponding code """

    comment = ""
    indentation = -1
    currIndent = -1
    code = []
    globalI = len(source) + 10

    # print ">>in comment loop"

    # loop through all the lines in the source, get the comment 
    # and the corresponding code
    with open(commentFile, "a") as commentF:
        with open(codeFile, "a") as codeF:
            for i in xrange(startLine, len(source)):

                globalI = i
                line = source[i]

                # print ">>Current line ", i, " in comment loop:" , line

                # comments need to be directly above code
                if line.strip() == "" and comment == "":
                    # print ">>empty line after comment, return error"
                    return (i,False)

                # Continue if we have an divider row
                if line.replace("#", "").strip() == "" and line.strip() != "":
                    # print ">>found divider row, continue"
                    continue

                # check if it is an comment, and if so add it to the comment
                if line.strip()[:2] in commentList:
                    # print ">>found commentline, add to comment"
                    comment += line.strip().replace("#", "") + " "
                    continue

                # lines with docstrings are skipped
                if '"""' in line or "'''" in line:
                    return (i,False)

                # if we get here, it means we are not in the comment anymore
                # First get the indentation level of the current line of code
                currIndent = len(line) - len(line.lstrip())

                # print ">>Current line indentation:" , currIndent


                # If it is the first line of code, set our indentation level
                if indentation == -1:
                    indentation = currIndent
                    # print ">>Set indentation for first time"

                # if we hit an empty line and have no code yet, return with an error 
                if line.strip() == "" and code == []:
                    # print ">>Found empty line and no code yet, return error"
                    return (i,False)

                # if we hit an empty line or go to an parent piece in the code
                # return the gathered code
                if line.strip() == "" or indentation > currIndent or (any(c in line for c in commentList)):
                    # write to file
                    for j in xrange(len(code)):
                        codeF.write(code[j] + "\n")
                    codeF.write("!@#$%!@#$%!@#$%!@#$%!@#$%")
                    commentF.write(comment + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")

                    # print ">>Ending code"
                    # code = "\n".join(code)
                    # print ">>Comment is:" , comment
                    # print  ">>Code is:\n" , code
                    return (i,True)

                # add the line to our code if all is well (without any inline comments if any)
                # print ">>Add codeline to code"
                if line.strip() != "":
                    code.append(line)

            # if we are here 
            # print ">>got to end with i " , globalI
            if comment.strip() != "" and code != []:
                # write to file
                for j in xrange(len(code)):
                    codeF.write(code[j] + "\n")
                codeF.write("!@#$%!@#$%!@#$%!@#$%!@#$%")
                commentF.write(comment + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")
                # codeF.write(" ".join([x.strip() for x in code]) + "\n")

                # code = "\n".join(code)
                # print ">>Comment is:" , comment
                # print  ">>Code is:\n" , code
                return (globalI+1,True)
            else:
                # print "in else"
                return (globalI+1,False)



if __name__ == '__main__':
    import sys
    
    with open(sys.argv[1]) as fp:
        make_pairs(fp)