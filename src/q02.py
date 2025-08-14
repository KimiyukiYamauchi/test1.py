# 1つの引数(整数)を受け取り以下の条件が成り立つならTrueを返す
# それ以外はFalseを返す
# 条件：
# 　90以上110以下である
# 　190以上210以下である
# 例：
# 　nearHundred(93) → True
# 　nearHundred(90) → True
# 　nearHundred(90) → True
# 
# @param int n 整数
# 
# @return 条件が成り立つならTrueを返す
#         それ以外はFalse
# 


def near_hundred(n):
    if (90 <= n <=110) or (190 <= n <= 210):
        return True
    else:
        return False
