# example of merge sort in Python
# merge function take two intervals
# one from start to mid
# second from mid+1, to end
# and merge them in sorted order
def merge(Arr, start, mid, end):

    # create a temp array
    temp = [0] * (end - start + 1)

    # crawlers for both intervals and for temp
    i, j, k = start, mid+1, 0

    # traverse both lists and in each iteration add smaller of both elements in temp
    while(i <= mid and j <= end):
        if(Arr[i] <= Arr[j]):
            temp[k] = Arr[i]
            k += 1
            i += 1
        else:
            temp[k] = Arr[j]
            k += 1
            j += 1

    # add elements left in the first interval
    while(i <= mid):
        temp[k] = Arr[i]
        k += 1
        i += 1

    # add elements left in the second interval
    while(j <= end):
        temp[k] = Arr[j]
        k += 1
        j += 1

    # copy temp to original interval
    for i in range(start, end+1):
        Arr[i] = temp[i - start]


# Arr is an array of integer type
# start and end are the starting and ending index of current interval of Arr

def mergeSort(Arr, start, end):

    if(start < end):
        mid = (start + end) // 2
        mergeSort(Arr, start, mid)
        mergeSort(Arr, mid+1, end)
        merge(Arr, start, mid, end)

    return Arr


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = mergeSort(nums, 0, len(nums)-1)
        target_arr = []

        for i in range(0, len(sorted_nums)):
            if sorted_nums[i] == target:
                target_arr.append(i)

        return target_arr
