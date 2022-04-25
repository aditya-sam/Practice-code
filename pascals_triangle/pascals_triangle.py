class Solution(object):
    def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        for i in range(1, numRows+1):
            if i == 1:
                temp = [1]
                result.append(temp)
            elif i == 2:
                temp = [1, 1]
                result.append(temp)
            else:
                temp2 = []
                for j in range(i):
                    if j == 0:
                        temp2.append(1)
                    elif j == i-1:
                        temp2.append(1)
                    else:
                        temp2.append(temp[j-1]+temp[j])
                temp = temp2
                result.append(temp)
        return result


print(Solution.generate(5))
