class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i
            
