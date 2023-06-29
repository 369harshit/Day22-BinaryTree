import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Test case
kth_largest = KthLargest(3, [4, 5, 8, 2])
output = [None]
output.append(kth_largest.add(3))
output.append(kth_largest.add(5))
output.append(kth_largest.add(10))
output.append(kth_largest.add(9))
output.append(kth_largest.add(4))
print(output)
