''''' 
Created on Dec 18, 2012 
写入文件 
@author: liury_lab 
'''
# 最简单的方法
all_the_text = 'hello python'
open('d:/text.txt', 'w').write(all_the_text)
all_the_data = b'abcd1234'
open('d:/data.txt', 'wb').write(all_the_data)
# 更好的办法
file_object = open('d:/text.txt', 'w')
file_object.write(all_the_text)
file_object.close()
# 分段写入
list_of_text_strings = ['hello', 'python', 'hello', 'world']
file_object = open('d:/text.txt', 'w')
for string in list_of_text_strings:
    file_object.writelines(string)
list_of_text_strings = ['hello', 'python', 'hello', 'world']
file_object = open('d:/text.txt', 'w')
file_object.writelines(list_of_text_strings)
