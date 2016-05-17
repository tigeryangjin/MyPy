# 身份证号码效验
def id_check(uid):
    if len(str(uid)) != 18:
        return uid, False
    else:
        mul_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 剔除输入身份证号码的最后一位
        id_list = list(str(uid))[0:len(list(str(uid))) - 1]
        last_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        sum_value = 0
        for i in range(len(id_list)):
            sum_value += int(mul_list[i]) * int(id_list[i])
        check_code = last_list[sum_value % 11]
        last_code = list(str(uid))[-1]
        if str(last_code) == str(check_code):
            return uid, True
        else:
            return uid, False


print(id_check('430203790909001'))
print(id_check('43020319790909001X'))
print(id_check('430203197909090012'))
