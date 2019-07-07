# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        p = None
        n = None
        # 直接下面这样写就是判断null了
        while pHead:
            # 把head.next先保存起来
            n = pHead.next
            # 把head指向前面的
            pHead.next = p
            # 把p变成head，链表不断
            p = pHead
            # 继续遍历
            pHead = n
        return p
