import re
s = '''See the U.S.A today. It's right here, not 
a world away. Average temp. is 66.5.'''
# s = str(input("Please input a string of text of any length."))
pat = r'[A-Z].*?[.!?] (?=[A-Z]|$)' 
m = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)
print(m)
for i in m:
    print('->', i)