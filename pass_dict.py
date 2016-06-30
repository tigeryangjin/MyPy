import os
import string

chars = string.printable[:-5]  # 后面5个是换行、tab等字符
chars = ''.join([chr(i) for i in range(32, 127)])


pds = []

rg = range(0, 10)

for first in rg:
    for second in rg:
        for three in rg:
            for four in rg:
                for five in rg:
                    for six in rg:
                        num = "%s%s%s%s%s%s" % (first, second, three, four, five, six)
                        pds.append(num)
print(type(pds))
print(pds[8])
file_object = open('f:/pwdNum6.txt', 'w')
file_object.writelines(['%s%s' % (x, os.linesep) for x in pds])
file_object.close()
