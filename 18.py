def num3sum(array,tsum):
    ans = []
    for i_left in range(len(array)-2):
        i_mid = i_left + 1
        i_right = len(array) - 1
        while i_mid < i_right:
            if array[i_left] + array[i_mid] + array[i_right] == tsum:
                ans.append([array[i_left],array[i_mid],array[i_right]])
                i_mid += 1
                i_right -= 1
            elif array[i_left] + array[i_mid] + array[i_right] > tsum:
                i_right -= 1
            else:
                i_mid += 1
        return ans
       
       
# 变体，三数之和最接近tsum的
def num3sum2(array,tsum):
    gap_min = 10000
    for i_left in range(len(array)-2):
        i_mid = i_left + 1
        i_right = len(array) - 1
        while i_mid < i_right:
            if array[i_left] + array[i_mid] + array[i_right] == tsum:
                return [array[i_left],array[i_mid],array[i_right]]
            elif array[i_left] + array[i_mid] + array[i_right] > tsum:
                if array[i_left] + array[i_mid] + array[i_right] - tsum < gap_min:
                    gap_min = array[i_left] + array[i_mid] + array[i_right] -tsum
                    ans = [array[i_left], array[i_mid], array[i_right]]
                i_right -= 1
            else:
                if tsum - (array[i_left] + array[i_mid] + array[i_right]) < gap_min:
                    gap_min = tsum - (array[i_left] + array[i_mid] + array[i_right])
                    ans = [array[i_left], array[i_mid], array[i_right]]
                i_mid += 1
        return ans
