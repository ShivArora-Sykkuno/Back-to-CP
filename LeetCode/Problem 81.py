class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while high >= low:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[low] == nums[high]:
                high -=1
                low +=1 
                continue

            if nums[mid] <= nums[high]:
                if nums[mid]<= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
            
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
        return False