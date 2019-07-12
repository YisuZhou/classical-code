# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# 两种方式，循环或者递归

# 循环
class Solution:
    def Clone(self, pHead):
        # 先把所有节点构造好，记录好新旧节点的对应关系
        # 然后再把next和random的连接线连起来
        if pHead is None:
            return None
        #1.建立原节点与复制节点间的map映射
        map_dict={}
        p=pHead
        # 保留复制表头指针，以便返回
        q=newHead=RandomListNode(p.label)
        map_dict[p]=q # 建立对应关系，旧的：新的
        p=p.next
        while p:
            q=RandomListNode(p.label)
            map_dict[p]=q
            p=p.next
        #2.复制next指针与random指针
        p=pHead
        while p:
            if p.next:
                map_dict[p].next=map_dict[p.next]  # 连接好next
            if p.random:
                map_dict[p].random=map_dict[p.random]  # 连接好random
            p=p.next
        return newHead
        
        
# 递归
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return pHead
        p=RandomListNode(pHead.label)
        p.next=pHead.next
        p.random=pHead.random
        p.next=self.Clone(pHead.next)
        return p
