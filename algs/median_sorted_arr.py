def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    a, b = nums1, nums2
    # binary search on smaller number
    if len(a) > len(b): a, b = b, a
    m, n = len(a), len(b)
    
    lo, hi, half = 0, m, (m + n + 1) // 2
    INF = float('inf')

    while True:
      i = (lo + hi) // 2
      j = half - i

      # values around the partition
      aL = a[i - 1] if i > 0 else -INF    # max of left, a
      aR = a[i] if i < m else INF         # max of right, a
      bL = b[j - 1] if j > 0 else -INF    # max of left, b
      bR = b[j] if j < n else INF         # max of right, b

      # check partition
      if aL <= bR and bL <= aR:
        if (m + n) % 2:
          return float(max(aL, bL))
        return (max(aL, bL) + min(aR, bR)) / 2.0

      # if aL is too big, move cut left
      if aL > bR:
        hi = i - 1
      # if bL is too big more right
      else:
        lo = i  + 1
