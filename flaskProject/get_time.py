import datetime

big_month = [1,3,5,7,8,10,12]
small_month = [4,6,9,11]

now = datetime.datetime.now()
month = now.month

first_date = datetime.datetime(now.year,now.month,1,0,0)
    #年 月 日 时 分
#print(first_date.weekday()) #python的日期当中 星期范围 0-6 0代表周一
first_week = first_date.weekday() #2019年9月1号是周日

    #如果一号周周一那么第一行1-7号   0
    # 如果一号周周二那么第一行empty*1+1-6号  1
    # 如果一号周周三那么第一行empty*2+1-5号  2
    # 如果一号周周四那么第一行empty*3+1-4号  3
    # 如果一号周周五那么第一行empyt*4+1-3号  4
    # 如果一号周周六那么第一行empty*5+1-2号  5
    #如果一号周日那么第一行empty*6+1号   6
    #输入 1月
        #得到1月1号是周几
        #[] 填充7个元素 索引0对应周一
        #返回列表
if month in big_month:
    day_range = range(1,32)
elif month in small_month:
    day_range = range(1,31)
else:
    day_range = range(1, 29)
