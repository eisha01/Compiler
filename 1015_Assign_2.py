import ast

tree = ast.parse("print(3+(5*2))")
print(ast.dump(tree))
exec(compile(tree, filename="", mode="exec"))

