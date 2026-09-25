class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            heapq.heappush(minHeap, (num, freq))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for num, freq in minHeap:
            res.append(num)
        return res