class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)

        l , r = 0, n - 1

        while l < r:
            area = max(area, (r - l) * min(heights[l], heights[r]))
            print(area, (r - l), (heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area