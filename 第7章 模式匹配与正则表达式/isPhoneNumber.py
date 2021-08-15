# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/11 11:10 下午
import datetime


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi Moshi is a phone number:')
print(isPhoneNumber('Moshi Moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
start = datetime.datetime.now()
for i in range(len(message)):
    chunk = message[i: i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
print('time:' + str(datetime.datetime.now() - start))
