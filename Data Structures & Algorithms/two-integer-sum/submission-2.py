class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}

        for i,n in enumerate(nums):
            dictionary[n] = i

        for i,n in enumerate(nums):
            diff = target - n

            if diff in dictionary and dictionary[diff] !=i:

                return[i,dictionary[diff]]
        
        return []


                
        