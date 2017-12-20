print('''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')

age=36
name='Derek'
print('{0} is {1} years old when he wrote this book'.format(name,age))
print("Why is {0} playing with that python?".format(name))
print('{name} is {age} years old when he wrote this book'.format(name='Daisy',age=37))

print('{0:.3f}'.format(1.0/3))     # 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:_^11}'.format('hello'))  # 使用下划线填充文本，并保持文字处于中间位置使用 (^) 定义 '___hello___'字符串长度为 11

print('a',end=' ')
print('b',end=' ')
print('c')

print("what\'s your name?")
print("what\'s your name?\\")
print("This is the first line.\nThis is the second line")
print("This is the first line.\tThis is the second line")
print("This is the first line.\
This is the second line")