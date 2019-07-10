# 前向遍历，递归版
def forward(root):
    if !root:
        return
    print(root.val)
    forward(root.left)
    forward(root.right)
    
# 前向遍历，非递归版
# 用栈保存每次的根节点
def forward(root):
    root_list = []
    if !root:
        return
    r_cur = root
    while root_list or r_cur:
        # 首先，一路向左并打印
        while r_cur:
            print(r_cur.val)
            root_list.append(r_cur)
            r_cur = r_cur.left
        # 这时候，根节点和左支都结束，以下处理右支。注意if条件
        if root_list:
            r_cur = root_list.pop()
            r_cur = r_cur.right
    
        
    
