# time 模块用于取得 Unix 纪元时间戳，并加以处理。但是，如果以更方便的格
# 式显示日期，或对日期进行算术运算（例如，搞清楚 205 天前是什么日期，或 123
# 天后是什么日期），就应该使用 datetime 模块。

# datetime 模块有自己的 datetime 数据类型。 datetime 值表示一个特定的时刻。 在交
# 互式环境中输入以下代码：

import datetime
import time

datetime.datetime.now()
# datetime.datetime(2021, 8, 27, 19, 44, 5, 375525)
#                    年、 月、 日、 时、分、 秒和 微秒。
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day  # (2015, 10, 21)
dt.hour, dt.minute, dt.second  # (16, 29, 0)

# Unix 纪元时间戳可以通过 datetime.datetime.fromtimestamp()，转换为 datetime
# 对象。 datetime 对象的日期和时间将根据本地时区转换。在交互式环境中输入以下
# 代码：
datetime.datetime.fromtimestamp(1000000)
# datetime.datetime(1970, 1, 12, 21, 46, 40)
datetime.datetime.fromtimestamp(time.time())
# datetime.datetime(2021, 8, 27, 19, 49, 54, 748509)

# 调用 datetime.datetime.fromtimestamp()并传入 1000000，返回一个 datetime 对
# 象， 表示 Unix 纪元后 1000000 秒的时刻。

# 表达式 datetime.datetime.now()
# 和 datetime.datetime.fromtimestamp(time.time())做的事情相同，它们都返回当前时刻
# 的 datetime 对象。

# datetime 对象可以用比较操作符进行比较，弄清楚谁在前面。后面的 datetime 对象
# 是“更大”的值。在交互式环境中输入以下代码：
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
halloween2015 == oct31_2015
halloween2015 > newyears2016
newyears2016 > halloween2015
newyears2016 != oct31_2015
# 比较 halloween2015 和 oct31_2015，它们是相等的。比
# 较 newyears2016 和 halloween2015， newyears2016 大于（晚于） halloween2015 。


# 15.4.1 timedelta 数据类型

# datetime 模块还提供了 timedelta 数据类型，它表示一段时间，而不是一个时刻。
timedelta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
timedelta.days, timedelta.seconds, timedelta.microseconds
# timedelta.seconds指除days之外的秒

timedelta.total_seconds()
str(timedelta)  # '11 days, 10:09:08'
# total_seconds指包括days的秒

# 我们将关键字参数传入 datetime.delta()，指定 11 天、 10 小时、
# 9 分和 8 秒的时间，将返回的 timedelta 对象保存在 delta 中。该 timedelta 对象的
# days 属性为 11， seconds 属性为 36548（ 10 小时、 9 分钟、 8 秒，以秒表示） 。
# 调用 total_seconds()告诉我们， 11 天、 10 小时、 9 分和 8 秒是 986948 秒。


dt = datetime.datetime.now()
dt
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays

# 利用+和-运算符， timedelta 对象与 datetime 对象或其他 timedelta 对象相加或相
# 减。利用*和/运算符， timedelta 对象可以乘以或除以整数或浮点数。在交互式环境
# 中输入以下代码：
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st  # datetime.datetime(2015, 10, 21, 16, 29)
oct21st - aboutThirtyYears  # datetime.datetime(1985, 10, 28, 16, 29)
oct21st - 2 * aboutThirtyYears  # datetime.datetime(1955, 10, 28, 16, 29)

# 15.4.2 暂停直至特定日期
halloween2021 = datetime.datetime(2021, 8, 27, 21, 58, 50)
while datetime.datetime.now() < halloween2021:
    time.sleep(1)
print('Done!')

# time.sleep(1)调用将暂停你的 Python 程序，这样计算机不会浪费 CPU 处理周期，
# 一遍又一遍地检查时间。相反， while 循环只是每秒检查一次，在 2016 年万圣节（或
# 你编程让它停止的时间）后继续执行后面的程序


# 15.4.3 将 datetime 对象转换为字符串

# Unix 纪元时间戳和 datetime 对象对人类来说都不是很友好可读。利用 strftime()方
# 法，可以将 datetime 对象显示为字符串。（ strftime()函数名中的 f 表示格式， format）。
# 该的 strftime()方法使用的指令类似于 Python 的字符串格式化。表 15-1 列出了完
# 整的 strftime()指令
# 表 15-1 strftime()指令
# strftime指令                    含义
# %Y                       带世纪的年份，例如'2014'
# %y                       不带世纪的年份， '00'至'99'（ 1970 至 2069）
# %m                       数字表示的月份, '01'至'12'
# %B                       完整的月份，例如'November'
# %b                       简写的月份，例如'Nov'
# %d                       一月中的第几天， '01'至'31'
# %j                       一年中的第几天， '001'至'366'
# %w                       一周中的第几天， '0'（周日）至'6'（周六）
# %A                       完整的周几，例如'Monday'
# %a                       简写的周几，例如'Mon'
# %H                       小时（ 24 小时时钟）， '00'至'23'
# %I                       小时（ 12 小时时钟）， '01'至'12'
# %M                       分， '00'至'59'
# %S                       秒， '00'至'59'
# %p                       'AM'或'PM'
# %%                       就是'%'字符

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')  # '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')  # '04:29 PM'
oct21st.strftime("%B of '%y")  # "October of '15"

# 15.4.4 将字符串转换成 datetime 对象
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')  # datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')  # datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of '%y")  # datetime.datetime(2015, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")  # datetime.datetime(2063, 11, 1, 0, 0)

# 要从字符串'October 21, 2015'取得一个 datetime 对象，将'October 21, 2015'作为
# 第一个参数传递给 strptime()，并将对应于'October 21, 2015' 的定制格式字符串作为
# 第二个参数。带有日期信息的字符串必须准确匹配定制的格式字符串，否则 Python
# 将抛出 ValueError 异常


