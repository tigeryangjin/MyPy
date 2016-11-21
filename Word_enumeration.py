import random

word = 'TOBEORNOTTOBE'


def random_letter(n):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(n))


random_word = random_letter(13)
word_list = list(word)
random_word_list = list(random_word)

print(word_list, random_word_list)
