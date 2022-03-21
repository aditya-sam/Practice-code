class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j+1] = nums[i+1]
                j += 1
        return j+1, nums


print(Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
