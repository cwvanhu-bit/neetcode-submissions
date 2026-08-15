class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x =  target - nums[i]
            if x in nums:
                if i != nums.index(x) and nums[i] + x == target: return sorted([nums.index(x), i])