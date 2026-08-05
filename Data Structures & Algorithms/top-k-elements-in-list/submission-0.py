class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1

        arr =[]
        for key,value in frequency_dict.items():
            arr.append([value,key])

        arr.sort()

        result =[]

        while len(result) < k:
            result.append(arr.pop()[1])

        return result
        