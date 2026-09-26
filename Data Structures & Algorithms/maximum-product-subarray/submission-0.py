class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_prod, max_prod = 1, nums[0]

        for n in nums:
            if cur_prod < 0:
                cur_prod = 1
            
            cur_prod *= n
            max_prod = max(max_prod, cur_prod)
        return max_prod