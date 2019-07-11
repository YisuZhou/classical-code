# 深度优先搜索

def dfs(i,j,matrix, table, count):
    row = len(matrix)
    col = len(matrix[0])
    if i <0 or i >= row or j <0 or j>= col or !matrix[i][j] or table[i][j]:  # 注意终止条件
        return 0  
    ret = 1  # 记录这个连通域里有几个点
    table[i][j] = count #连通域计数值
    ret += dfs(i-1,j,matrix,table,count)
    ret += dfs(i+1,j,matrix,table,count)
    ret += dfs(i,j-1,matrix,table,count)
    ret += dfs(i,j+1,matrix,table,count)
    return ret
    
def liantongyu(matrix):
    row = len(matrix)
    col = len(matrix[0])
    table = []
    for i in range(row):
        table.append([0]*col)
    count = 1
    ret_list = []
    for r in range(row):
        for c in range(col):
            if matrix[i][j] and !table[i][j]:  # 不能忘了这个条件
                ret = dfs(r,c,matrix, table, count)
                ret_list.append(ret)
                count += 1
    return count-1
    
    
