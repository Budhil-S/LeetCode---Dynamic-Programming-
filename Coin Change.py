class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 ] * (amount + 1)
        dp[0] = 0
        for am in range(1,amount+1):
            for coin in coins:
                if am - coin >= 0:
                    dp[am] = min(dp[am],1 + dp[am -coin])
        if dp[amount] != amount + 1: #dp not equal to default value
            return dp[amount]
        else:
            return -1