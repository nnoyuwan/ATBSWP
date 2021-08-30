# 在 Python 中，日期和时间可能涉及好几种不同的数据类型和函数。下面回顾了


# 表示时间的 3 种不同类型的值：
#  Unix 纪元时间戳（ time 模块中使用）是一个浮点值或整型值，表示自 1970 年
# 1 月 1 日午夜 0 点（ UTC）以来的秒数。
#  datetime 对象（属于 datetime 模块）包含一些整型值，保存在 year、 month、 day、
# hour、 minute 和 second 等属性中。
#  timedelta 对象（属于 datetime 模块）表示的一段时间，而不是一个特定的时刻。


# 下面回顾了时间函数及其参数和返回值：
#  time.time()函数返回一个浮点值，表示当前时刻的 Unix 纪元时间戳。
#  time.sleep(seconds)函数让程序暂停 seconds 参数指定的秒数。

#  datetime.datetime(year, month, day, hour, minute, second)函数返回参数指定的时
# 刻的 datetime 对象。如果没有提供 hour、 minute 或 second 参数，它们默认为 0。
#  datetime.datetime.now()函数返回当前时刻的 datetime 对象。
#  datetime.datetime.fromtimestamp(epoch)函数返回 epoch 时间戳参数表示的时刻
# 的 datetime 对象。

#  datetime.timedelta(weeks, days, hours, minutes, seconds, milliseconds, microseconds)函
# 数返回一个表示一段时间的 timedelta 对象。该函数的关键字参数都是可选的，
# 不包括 month 或 year。
#  total_seconds()方法用于 timedelta 对象，返回 timedelta 对象表示的秒数。

#  strftime(format)方法返回一个字符串，用 format 字符串中的定制格式来表示
# datetime 对象表示的时间。详细格式参见表 15-1。
#  datetime.datetime.strptime(time_string, format)函数返回一个 datetime 对象，它的
# 时刻由 time_string 指定，利用 format 字符串参数来解析。详细格式参见表 15-1。


