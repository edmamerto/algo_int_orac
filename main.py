# Problem Statement #
# Design a class to calculate the median of a number stream. The class
# should have the following two methods:

# 1. insertNum(int num):
#	- stores the number in the class
# 2. findMedian():
#	- returns the median of all numbers inserted in the class

# If the count of numbers inserted in the class is even, the median will
# be the average of the middle two numbers.

# Example 1:

# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
# 7. findMedian() -> output: 3.5

from heapq import *

class NumberStream:

	def __init__(self):
		self.maxHeap = []
		self.minHeap = []


	def insertNum(self, num):
		if not self.maxHeap:
			heappush(self.maxHeap, -num)
		elif not self.minHeap:
			heappush(self.minHeap, num)
		else:
			if num > -self.maxHeap[0]:
				heappush(self.minHeap, num)
			else:
				heappush(self.maxHeap, -num)
			total_length = len(maxHeap) + len(self.minHeap)
			if (total_length % 2) != 0:
				heappush(self.maxHeap, -heappop(self.minHeap))

a = NumberStream()
a.insertNum(3)
a.insertNum(1)
