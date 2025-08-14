# 引数(文字列)の先頭から3文字を3回結合した文字列を返す関数
# 引数が3文字に満たない場合はそれを3回結合する
# 例：
# 　front3("Java") → "JavJavJav"
# 　front3("Chocolate") → "ChoChoCho"
# 　front3("abc") → "abcabcabc"
# 
# @param string s 対象の文字列
# 
# @return 引数(文字列)の先頭から3文字を3回結合した文字列を返す
#         引数が3文字に満たない場合はそれを3回結合する
# 

def front3(s):
    if len(s) < 3:
        return s * 3
    else:
        return s[:3] * 3
