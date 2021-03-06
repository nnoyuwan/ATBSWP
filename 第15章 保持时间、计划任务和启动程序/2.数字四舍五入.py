# 在处理时间时，你会经常遇到小数点后有许多数字的浮点值。为了让这些值更
# 易于处理，可以用 Python 内置的 round()函数将它们缩短，该函数按照指定的精度
# 四舍五入到一个浮点数。只要传入要舍入的数字，再加上可选的第二个参数，指明
# 需要传入到小数点后多少位。如果省略第二个参数， round()将数字四舍五入到最接
# 近的整数。

import time

now = time.time()
now

# 再加上可选的第二个参数，指明需要传入到小数点后多少位。
round(now, 2)  # 1630036673.82
round(now, 4)  # 1630036673.8217
# 如果省略第二个参数， round()将数字四舍五入到最接近的整数。
round(now)

