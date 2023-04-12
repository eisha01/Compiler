import re

txt = "a+(b*c) or 3+ (5*2)"

x = re.findall(r"[.\(\)\*\w+]", txt)
print(x)

if(x):
    print("we have a matched string")

else:
    print("no match")