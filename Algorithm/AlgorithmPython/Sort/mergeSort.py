def merge_sort(nums):
	if len(nums) <= 1:
		return nums
	mid_index = len(nums) >> 1
	return merge(merge_sort(nums[:mid_index]), merge_sort(nums[mid_index:]))


def merge(nums1, nums2):
	m, n, p1, p2 = len(nums1), len(nums2), 0, 0
	res = []
	while True:
		if p1 == m:
			res.extend(nums2[p2:])
			break
		if p2 == n:
			res.extend(nums1[p1:])
			break
		if nums1[p1] < nums2[p2]:
			res.append(nums1[p1])
			p1 += 1
		else:
			res.append(nums2[p2])
			p2 += 1

	return res


if __name__ == '__main__':
	import time

	# n1 = list(range(1, 100000, 2))
	# n2 = list(range(2, 100000, 2))
	import random

	num_length = random.randint(10, 100)
	test_nums = []
	for _ in range(num_length):
		test_nums.append(random.randint(-100, 100))

	if not merge_sort(test_nums) == sorted(test_nums):
		print(merge_sort(test_nums))
		print(sorted(test_nums))
	else:
		print("OK!")
