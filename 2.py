# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n = 39):
        f0 = 0
        f1 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        # xrange带前不带后
        for i in xrange(2, n+1):
            a = f0 + f1
            f0 = f1
            f1 = a
        return a
