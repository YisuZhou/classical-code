# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        if row < 1:
            return False
        col = len(array[0])
        if col < 1:
            return False
        #上下界限，上，看每行最后一列元素>=目标，下，看每行第一列元素>目标，【上，下）
        i_min = 0
        i_max = row #不要 -1 ！！！
        for i in range(row):
            if array[i][-1] >= target:
                i_min = i
                break
        for ii in range(i_min,row):
            if array[ii][0] > target:
                i_max = ii
                break
        #左右界限，左，看每列最后一行元素>=目标，右，看每列第一行元素>目标，【左，右）
        j_min = 0
        j_max = col  # 不要 -1  ！！！
        for j in range(col):
            if array[-1][j] >= target:
                j_min = j
                break
        for jj in range(j_min,col):
            if array[0][jj] > target:
                j_max = jj
                break
        #确定范围后再找一遍
        for r in range(i_min,i_max):
            for c in range(j_min,j_max):
                if array[r][c] == target:
                    return True
        return False
