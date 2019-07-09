# 非递归的快排，用栈来模拟递归，记录对应的左右索引号


def quick_sort(list_in):
    if 0 >= len(list_in)-1:  # 注意结束条件
        return
    stack = [0,len(list_in)-1]
    while stack:
        i_left = stack.pop(0) # 取出当前一对索引号
        i_right = stack.pop(0)
        if i_left >= i_right:  # 注意某一部分的结束条件
            continue
        i_mid = partition(list_in,i_left,i_right)
        stack = stack + [i_left,i_mid-1,i_mid+1,i_right] # 加上新一对索引号
    print(list_in)
    return 

def partition(list_in,i_left,i_right):
    base = list_in[i_right]
    i_next = i_left
    for i in range(i_left,i_right):
        if list_in[i] <= base:
            list_in[i],list_in[i_next] = list_in[i_next],list_in[i]
            i_next+=1
    list_in[i_right],list_in[i_next] = list_in[i_next],list_in[i_right]
    return i_next


l = [2,5,3,1,6,8,7]
quick_sort(l)
