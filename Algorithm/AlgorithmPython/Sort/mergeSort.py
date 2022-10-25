def merge_sort(nums):
	mid_index = len(nums) >> 2
	return merge(merge_sort(nums[:mid_index]), merge_sort(nums[mid_index:]))


def merge(nums1, nums2):
	if not nums1 or not nums2:
		nums1.extend(nums2)
		return
	insert_index = 0
	while True:
		if not nums2:
			break
		num = nums2.pop(0)
		while insert_index < len(nums1) and num > nums1[insert_index]:
			insert_index += 1
		if insert_index == len(nums1):
			nums2 = [num] + nums2
			break
		nums1.insert(insert_index, num)
		insert_index += 1
	nums1.extend(nums2)
	return


def merge_v1(l1, l2):
	m, n, p1, p2 = len(l1), len(l2), 0, 0
	res = []
	while True:
		if p1 == m:
			res.extend(l2[p2:])
			break
		if p2 == n:
			res.extend(l1[p1:])
			break
		if l1[p1] < l2[p2]:
			res.append(l1[p1])
			p1 += 1
		else:
			res.append(l2[p2])
			p2 += 1

	l1[:] = res


if __name__ == '__main__':
	import time

	# n1 = list(range(1, 100000, 2))
	# n2 = list(range(2, 100000, 2))
	n1 = [2]
	n2 = [1]
	start_time = time.time()
	merge_v1(n1, n2)
	print(n1)
	print(time.time() - start_time)
