import astdump
import ast

file = "code.txt"	
r = open(file,'r')
tree = ast.parse(r.read())


astdump.indented(tree)