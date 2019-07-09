# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num):
            return []
        if len(num) <1 or size <1:
            return []
        ans = []
        for i in range(len(num)-(size-1)):
            ans.append(max(num[i:i+size]))
        return ans
