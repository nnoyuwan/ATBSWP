myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# 这个字典的键是'size'、 'color'和'disposition'。
# 这些键相应的值是'fat'、 'gray'和'loud'。
var = myCat['size']
print(var)

var = 'My cat has ' + myCat['color'] + ' fur.'
print(var)

# 字典仍然可以用整数值作为键， 就像列表使用整数值作为下标一样，
# 但它们不必从 0 开始，可以是任何数字。
spam = {12345: 'Luggage Combination', 42: 'The Answer'}

# 虽然确定两个列表是否相同时， 表项的顺序很重要
spam = ['cats', 'dogs', 'moose']
spam1 = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(id(spam))
print(id(spam1))
print(spam == spam1)  # True ==判断值相等
print(spam is spam1)  # False ==判断引用相等

# 但在字典中，键-值对输入的顺序并不重要
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  # 因为字典是不排序的，所以不能像列表那样切片。

spam = {'name': 'Zophie', 'age': 7}
print(spam['color'])  # KeyError: 'color'
