# Link: https://leetcode.com/problems/find-closest-number-to-zero/
# Start: 27 August 2024
# 

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]

        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]

        if closest in nums and (-1 * closest) in nums:
            if -1 * closest > closest:
                return (-1 * closest)
            elif -1 * closest < closest:
                return (closest)
            else:
                return closest
        else:
            return (closest)