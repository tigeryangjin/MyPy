# 支付宝2.15亿奖金平分
def zfb(min_person, max_person, total_amt):
    import matplotlib.pyplot as plt
    ind = []
    dif = []
    for p in range(min_person, max_person):
        ind.append(p)
        dif_amt = round(p * (total_amt / p - round(total_amt / p, 2)), 2)
        dif.append(dif_amt)
    for i in range(max_person - min_person):
        print(ind[i], dif[i])
    plt.scatter(ind, dif)
    plt.show()


# zfb(1000, 3000, 20000)

def writer_to_csv():
    import csv

    with open("XXX.csv", "w", newline="") as datacsv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvwriter.writerow(["A", "B", "C", "D"])


def write_file():
    '''
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


# 学生成绩class
class StudentsScore:
    def __init__(self, name, homework, quizzes, tests):
        self.name = name
        self.homework = homework
        self.quizzes = quizzes
        self.tests = tests

    # Add your function below!
    def average(self):
        total = float(sum(self))
        l = len(self)
        avg = total / l
        return avg

    def get_average(self):
        homework = StudentsScore.average(self.homework)
        quizzes = StudentsScore.average(self.quizzes)
        tests = StudentsScore.average(self.tests)
        return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

    def get_letter_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"


lloyd = StudentsScore('lloyd', [90.0, 97.0, 75.0, 92.0], [88.0, 40.0, 94.0], [75.0, 90.0])
alice = StudentsScore('alice', [100.0, 92.0, 98.0, 100.0], [82.0, 83.0, 91.0], [89.0, 97.0])
tyler = StudentsScore('Tyler', [0.0, 87.0, 75.0, 22.0], [0.0, 75.0, 78.0], [100.0, 100.0])


# 斐波那契数列 方法一
def fibonacci(m):
    list1 = []
    list1.append(0)
    list1.append(1)
    a, b = 0, 1
    for i in range(m):
        a = a + b
        if len(list1) < m:
            list1.append(a)
            b = a + b
            if len(list1) < m:
                list1.append(b)
            else:
                break
        else:
            break
    return list1


# 斐波那契数列 方法二
def fib(m):
    fibs = [0, 1]
    num = m
    for i in range(int(num) - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


# 以需要的时间间隔执行某个命令
def re_exe(cmd, inc=3):
    import time
    import os
    while True:
        os.system(cmd)
        time.sleep(inc)


def plt_scatter():
    from numpy import random, ones, array
    import matplotlib.pyplot as plt
    a = random.randint(0, 50, 50)
    b = random.randint(0, 50, 50)
    fig = plt.figure(1)
    plt.subplot(211)
    plt.scatter(a, b)

    # with label
    plt.subplot(212)
    label = list(ones(20)) + list(2 * ones(15)) + list(3 * ones(15))
    label = array(label)
    # 画图，最后二个参数为颜色参数。
    # label数据类型为numpy.ndarray，有三种值（1，2，3）
    plt.scatter(a, b, 15.0 * label, 15.0 * label)
    plt.show()
    print(label)


plt_scatter()
