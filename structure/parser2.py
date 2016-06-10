# import ast

# file = "code.txt"
# r = open(file,'r')

# node = ast.parse(r.read(), mode='eval') 

# ast.dump(node, True, True)

import ast
import astpp
 
file = "code.txt"	
r = open(file,'r')
tree = ast.parse(r.read())

print astpp.dump(tree)