# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = []
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.path(root,p)
        q_path = self.path(root,q)
        p_root = root
        for i in range(min(len(p_path),len(q_path))):
            if p_path[i] == q_path[j]:
                p_root = p_path[i]
            else:
                break
        return p_root
        
        
    def path(self,start,end):
        if start == end:
            ans.append(start)
            return ans
        elif start.left or start.right:
            return []
        
        pathbool = self.path(start.left,end) + self.path(start.right,end)
        return ans
        
