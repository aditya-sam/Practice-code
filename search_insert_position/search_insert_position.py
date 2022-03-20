class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        size = len(nums)
        return find(nums, start, end, target, size)


def find(nums, start, end, target, size):
    if size <= 1:
        if nums[start] == target:
            return start
        elif nums[start] < target:
            return start + 1
        else:
            if start == 0:
                return start
            else:
                return start

    mid = (start + end)//2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        start = mid + 1
        size = end - start + 1
        return find(nums, start, end, target, size)
    else:
        end = mid - 1
        size = end - start + 1
        return find(nums, start, end, target, size)


print(Solution.searchInsert([1, 3, 5, 6], 7))
