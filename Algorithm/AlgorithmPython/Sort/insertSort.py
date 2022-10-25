def insert_sort(nums):
	for i in range(1, len(nums)):
		tmp, tmp_i = nums[i], i - 1
		while tmp < nums[tmp_i] and tmp_i >= 0:
			nums[tmp_i + 1] = nums[tmp_i]
			tmp_i -= 1
		nums[tmp_i+1] = tmp
	return nums


if __name__ == "__main__":
	import random

	num_length = random.randint(10, 100)
	test_nums = []

	for _ in range(num_length):
		test_nums.append(random.randint(-100, 100))

	if not insert_sort(test_nums) == sorted(test_nums):
		print(insert_sort(test_nums))
		print(sorted(test_nums))
	else:
		print("OK!")
