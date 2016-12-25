from os.path import basename, splitext
import sys
import util


commentList = ["# ", "#!"]
dsList = ["'''", '"""']
commentExceptions = ["todo","to do"]

def generate_pairs(source, codeFile, commentFile, maxBucket, module='<string>'):
    # open the file
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()

    # print "Source:\n" , source
    source = source.splitlines()
    normalDocStrings = 0
    rejectedDocStrings = 0
    i = 0
    count = 0

    # check each line for comments
    while i < len(source):
        # print "Current i:", i
        line = source[i]
        # print "Index:", i
        # print "Current line:" , line

        # if line.strip()[:3] == '"""':
        if '"""' in line:

            # print "Current line " , i , ":" , line , " in file:" , filename
            # print "Found docstring"
            (i, success) = filterDocString(source, i, codeFile, commentFile, maxBucket)
            # print ">Returned line number:" , i, " with Success:", success

            # Throw an 'error' in case we are looping
            if i == count:
                print "Error, looping at line " , i , " in getDocStrings in file:" , filename
                sys.exit(0)

            count = i

            # only increment the count if there was no error
            if success:
                normalDocStrings += 1
            else:
                rejectedDocStrings += 1
            continue


        # increment by one
        i += 1

    # print "Total docstrings found: " , normalDocStrings + rejectedDocStrings
    # print "Normal docstrings: ", normalDocStrings
    # print "Rejected docstrings: ", rejectedDocStrings

    return (normalDocStrings, rejectedDocStrings)

def filterDocString(source, startLine, codeFile, commentFile, maxBucket):

    inComment = True
    comment = ""
    indentation = -1
    currIndent = -1
    code = []
    globalI = len(source) + 10

    # add the first line to the comment and check for single line docstrings
    count = (source[startLine].count('"""'))
    if count == 2:
        comment = source[startLine].strip().replace('"""', "") + " "
        inComment = False
    else:
        comment = source[startLine].strip().split('"""')[1]
    startLine += 1

    # print ">>Inside comment loop, added firstline:" , comment

    # loop through all the lines in the source, get the comment 
    # and the corresponding code
    with open(commentFile, "a") as commentF:
        with open(codeFile, "a") as codeF:
            for i in xrange(startLine, len(source)):
                # print "i in comment loop is:" , i
                globalI = i
                # print "I is:", i, " startline is:" , startLine
                line = source[i]

                # skip empty lines
                if line.strip() == "":
                    # print "Skipped empty line"
                    continue

                # If it is the first line of code, set our indentation level
                if indentation == -1:
                    indentation = currIndent

                # check if there is an block comment inside the docstring annotated code
                if any(comment in line for comment in commentList):
                    # print ">>Found block comment, return error"
                    return (i, False)

                currIndent = len(line) - len(line.lstrip())
                # print ">>Current indent" , currIndent , " current line:" , line

                if "'''" in line:
                    return (i,False)

                # check if we have encountered an doc string
                if '"""' in line:

                    # print ">>Found triple quote"

                    # first if we are at another indentation level, we found an deeper
                    # docstring, thus exit
                    if currIndent != indentation or not inComment:
                        # print ">>>It is a new comment, return error"
                        return(i,False)

                    # otherwise end the comment
                    else:
                        # print ">>>Closed comment"
                        comment += source[i].strip().replace('"""', "").replace("#","") + " "
                        inComment = False
                        continue

                # add text to the comment if it hasn't closed yet
                if inComment:
                    comment += line.strip().replace("#","") + " "
                    continue

                # if we are still here, we have closed the comment and are collecting code

                # return true if we found the end of the annotated code
                if indentation > currIndent:
                    code = util.cleanCode(code)
                    # only return true if we are in a function def,
                    # also no need to save code-comment pairs larger than maxBucket size
                    if  not isDef(source, startLine, i) or \
                        not (util.tokenize("".join(code)) < maxBucket[0] and util.tokenize(comment) < maxBucket[1]) or \
                        (any(exc in comment.lower() for exc in commentExceptions)):

                        return (i, False)

                    # write to file
                    for j in xrange(len(code)):
                        codeF.write(code[j] + "\n")
                    codeF.write("!@#$%!@#$%!@#$%!@#$%!@#$%")
                    commentF.write(util.cleanComment(comment) + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")

                    return(i, True)

                # if we are still here, add the current line to the code
                code.append(line.strip())

            # print ">>Got to the end with i:" , globalI
            if comment != "" and code != []:
                code = util.cleanCode(code)

                # only return true if we are in a function def
                # also no need to save code-comment pairs larger than maxBucket size
                if  not isDef(source, startLine, i) or \
                    not (util.tokenize("".join(code)) < maxBucket[0] and util.tokenize(comment) < maxBucket[1]) or \
                    (any(exc in comment.lower() for exc in commentExceptions)):
                    return (globalI+1, False)

               # write to file
                for j in xrange(len(code)):
                    codeF.write(code[j] + "\n")
                codeF.write("!@#$%!@#$%!@#$%!@#$%!@#$%")
                commentF.write(util.cleanComment(comment) + "\n!@#$%!@#$%!@#$%!@#$%!@#$%")
                # codeF.write(" ".join([x.strip() for x in code]) + "\n")

                # print "Comment:" , comment
                # print "Code:" , code, "\n"
                return (globalI+1, True)
            else:
                return (globalI+1, False)



# check if we are in a function definition
def isDef(source, startLine, i):
    # check the previous line
    containsDef = "def" in source[startLine - 1]

    # if we are not sure, check the rest of the source
    if not containsDef:
        for i in xrange(startLine, len(source)):
            if "def" in source[i]:
                containsDef = True

    # print "Contains Def:" , containsDef

    return containsDef

if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as fp:
        make_pairs(fp)