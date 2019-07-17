#动态规划  
#从右往左，看当前位置右边的那些所有最长递减子序列里的最大值有没有比当前位置小的  
#d[i]=max{d[k]| i<k<=n 且a[i]>a[k]} +1,边界i == n 的时候是1  
#无优化算法，O(n^2)  https://blog.csdn.net/stormbjm/article/details/8919484  
#优化算法，优化的是找剩下来的里面的那个过程,https://blog.csdn.net/weixin_41162823/article/details/81901569  
#对于序列A中的每个元素A[i]，我们都可以快速找到“小于A[i]的所有元素中F的值最大的那个”，二分，O(nlogn)  
#下面实现一个无优化的（没有完善，其实过程中应该找到所有满足条件的子序列）  

def  LDS(array):  
    n = len(array)  
    d = [1]*n  #存储包含当前元素的子序列长度  
    p = [-1]*n  #子序列下一个值的索引号，没有就是-1
    # 动态规划的核心
    for i in range(n-1,-1,-1):
        if i == n-1:
            d[i]=1
        else:
            # 另一边找到满足条件的数，然后更新
            mmax, mindex = search(array,d,i+1,len(array))
            d[i] = mmax+1
            p[i] = mindex
    # 
    max_len = max(d)
    # 最长的可能有几个
    max_start_list = []
    for j in range(len(d)):
        if d[j] == max_len:
            max_start_list.append(j)
    ans_all = []
    for max_start in max_start_list:
        ans = []
        i_next = max_start
        while p[i_next] != -1 :
            ans.append(array[i_next])
            i_next = p[i_next]
        ans.append(array[i_next])
        ans_all.append(ans)
    return ans_all
def search(array,d,start,end):  # 待完善，应该返回两个列表，如果满足条件的有多个
    mmax = 0
    mindex = -1
    for i in range(start,end):
        if array[i] < array[start-1]:
            if mmax < d[i]:
                mmax = d[i]
                mindex = i
    return mmax,mindex
