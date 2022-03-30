class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i]/val != 1:
                nums[count] = nums[i]
                count += 1
        return count


print(Solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
