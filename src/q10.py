# 与えられたint型の配列に1,2,3の並びの要素があればtrue、
# それ以外はfalseを返す関数
# 例：
# 　array123([1, 1, 2, 3, 1]) → true
# 　array123([1, 1, 2, 4, 1]) → false
# 　array123([1, 1, 2, 1, 2, 3]) → true
# 
# @param array nums int型の配列
# 
# @return 上記の条件でbool値を返す
# 

def array123(nums):
    a = 0
    if len(nums) < 2:
        return False
    else:
        for num in nums:
            if nums[num-2] == 1 and nums[num-1] == 2 and  nums[num] == 3:
                a += 1
        if a >= 1:
            return True
        elif a == 0:
            return False
