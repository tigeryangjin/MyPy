import random


def get_code():
    source = list('0123456789')
    for i in range(97, 123):
        source.append(chr(i))
    print(''.join(random.sample(source, 4)))


print(get_code())
