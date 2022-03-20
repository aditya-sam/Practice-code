def merge(arr, start, mid, end):
    temp = [0]*(end - start+1)
    i, j, k = start, mid+1, 0

    while(i <= mid and j <= end):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(start, end+1):
        arr[i] = temp[i-start]


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)

    return arr


class Solution(object):
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        sort_nums = mergeSort(nums, 0, len(nums)-1)

        for i in range(0, len(sort_nums), 2):
            if i == len(nums)-1:
                return sort_nums[i]
            elif sort_nums[i] == sort_nums[i+1]:
                continue
            else:
                return sort_nums[i]


print(Solution.singleNumber([2, 2, 1]))
print(Solution.singleNumber([4, 1, 2, 1, 2]))
print(Solution.singleNumber([1]))
