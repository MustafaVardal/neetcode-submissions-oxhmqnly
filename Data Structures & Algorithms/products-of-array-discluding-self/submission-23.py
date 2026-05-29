class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)

        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if not i == j:
                    res *= nums[j]

            products[i]= (res)

        return products

            