# 15.3 项目：超级秒表


# 假设要记录在没有自动化的枯燥任务上花了多少时间。你没有物理秒表，要为
# 笔记本或智能手机找到一个免费的秒表应用，没有广告，且不会将你的浏览历史发
# 送给市场营销人员，又出乎意料地困难（在你同意的许可协议中，它说它可以这样做。
# 你确实阅读了许可协议，不是吗？）。你可以自己用 Python 写一个简单的秒表程序。
# 总的来说，你的程序需要完成：

#  记录从按下回车键开始，每次按键的时间，每次按键都是一个新的“单圈”。
#  打印圈数、总时间和单圈时间。

# 这意味着代码将需要完成以下任务：
#  在程序开始时，通过调用 time.time()得到当前时间，将它保存为一个时间戳。
# 在每个单圈开始时也一样。
#  记录圈数，每次用户按下回车键时加 1。
#  用时间戳相减，得到计算流逝的时间。
#  处理 KeyboardInterrupt 异常，这样用户可以按 Ctrl-C 退出。

# 打开一个新的文件编辑器窗口，并保存为 stopwatch.py。

# 第 1 步：设置程序来记录时间
# 秒表程序需要用到当前时间，所以要导入的 time 模块。程序在调用 input()之前，
# 也应该向用户打印一些简短的说明，这样计时器可以在用户按下回车键后开始。然
# 后，代码将开始记录单圈时间。

# ! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, '
      'press ENTER to "click" the stopwatch.'
      'Press Ctrl-C to quit.')

input()  # press Enter to begin
print('Started.')

startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.

# 第 2 步：记录并打印单圈时间
# 现在，让我们编码开始每一个新的单圈，计算前一圈花了多少时间，并计算自
# 启动秒表后经过的总时间。我们将显示的单圈时间和总时间，为每个新的单圈增加
# 圈计数。将下面的代码添加到程序中：

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    pass

# 在行，我们打印出圈数，消耗的总时间和单圈时间。由于用户为 input()调用
# 按下回车时，会在屏幕上打印一个换行，所以我们向 print()函数传入 end=''，避免
# 输出重复空行。
