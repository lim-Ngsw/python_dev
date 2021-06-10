num = 1
name = 'Mike'
is_ok = True

print(num, type(num)) #int型
print(name, type(name)) #str型
print(is_ok, type(is_ok)) #bool型

num = name
print(num, type(num)) #str型として認識される

name = '1' #文字列としての1
new_num = int(name) #型変換
print(new_num, type(new_num)) #int型として変換される

"""
num: int = 1
name:str = Mike

上記のような『型宣言』も存在する。
機能そのものには影響はないが可読性には良いのかも。

"""
"""
エラー例
1num = 1 （文頭に数字）
if = 1 （すでに機能が割り当てられているもの）

上記のような使い方はSyntax Errorとなる。
"""
