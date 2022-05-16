class Solution(object):
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(nums)):
            if nums[i] >= max:
                max = nums[i]

        freq = [0 for i in range(max)]
        res, i = 0, 0

        while (i < len(nums)):
            freq[nums[i] - 1] += 1
            i += 1

        max = freq[0]
        for j in range(len(freq)):
            if freq[j] >= max:
                max = freq[j]
                res = j+1
        return res


print(Solution.majorityElement([3, 3, 4]))
