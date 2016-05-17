to_21=[x for x in range(1,22)]
odds=to_21[::2]
middle_third=to_21[7:14]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message=garbled[::-1][::2]

'''
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message=filter(lambda x:x<>"X",garbled)
print(message)


print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)   # Bitwise AND
print(9 | 4)   # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT
'''

def check_bit4(input):
    x=bin(input)
    i=x[::-1][3:4]
    if i==str(1):
        return "on"
    else:
        return "off"


#print(check_bit4(0b1000))

def flip_bit(number,n):
    mask=(0b1<<n-1)
    return bin(number^mask)

print(flip_bit(0b1010101, 3))
#0b101