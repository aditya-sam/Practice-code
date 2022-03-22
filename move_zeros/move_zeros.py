
def swap(i, j, nums):
    temp = nums[j]
    nums[j] = nums[i]
    nums[i] = temp


class Solution(object):
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
                j = i+1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i >= len(nums) or j >= len(nums):
                break
            swap(i, j, nums)
        return nums


print(Solution.moveZeroes([0, 1, 0, 3, 12]))
