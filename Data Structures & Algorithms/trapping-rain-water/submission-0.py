class Solution:
    def trap(self, height: List[int]) -> int:

        max_left, max_right = [0]*len(height), [0]*len(height)

        current = 0
        for i in range(len(height)):
            current = max(current,height[i])
            max_left[i] = current

        current2=0
        for i in range(len(height)-1,-1,-1):
            current2 = max(current2,height[i])
            max_right[i] = current2

        total = 0
        for i in range(len(height)):
            trapped_water = min(max_left[i],max_right[i]) - height[i]
            if trapped_water <=0:
                continue
            total = total + trapped_water

        return total
            
            

        
        