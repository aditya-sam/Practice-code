class Solution(object):
    def isMonotonic(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) > 1:
            j, k = 0, 1
            try:
                while nums[j] == nums[k]:
                    j += 1
                    k += 1
                if nums[j] < nums[k]:
                    for i in range(0, len(nums)-1):
                        if nums[i] <= nums[i + 1]:
                            continue
                        else:
                            return False
                    return True
                else:
                    for i in range(0, len(nums)-1):
                        if nums[i] >= nums[i + 1]:
                            continue
                        else:
                            return False
                    return True
            except:
                return True
        else:
            return True


print(Solution.isMonotonic([1, 1, 2]))
