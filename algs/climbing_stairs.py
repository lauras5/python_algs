def climbStairs(n):
  """
  :type n: int
  :rtype: int
  """
  a, b = 1, 2

  if n <= 2:
    return n

  for _ in range(3, n + 1):
    a, b = b, a + b
    # print(a, b)
  
  return b

print(climbStairs(3))   # 3
print(climbStairs(5))   # 8
print(climbStairs(7))   # 21
print(climbStairs(10))  # 89
