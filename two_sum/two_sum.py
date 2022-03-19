class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            diff = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] != diff:
                    continue
                return [i, j]


print(Solution.twoSum([-1, -2, -3, -4, -5], -8))
