class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1 , max(piles)
        result = r

        while l <= r:
            mid = (l+r) // 2
            speed = mid
            time = 0 

            for p in piles:
                time += math.ceil(float(p)/speed)

            if time <= h:
                result = min(result, speed)
                r = mid - 1

            else:
                l = mid + 1
        
        return result

 

