import string

chars = string.printable[:-5]  # 后面5个是换行、tab等字符
chars = ''.join([chr(i) for i in range(32, 127)])

print(chars)

# p = []
# for i in chars:
#     for j in chars:
#         p.append(i + j)
# print(p)

p = [i + j for i in chars for j in chars]
print(p)
