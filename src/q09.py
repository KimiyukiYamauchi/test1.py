# 与えられた文字列の末尾の2文字が文字列中に現れる数を返す処理
# 例：
# 　last2("hixxhi") → 1
# 　last2("xaxxaxaxx") → 1
# 　last2("axxxaaxx") → 2
# 
# @param string str 文字列
# 
# @return 上記の条件での数を返す

def last2(str):
    if len(str) < 2:
        return 0

    last2 = str[-2:]
    count = 0

    for i in range(len(str) - 2):
        if str[i:i+2] == last2:
            count += 1

    return count
