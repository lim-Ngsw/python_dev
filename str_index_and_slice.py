word =('python')
#index
print(word[0]) #1文字目を取り出す＝p
print(word[1]) #2文字目を取り出す=y
print(word[-1]) #最後の文字を取り出す =n

#slice
print(word[0:2]) #インデックスの0と1を取り出す=pとy
print(word[2:5]) #インデックスの2〜4＝tho

print('#################')
print(word[0:2]) #py
print(word[:2]) #py
print('#################')
print(word[2:]) #thon
#print(word[100]) 存在しないインデックスはエラー表示になる
word = 'j' + word[1:] #一文字目をjに置き換える
print(word) #jython

n=len(word) #len = length（文字数を表示する）
print(n) #6
