#给定一个未排序的整数数组（可能出现重复），找出最长连续序列的长度。要求算法的时间复杂度为 O(n)。

# 这个时间复杂度，肯定是不能先排序的了
# map有个很神奇的点，查找的时间复杂度是O（1），python中，list的in是O（n），但是dict的in是O（1）

# 那我们就可以一次遍历数组，每次更新左右的信息。对于数字i，找到i-1和i+1对应的value值,如果不存在则记0。
# 然后把i的value值设为i-1与i+1的value值之和，并加1，相当于左右两串和i连接起来。同时置最左端和最右端的数的value值为i的value值。然后更新一次最大值。

l_map = {}  # 存储字典 列表元素:包含该元素的最长序列长度
l_max = 1
for i in l:
    if i not in l_map:  # 避免重复元素影响
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

# 看到一种新解法，二进制用处很多。二进制下，在对应数字的位置置1，然后列表遍历结束后，会得到一个数。最后问题转变成，某个数的二进制下有几个连续的1
def solution(line):
    data = line.split(",")
    num = 0
    # 在对应的位置1
    for x in data:
        num = num|(1<<int(x)) 
    # 获取二进制字符串
    num = bin(num)[2:]  # bin()返回的是字符串，且开头是0b
    # 获得最大连续的1数量
    continuous = 0
    maxcontinuous = 0
    for x in num:
        if x == '0':
            if continuous > maxcontinuous:
                maxcontinuous = continuous
            continuous = 0
        else:
            continuous += 1
    return str(maxcontinuous)


