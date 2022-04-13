class Solution(object):
    def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        power = len(digits) - 1
        num = 0
        res = []

        for i in range(len(digits)):
            num += digits[i] * (10**power)
            power -= 1
            if power < 0:
                break

        num += 1

        while num != 0:
            res = [num % 10] + res
            num = num // 10

        return res


print(Solution.plusOne([9]))
