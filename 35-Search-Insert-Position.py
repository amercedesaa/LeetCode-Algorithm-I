class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1
        
        while a <= b:
            m = (a + b) // 2
            
            if nums[m] == target:
                return m
            elif target > nums[m]:
                a = m + 1
            else:
                b = m - 1
        
        return a
