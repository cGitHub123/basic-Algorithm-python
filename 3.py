# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if (number <= 0):
            return 0
        if (number == 1):
            return 1
        if (number == 2):
            return 2
        third = 0
        first = 1
        second = 2
        for i in xrange(3,number + 1):
            third = first + second
            first = second
            second = third
        return third