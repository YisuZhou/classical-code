def overlap(list1,list2):
    dict1 = {}
    for i in list1:
        dict1[i] = 1
    ans = []
    for ii in list2:
        if ii in dict1:
            ans.append(ii)
    return ans
        
