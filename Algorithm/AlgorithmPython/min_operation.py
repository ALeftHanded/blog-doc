"""
https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid/
给你一个大小为m x n 的二维整数网格 grid_test 和一个整数 x 。每一次操作，你可以对 grid_test 中的任一元素 加 x 或 减 x 。

单值网格 是全部元素都相等的网格。

返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 -1 。

m == grid_test.length
n == grid_test[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid_test[i][j] <= 104
"""


def minOperations_test(grid, x):
	arr = []
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			arr.append(grid[i][j])
	arr = sorted(arr)
	print("arr", arr)

	diff_for_test = [(arr[i] - arr[0]) % x for i in range(len(arr))]
	print("diff_for_test", diff_for_test)
	if sum(diff_for_test) > 0:
		return -1
	res_arr = []
	for k in range(len(arr)):
		diff = [abs((arr[i] - arr[k]) // x) for i in range(len(arr))]
		print("diff", diff, sum(diff))
		res_arr.append(sum(diff))

	return min(res_arr)


def minOperations_v1(grid, x):
	arr = []
	m, n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			arr.append(grid[i][j])
	arr = sorted(arr)
	diff_for_test = [(arr[i] - arr[0]) % x for i in range(len(arr))]
	if sum(diff_for_test) > 0:
		return -1
	return sum([abs((arr[i] - arr[len(arr)//2]) // x) for i in range(len(arr))])


def minOperations_v2(grid, x):
	arr, m, n = [], len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			arr.append(grid[i][j])
	arr = sorted(arr)
	for i in range(len(arr)):
		if (arr[i] - arr[0]) % x:
			return -1
	return sum([abs((arr[i] - arr[len(arr) // 2])) for i in range(len(arr))]) // x


if __name__ == "__main__":
	grid_test = [list(range(2, 200100, 5))]
	x_test = 5

	from time import process_time

	start_time = process_time()
	ans = minOperations_v1(grid_test, x_test)
	during = process_time() - start_time
	print("----- v1 -----")
	print(ans, during)

	start_time = process_time()
	ans = minOperations_v2(grid_test, x)
	during = process_time() - start_time
	print("----- v2 -----")
	print(ans, during)
