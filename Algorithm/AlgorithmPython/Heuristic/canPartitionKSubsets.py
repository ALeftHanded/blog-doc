# 给定一个整数数组 test_nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 提示：
# 1 <= k <= len(test_nums) <= 16
# 0 < test_nums[i] < 10000
# 每个元素的频率在 [1,4] 范围内

class Solution:
	def canPartitionKSubsets(self, nums, k):
		"""
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """



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
