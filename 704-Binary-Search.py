class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
        while a<=b:
            p=(a+b)//2
            if nums[p]==target:
                return p
            elif nums[p]<target:
                a=p+1
            elif nums[p]>target:
                b=p-1
        return -1
        
