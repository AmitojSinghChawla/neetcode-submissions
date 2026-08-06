class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)
        product1 = 1
        product2 = 1   

        for i in range(len(nums)):
            prefix[i] = product1
            product1  = product1 * nums[i]

        for i in range(len(nums)-1,-1,-1):
            suffix[i] = product2
            product2  = product2 * nums[i]

        for i in range(len(nums)):
            res = prefix[i] * suffix[i]
            result[i] = res
        
        return result
