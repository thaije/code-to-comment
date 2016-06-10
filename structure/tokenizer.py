import tokenize

file = open("code.txt")

# something = tokenize.generate_tokens(file.readline)

# for line in list(something):
# 	print line

def handle_token(type, token, (srow, scol), (erow, ecol), line):
    print "%d,%d-%d,%d:\t%s\t%s" % \
        (srow, scol, erow, ecol, tokenize.tok_name[type], repr(token))

tokenize.tokenize(
    file.readline,
    handle_token
    )
