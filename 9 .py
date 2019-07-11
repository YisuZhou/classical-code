# 中序遍历，递归版
def mid(root):
    if !root:
        return
    mid(root.left)
    print(root.val)
    mid(root.right)
   
  
# 中序遍历，非递归版。和前序非递归一样，用栈储存每个父节点
def mid(root):
    if !root:
        return
    root_list = []
    cur_r = root
    
    while cur_r or root_list:
        while cur_r:
            root_list.append(cur_r)
            cur_r = cur_r.left
        # 以上就把所有的左支存下来了
        
        if root_list:  # 下面有pop，记得要这个if条件
            cur_r = root_list.pop()
            print(cur_r.val)
            # 以上就把左和根打出来了
            cur_r = cur_r.right

