import random


def random_letter(n):
    # 生成n长度的随机字符串
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(n))


def single_ns(word):
    # 单次自然选择
    word = word.upper()
    length = len(word)
    s = '{:>' + str(length) + '}'
    word_tmp = s.format('')  # 生成固定长度的空字符串

    word_tmp_list = list(word_tmp)
    word_list = list(word)
    count = 0

    while word_list != word_tmp_list:
        random_word = random_letter(int(length))
        random_word_list = list(random_word)
        count += 1
        for i in range(len(word_list)):
            if word_list[i] == random_word_list[i]:
                word_tmp_list[i] = random_word_list[i]
        print(word_tmp_list, random_word_list, count)


def ns(word):
    word = word.upper()
    length = len(word)
    s = '{:>' + str(length) + '}'
    word_tmp = s.format('')

    word_tmp_list = list(word_tmp)
    word_list = list(word)
    count = 0

    while word_list != word_tmp_list:
        random_word = random_letter(int(length))
        random_word_list = list(random_word)
        count += 1
        for i in range(len(word_list)):
            if word_list[i] == random_word_list[i]:
                word_tmp_list[i] = random_word_list[i]
    return count


def avg_count(word, n):
    # 自然选择平均次数
    sum_count = 0
    for i in range(n):
        sum_count += ns(word)
    return sum_count / n


print(avg_count('G', 10))
print(single_ns('tigeryangjin'))
