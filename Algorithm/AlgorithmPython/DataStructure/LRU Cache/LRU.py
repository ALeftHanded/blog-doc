# LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# https://leetcode-cn.com/problems/lru-cache/
import collections


class LRUCacheV1:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.hashmap = {}

	def get(self, key: int) -> int:
		if self.hashmap.get(key, None) is None:
			return -1
		else:
			value = self.hashmap[key]
			self.hashmap.pop(key, None)
			self.hashmap[key] = value
			return value

	def put(self, key: int, value: int) -> None:
		if not self.hashmap:
			self.hashmap[key] = value
		else:
			if key in self.hashmap:
				self.hashmap[key] = value
				self.hashmap.pop(key, None)
				self.hashmap[key] = value
			else:
				self.hashmap[key] = value
				if len(self.hashmap) > self.capacity:
					lru_key = list(self.hashmap.keys())[0]
					self.hashmap.pop(lru_key, None)


class LRUCacheV2:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.hashmap = {}
		self.length = 0

	def get(self, key: int) -> int:
		if self.hashmap.get(key, None) is None:
			return -1
		else:
			value = self.hashmap[key]
			self.hashmap.pop(key, None)
			self.hashmap[key] = value
			return value

	def put(self, key: int, value: int) -> None:
		if not self.hashmap:
			self.hashmap[key] = value
			self.length = 1
		else:
			if self.hashmap.get(key, None) is not None:
				self.hashmap[key] = value
				self.hashmap.pop(key, None)
				self.hashmap[key] = value
			else:
				self.hashmap[key] = value
				self.length += 1
				if self.length > self.capacity:
					for k in self.hashmap:
						lru_key = k
						self.hashmap.pop(lru_key, None)
						self.length -= 1
						break


class LRUCache(collections.OrderedDict):
	def __init__(self, capacity: int):
		super().__init__()
		self.capacity = capacity

	def get(self, key: int) -> int:
		if key not in self:
			return -1
		self.move_to_end(key)
		return self[key]

	def put(self, key: int, value: int) -> None:
		if key in self:
			self.move_to_end(key)
		self[key] = value
		if len(self) > self.capacity:
			self.popitem(last=False)


if __name__ == '__main__':
	from time import process_time
	a = process_time()
	LRU_cache_test = LRUCache(2)
	for i in range(100000):
		LRU_cache_test.put(i, i)
		print(LRU_cache_test.get(i-1))
		print(LRU_cache_test.get(i+1))
		print(LRU_cache_test.get(i))
	print("Time:", process_time() - a)
