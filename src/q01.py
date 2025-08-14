# sum_double: ２つの引数(整数)の合計を返す関数
# ２つの引数(整数)の合計を返す、但し２つの引数が等しい場合は合計の2倍を返す関数
# 例：
# 　sum_double(1, 2) → 3
# 　sum_double(3, 2) → 5
# 　sum_double(2, 2) → 8
# 
# @param int a 整数
# @param int b 整数
# 
# @return ２つの引数(整数)の合計、但し２つの引数が等しい場合は合計の2倍
# 

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return (a + b)
