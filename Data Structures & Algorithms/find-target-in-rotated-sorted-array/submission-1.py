class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        
        while l < r:

            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else :
                r = m
        
        pivot = l

        def binary_search(left:int, right:int) :
            l, r = left, right
            
            while l <= r:
                mid = (l+r)//2
                if target > nums[mid]:
                    l = mid + 1
                elif target == nums[mid]:
                    return mid
                else:
                    r = mid - 1
            
            return -1

        result = binary_search(0,pivot-1)

        if result!= -1:
            return result
        else:
            return binary_search(pivot,len(nums)-1)