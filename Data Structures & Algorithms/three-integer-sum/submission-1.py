class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # skip duplicate fixed numbers (only from the 2nd element on)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicate pointer values after a match
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return result