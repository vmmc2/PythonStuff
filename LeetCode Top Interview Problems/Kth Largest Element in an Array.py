import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Tem que usar uma minHeap para resolver o problema...
        li = []
        heapq.heapify(li) # convertendo li em uma minHeap
        for element in nums:
            heapq.heappush(li, element)
            if len(li) > k:
                heapq.heappop(li)
        return li[0]
