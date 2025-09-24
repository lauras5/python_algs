"""
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
"""

def change(amount, coins):
  """
  :type amount: int
  :type coins: List[int]
  :rtype: int
  """
  dp = [0] * (amount + 1)
  dp[0] = 1

  for coin in coins:
      for x in range(coin, amount + 1):
          dp[x] += dp[x - coin]
          
  return dp[amount]