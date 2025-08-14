# 引数(文字列)のindexが1の位置から"del"があればそれを削除して返す
# なければ引数(文字列)をそのまま返す関数
# 例：
# 　del_del("adelbc") → "abc"
# 　del_del("adelHello") → "aHello"
# 　del_del("adedbc") → "adedbc"
# 
# @param string str 文字列
# 
# @return 引数(文字列)のindexが1の位置から"del"があればそれを削除して返す
# 　　　　なければ引数(文字列)をそのまま返す
# 
#/

def del_del(str):
    if str[1:4] == "del":
        return str[0] + str[4:]
    else:
        return str
