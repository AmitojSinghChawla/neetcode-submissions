class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1 + nums2

        nums3.sort()

        l, r = 0 , len(nums3) - 1
        
        if len(nums3) % 2 == 0:
            mid = (l+r) // 2            
            return (nums3[mid] + nums3[mid+1])/2
        else:
            return nums3[(l+r)//2]
            