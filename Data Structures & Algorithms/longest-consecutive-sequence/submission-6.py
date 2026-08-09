class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        if not nums:
            return 0

        for i in nums:
            seen.add(i)

        longest = 0
        for i in seen:
            if i-1 not in seen:
                current = i
                length  = 1
                while current + 1 in seen:
                    length  = length  + 1
                    current = current + 1
                longest = max(longest, length)

        return longest
        