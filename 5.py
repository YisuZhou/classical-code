#给定一个未排序的整数数组（可能出现重复），找出最长连续序列的长度。要求算法的时间复杂度为 O(n)。

# 这个时间复杂度，肯定是不能先排序的了
# map有个很神奇的点，查找的时间复杂度是O（1），python中，list的in是O（n），但是dict的in是O（1）

# 那我们就可以一次遍历数组，每次更新左右的信息。对于数字i，找到i-1和i+1对应的value值,如果不存在则记0。
# 然后把i的value值设为i-1与i+1的value值之和，并加1，相当于左右两串和i连接起来。同时置最左端和最右端的数的value值为i的value值。然后更新一次最大值。

l_map = {}  # 存储字典 列表元素:包含该元素的最长序列长度
l_max = 1
for i in l:
    if i not in l_map:
        # 确定左右连续串长度
        if i-1 not in l_map:
            i_left = 0
        else:
            i_left = l_map[i-1]
        if i+1 not in l_map:
            i_right = 0
        else:
            i_right = l_map[i+1]
        # 更新当前元素对应长度，左右都没就是1
        l_map[i] = i_left+i_right+1  
        # 更新左右
        if i_left:
            l_map[i-1] = l_map[i]
        if i_right:
            l_map[i+1] = l_map[i]
        # 更新最长子串长度
        l_max = max(l_max,l_map[i])
print(l_max)



