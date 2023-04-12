import re
import ast

regular_expression = "a+(b*c)"

regular_expression_2 = "3+ (5*2)"

y = re.findall(r"[.\()\*\w+]", regular_expression)

x = re.findall(r"[.\()\*\w+]", regular_expression_2)

syntax_tree = ast.parse("print(3+(5*2))")
print(ast.dump(syntax_tree))
exec(compile(syntax_tree, filename="", mode="exec"))

syntax_tree_2 = ast.parse("print('a+(b*c)')")
print(ast.dump(syntax_tree_2))
exec(compile(syntax_tree_2, filename="", mode="exec"))



print(y)

print(x)

