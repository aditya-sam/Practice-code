class Solution(object):
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = nums[0]
        sum = 0

        for i in range(len(nums)):
            sum = sum + nums[i]

            if sum > val:
                val = sum

            if sum < 0:
                sum = 0

        return val


print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
