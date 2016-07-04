import string

charset = string.printable[:-38]
for i in range(999999999999):
    for ch1 in range(len(charset)):
        for ch2 in range(len(charset)):
            password = str(charset[ch1]) + str(charset[ch2])
            print(i, password)
