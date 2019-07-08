def partition(list_in,i_left,i_right):
    base = list_in[i_right]
    i_next = i_left
    for ii in range(i_left,i_right):
        if list_in[ii] <= base:
            list_in[i_next], list_in[ii] = list_in[ii], list_in[i_next]
            i_next += 1
    list_in[i_next], list_in[i_right] = list_in[i_right], list_in[i_next]

    return i_next
    
def quick_sort(list_in,i_left,i_right,k):
    if k < 0:
        return None
    elif k > len(list_in) :
        return None
    i_mid = partition(list_in,i_left,i_right)

    if i_mid == k:
        print list_in[i_mid]
    elif i_mid > k:
        quick_sort(list_in,i_left,i_mid-1,k)
    else:
        quick_sort(list_in,i_mid+1,i_right,k)
        
 if __name__ == '__main__':
     ll = [1,4,7,2,8,5]
     i_left = 0
     i_right = len(ll)-1
     k = 3
     quick_sort(ll,i_left,i_right,k)
