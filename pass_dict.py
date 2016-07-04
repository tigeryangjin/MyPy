import string

# import os

# 密码字符集
charset = string.printable[:-38]
# pds = []

file_object = open('f:/pwdNum6.txt', 'w')
for ch1 in range(len(charset)):
    for ch2 in range(len(charset)):
        for ch3 in range(len(charset)):
            for ch4 in range(len(charset)):
                for ch5 in range(len(charset)):
                    file_object.write(
                        str(charset[ch1]) + str(charset[ch2]) + str(charset[ch3]) + str(charset[ch4]) + str(
                            charset[ch5]) + '\n')
file_object.close()
