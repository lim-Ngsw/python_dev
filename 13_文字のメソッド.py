s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start) #True
is_start = s.startswith('X')
print(is_start) #False
'''
startswith -> ()内で指定した文字列から始まっているか、を調べることができる
始まっていればTrue, いなければFalseを返す
'''

print(s.find('Mike')) #11
print(s.rfind('Mike')) #20
'''
find/rfind -> ()内で指定した文字列がどこにあるかを探す。それぞれ何文字目から始まっているかを返してくれる。
findは前から数え、rfindは後ろから数えてくれる。
'''
print(s.count('Mike')) #2
'''
count -> ()内で指定した文字列がいくつ含まれているかを返してくれる。
'''
print(s.capitalize()) #My name is mike. hi mike.
print(s.title()) #My Name Is Mike. Hi Mike.
print(s.upper()) #MY NAME IS MIKE. HI MIKE.
print(s.lower()) #my name is mike. hi mike.
'''
capitalize -> 変数（str形式）の文頭のみを大文字にする
title -> 単語の頭を大文字にする
upper -> すべて大文字にする
lower -> すべて小文字にする
'''
print(s.replace('Mike' , 'Nancy'))
'''
replace -> 指定したワード（例ではMikeからNancy）に置き換える
'''
