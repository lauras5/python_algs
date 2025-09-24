def minPathSum(self, grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  """
  num_rows, num_cols = len(grid), len(grid[0])
  dp = [0] * num_cols

  # first row
  dp[0] = grid[0][0]
  for j in range(1, num_cols):
    dp[j] = dp[j - 1] + grid[0][j]

  for i in range(1, num_rows):
    dp[0] += grid[i][0]
    for j in range(1, num_cols):
      dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
  return dp[-1]
