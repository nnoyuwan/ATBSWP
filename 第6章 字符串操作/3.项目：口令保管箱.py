# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/9 4:59 下午
import sys
import pyperclip

# 第 1 步：程序设计和数据结构

PASSWORDS = {'email': 'F7min l BDDuvMJuxESS KHFhTxFt jVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

# 第 2 步：处理命令行参数
if len(sys.argv) < 2:
    # 因为命令行参数是必须的，所以如果用户忘记添加参数（也就 是说，如果列表中少于两个值），你就显示用法信息。
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
# sys.argv 列表中的第一项总是一个字符串，它包含程序的文件名 （'pw.py'）。
# 第二项应该是第一个命令行参数。
account = sys.argv[1]  # first command line arg is the account name

# 第 3 步：复制正确的口令
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)


