class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, x in enumerate(nums):
            if target-x in index:
                return [index[target-x], i]
            index[x] = i
  
