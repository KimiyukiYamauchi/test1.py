# 文字列と非負の整数を受け取り、文字列の最初3文字を非負の整数回繰り返した文字列を返す
# 但し、文字列は3文字より少ないことがある
# 例：
# 　front_times("Chocolate", 2) → "ChoCho"
# 　front_times("Chocolate", 3) → "ChoChoCho"
# 　front_times("Abc", 3) → "AbcAbcAbc"
# 
# @param bool str 先頭3文字を繰り返す
# @param bool n 繰り返し回数
# 
# @return 文字列の最初3文字を非負の整数回繰り返した文字列
# 

def front_times(str, n):
    if len(str) >= 3:
        return str[:3] * n
    else:
        return str * n
