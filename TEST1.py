import re

str1 = 'name:yangjin age:36 jf:xxx'
pattern1 = re.compile(r'name:(.*) age:(.*) jf:(.*)')
data = pattern1.findall(str1)
print(data)
print(type(data))
