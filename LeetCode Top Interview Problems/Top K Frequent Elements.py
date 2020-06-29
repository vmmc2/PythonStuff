class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        li = []
        heapq.heapify(li)
        for i in range(0, len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for (key, value) in d.items():
            heapq.heappush(li, (value, key))
        almost = heapq.nlargest(k, li)
        answer = []
        for element in almost:
            answer.append(element[1])
        return answer
