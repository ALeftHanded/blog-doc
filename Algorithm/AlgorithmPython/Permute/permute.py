# 给定一个不含重复数字的数组 test_nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

# 1 <= test_nums.length <= 6
# -10 <= test_nums[i] <= 10
# test_nums 中的所有整数 互不相同

import unittest

from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		"""
        :param nums:
        :return:
        """
		res = []
		return res


if __name__ == '__main__':
	solution = Solution()

	nums = [1, 2, 3, 4, 5, 6]

	res = solution.permute(nums)
	print(res)
