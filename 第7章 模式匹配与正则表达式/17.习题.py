# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/14 1:55 上午

# 20
import re

p = re.compile(r'^\d{1,3}(,\d{3})*$')
search = p.search('42')
search.group()
search = p.search('1,234')
search.group()
search = p.search('6,368,745')
search.group()
search = p.search('12,34,567')
search.group()
search = p.search('1234')
search.group()

# 21
re_compile = re.compile(r'[A-Z][a-z]+\s(Nakamoto)$')
m = re_compile.search('Satoshi Nakamoto')
m.group()
m = re_compile.search('Alice Nakamoto')
m.group()
m = re_compile.search('RoboCop Nakamoto')
m.group()
m = re_compile.search('satoshi Nakamoto')
m.group()
m = re_compile.search('Mr. Nakamoto')
m.group()
m = re_compile.search('Nakamoto')
m.group()
m = re_compile.search('Satoshi nakamoto')
m.group()

# 22
re_compile = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$', re.I)
m = re_compile.search('Alice eats apples.')
m.group()
m = re_compile.search('Bob pets cats.')
m.group()
m = re_compile.search('Carol throws baseballs.')
m.group()
m = re_compile.search('Alice throws Apples.')
m.group()
m = re_compile.search('BOB EATS CATS.')
m.group()
m = re_compile.search('RoboCop eats apples.')
m.group()
m = re_compile.search('ALICE THROWS FOOTBALLS.')
m.group()
m = re_compile.search('Carol eats 7 cats.')
m.group()
