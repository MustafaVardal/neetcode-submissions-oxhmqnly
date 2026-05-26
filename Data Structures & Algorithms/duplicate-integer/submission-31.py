class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uni= set()

        for i in range(len(nums)):
            if  nums[i] in uni:
                return True
            else:
                uni.add(nums[i])
        return False
        #return False

        
        #  nums = [ 1, 2, 3, 4]
        # set(1,2,3,4)
        # then we can compare with real numbers.

        # if nums[i] in set:
        # return False
        # else:
        #   set.add(nums[i])
        return True