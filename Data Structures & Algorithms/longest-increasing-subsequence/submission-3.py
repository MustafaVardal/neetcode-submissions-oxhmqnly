class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_list = []
        
        for num in nums:
            left, right = 0, len(sub_list) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if sub_list[mid] < num:
                    left  = mid + 1
                else:
                    right = mid - 1
            
            if left == len(sub_list):
                sub_list.append(num)
            else:
                sub_list[left] = num
        return len(sub_list)