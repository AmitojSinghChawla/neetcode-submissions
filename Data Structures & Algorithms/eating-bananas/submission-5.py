class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # result = max(piles)
        # while speed < max(piles):
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)

        #     if totalTime <= h:
        #         result = min(result,speed)
        #     speed += 1
        # return result

        l,r = 1 , max(piles)
        result = r

        while l<=r :
            mid = (l+r) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p)/mid)

            if time <= h:
                r = mid - 1
                result = min(result,mid)

            else:
                l = mid + 1

        return result


                

 

