class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for freq, num in minHeap:
            res.append(num)
        return res