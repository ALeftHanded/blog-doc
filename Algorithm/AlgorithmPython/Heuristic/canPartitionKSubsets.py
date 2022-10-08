# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 提示：
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内

class Solution:
	def __init__(self):
		self.count = 0
		self.cache = {0: []}
		self.val = 0
		self.deduplicate_cache = []

	def canPartitionKSubsets(self, nums, k):
		"""
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
		if k == 0:
			return nums == []
		if sum(nums) % k:
			return False
		val = sum(nums) // k
		deduplicate_cache = self.getAllSubArraySumCanEqualToValue(nums, val)
		self.__init__()
		if not deduplicate_cache:
			return False
		for tmp_solution in deduplicate_cache:
			for solution_num in tmp_solution:
				nums.remove(solution_num)
			if self.canPartitionKSubsets(nums, k - 1):
				return True
			else:
				nums.extend(tmp_solution)

		return False

	def ifSubArraySumCanEqualToValue(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: bool
		"""
		if val == 0:
			return True
		# Too large or small
		if sum(nums) < val or val < 0:
			return False
		for i in range(len(nums)):
			if self.ifSubArraySumCanEqualToValue(nums[:i] + nums[i + 1:], val - nums[i]):
				if sum(self.cache[self.count]) == self.val:
					self.count += 1
					self.cache[self.count] = [nums[i]]
				else:
					self.cache[self.count].append(nums[i])
				return True
		return False

	def getAllSubArraySumCanEqualToValue(self, nums, val):
		"""
        :type nums: List[int]
        :type val: int
        :rtype: List[List[int]]
        """
		self.val = val
		for i in range(len(nums)):
			if self.ifSubArraySumCanEqualToValue(nums[:i] + nums[i + 1:], val - nums[i]):
				self.cache[self.count].append(nums[i])
			else:
				self.cache[self.count] = []
				continue

		for v in self.cache.values():
			if v:
				v = sorted(v)
				if v not in self.deduplicate_cache:
					self.deduplicate_cache.append(v)

		return self.deduplicate_cache


if __name__ == "__main__":
	s = Solution()
	import random

	# # test for ifSubArraySumCanEqualToValue
	# for i in range(10000):
	# 	rand_val = random.randint(0, 100)
	# 	rand_nums = []
	# 	for j in range(random.randint(1, 50)):
	# 		rand_nums.append(random.randint(0, 60))
	# 	print(rand_nums, rand_val)
	# 	deduplicate_cache = s.getAllSubArraySumCanEqualToValue(rand_nums, rand_val)
	# 	print(deduplicate_cache)
	#
	# 	# judge
	# 	for l in deduplicate_cache:
	# 		if sum(l) != rand_val:
	# 			print("ERROR!")
	#
	# 	print("-------------------")
	#
	# 	s.__init__()
	# if s.getAllSubArraySumCanEqualToValue(rand_nums, rand_val):
	# 	if sum(s.cache) == rand_val:
	# 		print(s.cache, rand_val)
	# 	else:
	# 		print(s.cache, rand_val, "ERROR!")
	# else:
	# 	print("Failed")
	# 	print("-------------------")
	# 	print(s.cache, rand_nums, rand_val)
	# 	print("-------------------")
	# s.cache = {0: []}

	nums = [45, 26, 53, 7, 50, 15, 34, 34, 58, 8, 30, 3, 34, 30, 24, 58, 47, 28, 37, 17]
	k = 11
	s.canPartitionKSubsets(nums, k)

	for i in range(10000):
		rand_k = random.randint(1, 16)
		rand_nums = []
		for j in range(random.randint(1, 50)):
			rand_nums.append(random.randint(0, 60))
		print(rand_nums, rand_k)
		print(s.canPartitionKSubsets(rand_nums, rand_k))
		print("-------------------")
		s.__init__()
