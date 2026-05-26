class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sexy ;P
        sexy = defaultdict(int)
        # i  and j will be unique!! 
        # this mean we do not need 2 for loop for it!

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if nums[i] in sexy:
                return [sexy[nums[i]], i] 
            
            sexy[diff] = i
            
            
      

            

        # nums[i] + nums[j] == target

        # nums[i] we can iterate it and we can find it diff with target 
        # if we find it with difference between target and nums[i]
        # it will be arithmatically target - nums[i] == nums[j]
        # then we need to check it this equation to the nums[j] vs diff 
        # But how? we are not automatically keeping nums[j] at that time
        # For that we can use nums if diff inside of the map then add then
        # we are going to diff location which is we will provide with hashmap
        # and we are goin to provide i
        # if not in the list we re going to add some portion of diff to nums[i] into map