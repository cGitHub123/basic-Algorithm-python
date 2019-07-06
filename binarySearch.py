class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        # python求数组长度是len
        end = len(nums) - 1
        while start <= end:
            # / 返回浮点数，// 返回整数
            if nums[(start+end)//2] == target:
                return (start + end)//2
            if nums[(start+end)//2] > target:
                end = (start + end) // 2 - 1
            if nums[(start+end)//2] < target:
                start = (start + end) // 2 + 1
        return -1