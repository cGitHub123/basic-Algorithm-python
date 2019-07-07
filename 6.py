# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        t = None
        if pHead2 == None:
            return pHead1
        if pHead1 == None:
            return pHead2
        if pHead1.val <= pHead2.val:
            t = pHead1
            t.next = self.Merge(pHead1.next, pHead2)
        if pHead1.val > pHead2.val:
            t = pHead2
            t.next = self.Merge(pHead1,pHead2.next)
        return t