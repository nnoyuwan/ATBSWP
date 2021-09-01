import threading, time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of the program.')

# 为了创建一个 Thread 对象，
# 我们调用 threading.Thread()，并传入关键字参数 target=takeANap。这意味着我们
# 要在新线程中调用的函数是 takeANap()。请注意，关键字参数是 target=takeANap，
# 而不是 target=takeANap()。这是因为你想将 takeANap()函数本身作为参数，而不是
# 调用 takeANap()，并传入它的返回值。
# 我们将 threading.Thread()创建的 Thread 对象保存在 threadObj 中，然后调用
# threadObj.start()，创建新的线程，并开始在新线程中执行目标函数。如果运行该
# 程序，输出将像这样：
# Start of program.
# End of program.
# Wake up!


