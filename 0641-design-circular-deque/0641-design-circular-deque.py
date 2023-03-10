class MyCircularDeque:
	from collections import Counter

	def __init__(self, k: int):
		self.q = deque()
		self.length = 0
		self.max_ = k



	def insertFront(self, value: int) -> bool:
		if (self.length < self.max_):
			self.q.appendleft(value)
			self.length += 1
			return True

		else:
			return False

	def insertLast(self, value: int) -> bool:
		if (self.length < self.max_):
			self.q.append(value)
			self.length += 1
			return True
		else:
			return False


	def deleteFront(self) -> bool:
		if (self.length > 0):
			self.q.popleft()
			self.length -= 1
			return True

		else:
			return False


	def deleteLast(self) -> bool:
		if (self.length > 0):
			self.q.pop()
			self.length -= 1
			return True
		else:
			return False


	def getFront(self) -> int:
		if self.length > 0:
			return self.q[0]

		else:
			return -1

	def getRear(self) -> int:
		if self.length > 0:
			return self.q[-1]

		else:
			return -1


	def isEmpty(self) -> bool:
		return self.length == 0


	def isFull(self) -> bool:
		return self.length == self.max_




# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()