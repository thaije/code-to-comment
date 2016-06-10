# -*- coding: utf-8 -*-
"""Parse Python source code and get docstrings with their corresponding code."""

__all__ = ('get_docstrings', 'print_docstrings')

import ast
import cStringIO, tokenize
import re

from itertools import groupby
from os.path import basename, splitext


NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}


def get_docstrings(source):
    """Parse Python source code and yield a tuple of ast node instance, name,
    line number and docstring for each function/method, class and module.
    
    The line number refers to the first line of the docstring. If there is
    no docstring, it gives the first line of the class, funcion or method
    block, and docstring is None.
    """ 
    tree = ast.parse(source)
    
    for node in ast.walk(tree):
        if isinstance(node, tuple(NODE_TYPES)):
            docstring = ast.get_docstring(node)
            lineno = getattr(node, 'lineno', None)

            if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Str)):
                # lineno attribute of docstring node is where string ends 
                lineno = node.body[0].lineno - len(node.body[0].value.s.splitlines()) + 1

            yield (node, getattr(node, 'name', None), lineno, docstring)


def generate_pairs(source, module='<string>'):
    """Parse Python source code from file or string and print docstrings 
    and line numbers. Only print for functions/methods, and only with 
    a non-empty docstring.
    
    The line number is the first line number of the definition, the last 
    from the last line
  
    """
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()

    docstrings = sorted(get_docstrings(source),
        key=lambda x: (NODE_TYPES.get(type(x[0])), x[1]))
    grouped = groupby(docstrings, key=lambda x: NODE_TYPES.get(type(x[0])))
    
    i = 0

    for type_, group in grouped:
        for node, name, lineno, docstring in group:

            print('-' * 50)

            print i
            i += 1
            print "Line:" , lineno

            # only use functions
            if not (isinstance(node,ast.FunctionDef) or isinstance(node,ast.ClassDef)):
                print " Not an function, skipping"
                print node
                continue

            # only use code with an non-empty docstring
            if docstring.strip() is '':
                print "Docstring empty, skipping"
                continue

            # calc first line, get source code 
            lineno = lineno - 2
            sourceCode = getSourceCode(lineno, source)

            if "Class" in sourceCode:
                print "Class definition, skipping"
                continue

            print "normal comments:" , ('# ' in sourceCode)
            print "doc strings:" , sourceCode.count('"""')
            print node 

            # skip the function if it contains normal comments
            hasComments = ('# ' in sourceCode) or (sourceCode.count('"""') >= 4)
            if hasComments:
                print "contains comments, skipping"
                continue

            #remove comments / docstrings and empty lines
            sourceCode = removeCommentsAndDocstrings(sourceCode)

            print "Type:" , type_
            print "Name:" , name
            print "Docstring:" , docstring , "\n"
            print "Source code: \n", sourceCode



# Get the line number of the last object in the node 
def getSourceCode(firstLine, source):

    # Split the source code into a list
    source = source.splitlines()

    # get the first line of this function and count the indents
    firstLineStr = source[firstLine]
    indents = len(firstLineStr) - len(firstLineStr.lstrip())

    functionCode = firstLineStr + "\n"
    # add lines of code to the our string untill we have found 
    # the next function, or the EOF
    for i in xrange(firstLine + 1, len(source)):

        currentIndents = len(source[i]) - len(source[i].lstrip())

        if currentIndents > indents:
            functionCode += source[i] + "\n"
        elif source[i] == "":
            continue
        else:
            break

    return functionCode



def removeCommentsAndDocstrings(source):
    """
    Returns 'source' minus comments and docstrings.
    """
    io_obj = cStringIO.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        # The following two conditionals preserve indentation.
        # This is necessary because we're not using tokenize.untokenize()
        # (because it spits out code with copious amounts of oddly-placed
        # whitespace).
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        # Remove comments:
        if token_type == tokenize.COMMENT:
            pass
        # This series of conditionals removes docstrings:
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
        # This is likely a docstring; double-check we're not inside an operator:
                if prev_toktype != tokenize.NEWLINE:
                    # Note regarding NEWLINE vs NL: The tokenize module
                    # differentiates between newlines that start a new statement
                    # and newlines inside of operators such as parens, brackes,
                    # and curly braces.  Newlines inside of operators are
                    # NEWLINE and newlines that start new code are NL.
                    # Catch whole-module docstrings:
                    if start_col > 0:
                        # Unlabelled indentation means we're inside an operator
                        out += token_string
                    # Note regarding the INDENT token: The tokenize module does
                    # not label indentation inside of an operator (parens,
                    # brackets, and curly braces) as actual indentation.
                    # For example:
                    # def foo():
                    #     "The spaces before this docstring are tokenize.INDENT"
                    #     test = [
                    #         "The spaces before this string do not get a token"
                    #     ]
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line

    # remove empty lines
    out = "\n".join([line for line in out.split('\n') if line.strip() != ''])
    
    return out


if __name__ == '__main__':
    import sys
    
    with open(sys.argv[1]) as fp:
        generate_pairs(fp)