def matrix_mul(m_a,m_b):
    a_row = len(m_a)
    if a_row < 1:
        return None
    a_col = len(m_a[0])
    if a_col < 1:
        return None
    b_row = len(m_b)
    if b_row < 1:
        return None
    b_col = len(m_b[0])
    if b_col < 1:
        return None

    if a_col != b_row:
        return None

    ans = []
    for i in range(a_row):
        ans.append([0]*b_col)

    for r in range(a_row):
        for c in range(b_col):
            # 内积
            ele = 0
            for n in range(a_col):
                ele += m_a[r][n] * m_b[n][c]
            ans[r][c] = ele
    return ans

a = [[1,2,3,4],[2,3,4,5]]
b = [[1,0],[2,1],[2,3],[1,2]]
print(matrix_mul(a,b))

                
