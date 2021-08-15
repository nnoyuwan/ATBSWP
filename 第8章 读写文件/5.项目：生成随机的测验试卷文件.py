# -*- coding:utf-8 -*-
# author:yuwanmo
# contact: a13767092838@gmail.com
# datetime:2021/8/15 9:52 上午

# 下面是程序所做的事：
#
# • 创建 35 份不同的测验试卷。
#
# • 为每份试卷创建 50 个多重选择题，次序随机。
#
# • 为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。
#
# • 将测验试卷写到 35 个文本文件中。
#
# • 将答案写到 35 个文本文件中。

import random

state_capital_kwl = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoin',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}

for i in range(35):
    # TODO: Create the quiz and answer key files.
    quiz_file = open('capital_test%s.txt' % (i + 1), 'w', encoding='utf-8')
    ans_file = open('cpaital_ans%s.txt' % (i + 1), 'w', encoding='utf-8')
    # Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\n')
    quiz_file.write(' ' * 20 + 'State Capitals Quiz (From %s)' % (i + 1))
    quiz_file.write('\n\n')

    # Shuffle the order of the states.
    states = list(state_capital_kwl.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each.
    for j in range(50):
        correctAnswer = state_capital_kwl[states[j]]
        wrongAnswers = list(state_capital_kwl.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quiz_file.write('%s. What is the capital of %s?\n' % (j + 1, states[j]))
        for k in range(4):
            quiz_file.write('%s. %s\n' % ('ABCD'[k], answerOptions[k]))
        quiz_file.write('\n')
        ans_file.write('%s. %s\n' % (j + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quiz_file.close()
    ans_file.close()
