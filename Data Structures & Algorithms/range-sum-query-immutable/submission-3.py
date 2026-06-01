class NumArray:

    def __init__(self, nums: List[int]):
        self.result = []
        total = 0 
        for num in nums:
            total += num
            self.result.append(total)


    def sumRange(self, left: int, right: int) -> int:
        preR = self.result[right]
        preL = self.result[left - 1] if left > 0 else 0
        return preR - preL
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)