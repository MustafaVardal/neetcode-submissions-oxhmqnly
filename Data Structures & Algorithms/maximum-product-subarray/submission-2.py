class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = res = nums[0]


        for num in nums[1:]:
            if num < 0:
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(num, num * maxProd)
            minProd = min(num, num * minProd)

            res = max(res, maxProd)
        return res
