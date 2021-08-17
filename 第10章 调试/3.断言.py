# “断言”是一个心智正常的检查，确保代码没有做什么明显错误的事情。这些
# 心智正常的检查由 assert 语句执行。如果检查失败，就会抛出异常。在代码中， assert
# 语句包含以下部分：

# • assert 关键字；
# • 条件（即求值为 True 或 False 的表达式）；
# • 逗号；
# • 当条件为 False 时显示的字符串。

podBayDoorStatus = 'open'
# 这里，我们加入了信息 'The pod bay doors need to be "open".'，这样如果断言失败，就很容易看到哪里出了错。
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t to do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# AssertionError: The pod bay doors need to be "open".

# 稍后，假如我们犯了一个明显的错误，把另外的值赋给 podBayDoorStatus，但
# 在很多行代码中，我们并没有意识到这一点。这个断言会抓住这个错误，清楚地告
# 诉我们出了什么错。

# 在日常英语中， assert 语句是说：“我断言这个条件为真，如果不为真，程序中什
# 么地方就有一个缺陷。”不像异常，代码不应该用 try 和 except 处理 assert 语句。如果
# assert 失败，程序就应该崩溃。通过这样的快速失败，产生缺陷和你第一次注意到该缺
# 陷之间的时间就缩短了。这将减少为了寻找导致该缺陷的代码，而需要检查的代码量。


# 10.3.1 在交通灯模拟中使用断言
# 假定你在编写一个交通信号灯的模拟程序。代表路口信号灯的数据结构是一个
# 字典，以 'ns' 和 'ew' 为键，分别表示南北向和东西向的信号灯。这些键的值可以
# 是 'green'、 'yellow' 或 'red' 之一。代码看起来可能像这样：

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


# 这两个变量将针对 Market 街和第 2 街路口，以及 Mission 街和第 16 街路口。 作
# 为项目启动，你希望编写一个 switchLights() 函数，它接受一个路口字典作为参数，
# 并切换红绿灯。

# 开始你可能认为， switchLights() 只要将每一种灯按顺序切换到下一种顔色：
# 'green' 值应该切换到 'yellow'， 'yellow' 应该切换到 'red'， 'red' 应该切换到'green'。实
# 现这个思想的代码看起来像这样：

def switchLight(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)


switchLight(market_2nd)
print(market_2nd)

# 你可能已经发现了这段代码的问题，但假设你编写了剩下的模拟代码，有几千
# 行，但没有注意到这个问题。当最后运行时，程序没有崩溃，但虚拟的汽车撞车了！

# 因为你已经编写了剩下的程序，所以不知道缺陷在哪里。也许在模拟汽车的代
# 码中，或者在模拟司机的代码中。可能需要花几个小时追踪缺陷，才能找到
# switchLights() 函数。

# 但如果在编写 switchLights() 时，你添加了断言，确保至少一个交通灯是红色，
# 可能在函数的底部添加这样的代码：

# 这里重要的一行是 AssertionError。虽然程序崩溃并非如你所愿，但它马上指
# 出了心智正常检查失败：两个方向都没有红灯，这意味着两个方向的车都可以走。
# 在程序执行中尽早快速失败，可以省去将来大量的调试工作。


# 10.3.2 禁用断言
# 在运行 Python 时传入-O 选项，可以禁用断言。如果你已完成了程序的编写和
# 测试，不希望执行心智正常检测，从而减慢程序的速度，这样就很好（尽管大多数
# 断言语句所花的时间，不会让你觉察到速度的差异）。断言是针对开发的，不是针
# 对最终产品。当你将程序交给其他人运行时，它应该没有缺陷，不需要进行心智正
# 常检查。如何用-O 选项启动也许并不疯狂的程序，详细内容请参考附录 B。
