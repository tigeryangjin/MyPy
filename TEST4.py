import datetime


def get_v_date(default=str(datetime.date.today() - datetime.timedelta(days=1))):
    r = input('请输入日期（格式：yyyy-mm-dd，默认值为昨天）: ')
    if r == '':
        return default
    return r

print(get_v_date())