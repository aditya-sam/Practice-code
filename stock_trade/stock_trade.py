class Solution(object):
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] > prices[i]:
                continue
            else:
                for j in range(i, len(prices)):
                    if prices[j] - prices[i-1] > max_profit:
                        max_profit = prices[j] - prices[i-1]

        return max_profit


print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
