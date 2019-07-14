# 这段代码的核心是在二叉树中找到某个节点，并保存路径
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p_path = []
        q_path = []
        if not (self.path(root,p,p_path) and self.path(root,q,q_path)):
            return None          
        p_root = root
        for i in range(min(len(p_path),len(q_path))):
            if p_path[i] == q_path[i]:
                p_root = p_path[i]
            else:
                break
        return p_root
        
        
    def path(self,start,end,ans):
        if not start:
            return False  
        ans.append(start)
        if start == end:
            return True
        if self.path(start.left,end,ans):
            return True
        elif self.path(start.right,end,ans):
            return True
        else:
            ans.pop()  # 这一步一定不能忘
            return False
        
        
        
# 这段代码完全递归去找
class Solution:
    def lowestCommonAncestor(self, root, A, B):
        if(root is None or root==A or root==B):
            return root        #若root为空或者root为A或者root为B，说明找到了A和B其中一个
        left=self.lowestCommonAncestor(root.left,A,B)
        right=self.lowestCommonAncestor(root.right,A,B)
        if left  and right :
            return root      #若左子树找到了A，右子树找到了B，说明此时的root就是公共祖先
        if not left :    #若左子树是none右子树不是，说明右子树找到了A或B
            return right
        if not right :   #同理
            return left

        
        
