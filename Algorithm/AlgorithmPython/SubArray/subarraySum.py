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
		res = 0
		preSum = 0
		left_exist_dic = {0: 1}

		for i in nums:
			preSum += i
			if preSum - k in left_exist_dic:
				res += left_exist_dic.get(preSum - k, 0)
			if preSum in left_exist_dic:
				left_exist_dic[preSum] += 1
			else:
				left_exist_dic[preSum] = 1

		return res


if __name__ == "__main__":
	s = Solution()

	n = [1, 2, 3, 4, 5, 6]
	val = 7
	print(s.subarraySum(n, val))
