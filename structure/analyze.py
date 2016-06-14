import re
import grammar
import tokenize

file = open("code.txt")


for token in tokenize.generate_tokens(file.readline):

    token = token[1].strip()

    # print "Token is:" , type(token)

     # skip empty spaces
    if token.strip() == "":
        pass
    elif grammar.is_keyword(token):
        pass
    elif grammar.is_literal(token):
        pass
    elif grammar.is_operator(token):
        pass
    elif grammar.is_identifier(token):
        pass
    elif grammar.is_delimeter(token):
        pass
    # elif grammar.is_indent(token):
    #     pass
    elif grammar.is_newline(token):
        pass
    else:
        print "(No idea", token , ")"
        pass

print "(ENDMARKER)"     

# tokenize.tokenize(file.readline)

# lines = fin.readlines()
# if len(lines) <= 0:
#     print "Input file %s is empty" % myfile 
#     quit(0)

# def breakup_line(line):
#     words = line.split()
#     newwords = []
#     for i in range(len(words)):
#         if words[i][0] in ("'",'"') and words[i][-1] in ("'",'"'): # don't break strings
#             newwords.append(words[i])
#         else: # break up further based on punctuation
#             t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
#             newwords.extend(t)
#     return newwords
            
# def get_strings(words):
#     new_words = []
#     adding = False
#     tmpstring = ''
#     skip = False
#     for w in words:
#         if ('"' in w or "'" in w) and (w.count('"') < 2 and w.count("'") < 2):
#             adding = not adding
#         if not adding:
#             new_words.append(tmpstring+w)
#             tmpstring = ''
#             skip = True
#         if adding:
#             tmpstring += w + ' '
#         else:
#             if skip:
#                 skip = False
#             else:
#                 new_words.append(w)
#     return new_words
            

# skip = False
# for line in lines:
#     if '#' in line:
#         line = line[:line.index('#')]
#     tokens = breakup_line(line)
#     final = get_strings(tokens)
#     for c, item in enumerate(final):
#         if not skip:

#             # comments are already filtered from input
#             # if is_comment(item):
#             #     pass
#             # skip empty spaces
#             if item.strip() == "":
#                 pass

#             elif grammar.is_keyword(item):
#                 pass
#             elif grammar.is_literal(item):
#                 pass
#             elif grammar.is_operator(item):
#                 pass
#             elif grammar.is_identifier(item):
#                 pass
#             elif grammar.is_delimeter(item):
#                 pass
#             elif grammar.is_indent(item):
#                 pass
#             elif grammar.is_newline(item):
#                 pass


#             if is_op(item):
#                 try:
#                     if is_op(item + final[c+1]):
#                         print '(OP "%s")' % str(item + final[c+1])
#                         skip = True
#                     else:
#                         print '(OP "%s")' % item 
#                 except:
#                     print '(OP "%s")' % item 

#             elif is_del(item):
#                 pass
#             elif is_keyword(item):
#                 pass
#             elif is_ID(item):
#                 pass
#             else:
#                 print "(LIT %s)" % item
#         else:
#             skip = False  



# print "(ENDMARKER)"
