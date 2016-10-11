import re

str1 = 'name="_xsrf" value="2348b677e4b74c5e06a2a443b2a3e0f6"'
cer = re.compile('value="(.*)"', flags=0)
strlist = cer.findall(str1)
