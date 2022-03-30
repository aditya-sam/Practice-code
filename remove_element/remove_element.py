class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            count = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[count] = nums[i]
                    count += 1
            return count


print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
