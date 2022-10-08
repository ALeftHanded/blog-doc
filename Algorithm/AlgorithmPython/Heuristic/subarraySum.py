# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
from typing import List
import random


class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		preSum = [sum(nums[:i+1]) for i in range(len(nums))]




if __name__ == "__main__":
	s = Solution()

	n = [1, 2, 3, 4, 5, 6]
	val = 7
	print(s.subarraySum(n, val))
