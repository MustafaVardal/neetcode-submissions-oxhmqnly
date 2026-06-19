class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]: 
                r = m
            else:
                l = m + 1
        
        return nums[l]


""" [ 3, 4, 5, 6, 1, 2 ] ---> 
          l        m     r

          nums[r] =  2 , 1

          nums[l] = 3, 4, 5
          
          nums[m] = 6

          nums[m] > nums[l]:
          l = m + 1
          return l
          nums[m] < nums[r]:
          r -= 1
          return r """