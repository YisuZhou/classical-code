# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ans = []
        i_left = 0
        i_right = len(array)-1
        
        while i_left < i_right:
            if array[i_left] + array[i_right] == tsum:
                ans.append([i_left,i_right])
                i_left += 1
                i_right -= 1
            elif array[i_left] + array[i_right] > tsum:
                i_right -= 1
            else:
                i_left += 1
        if ans:  
            # 因为递增，所以乘积最小的就是差距最大的。ab = ((a+b)^2 - (a-b)^2) / 4, a+b = tsum
            return [array[ans[0][0]],array[ans[0][1]]]
        else:
            return []
            
            
# 变体：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 如果没有等于的，输出两数之和最接近S的那对
def FindNumbersWithSum2(self, array, tsum):
    i_left = 0
    i_right = len(array)-1
    gap_min = tmux
    while i_left < i_right:
        if array[i_left] + array[i_right] == tsum:
            gap_min = 0
            ans= [array[i_left],array[i_right]]
            break
        elif array[i_left] + array[i_right] > tsum:
            if array[i_left] + array[i_right] - tsum < gap_min:
                gap_min = array[i_left] + array[i_right] - tsum
                ans = [array[i_left],array[i_right]]
            i_right -= 1
        else:
            if tmux - array[i_left] - array[i_right] < gap_min:
                gap_min = tmux - array[i_left] - array[i_right]
                ans = [array[i_left],array[i_right]]
            i_left += 1
   return ans
