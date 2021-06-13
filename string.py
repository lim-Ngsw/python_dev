s = 'test'
print(s)

print('hello')
print("hello")
print("I don't know")
print('I don\'t know') #バックスラッシュを前につける= 文字列という認識
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?') #\n =改行
print(r'C:\name\name') #r =raw data（生データ）
print("###################")
print("""\
line1
line2
line3\
""")
print("###################")
print('Hi.' * 3 + 'Mike.') #演算子を用いることも可能
print('py''thon') #python
prefix = 'py'
print(prefix + 'thon') #変数を含む場合は演算子を使わないとエラー

#演算子を使わずリテラル同士でつなげるメリット→下記のように長いコードを描く際は見やすくできる
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s) #1行で表示される
