# 2つの引数(整数)で、10以上20以下の範囲の大きいほうを返す。
# 2つの引数(整数)が、どちらも10以上20以下でない場合は0を返す
# 例：
# 　　max1020(11, 19) → 19
# 　　max1020(19, 11) → 19
# 　　max1020(11, 9) → 11
# 
# @param int $a 整数
# @param int $b 整数
# 
# @return 2つの引数(整数)で、10以上20以下の範囲の大きいほうを返す。
# 　　　　2つの引数(整数)が、どちらも10以上20以下でない場合は0を返す

def max1020(a, b):
    diff_a = 10 <= a <= 20
    diff_b = 10 <= b <= 20
    if diff_a > diff_b:
        return a
    elif diff_b > diff_a:
        return b
    else:
        return 0
