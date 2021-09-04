print('a is {}' .format('test')) #a is test
'''
format -> {}内に、指定した文字列を『代入』する。
'''
print('a is {} {} {}' .format(1,2,3)) #a is 1 2 3
print('a is {0} {1} {2}' .format(1,2,3)) #a is 1 2 3
print('a is {2} {1} {0}' .format(1,2,3)) #a is 3 2 1
'''
こうして複数入力も可能。インデックスを指定することで
並べ替えて代入することもできる。数字は型変換され文字列として代入される。
'''
print('My name is {0} {1}' .format('John', 'Smith')) #My name is John Smith.
print('My name is {name} {family}' .format(name = 'John', family = 'Smith')) #My name is John Smith.
'''
代入先として変数を使うことも可能。
'''

a = 'test'
print(f'a is {a}') #a is test

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}') #a is 1, 2, 3
print(f'a is {z}, {y}, {x}') #a is 3, 2, 1

name = 'John'
family = 'Smith'
print(f'My name is {name} {family}') #My name is John Smith.
'''
3.6以降使われるf-stringsというスタイル。
'''
