import datetime

a = str(datetime.date.today() - datetime.timedelta(days=1))
v_date = input('请输入日期（格式：yyyy-mm-dd，默认值为昨天）: '+a)


