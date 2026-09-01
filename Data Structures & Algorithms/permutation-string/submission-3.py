class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dictt1, dictt2 = {}, {}

        ls1 = len(s1)
        l = 0

        if len(s2) < len(s1) :
            return False

        for i in range(len(s1)):
            dictt1[s1[i]] = 1 + dictt1.get(s1[i],0)

        for r in range(len(s2)):
            dictt2[s2[r]] = 1 + dictt2.get(s2[r],0)

            if r >= len(s1):
                dictt2[s2[l]] -= 1
                if dictt2[s2[l]] == 0:
                    del dictt2[s2[l]]
                l +=1

            if dictt1 == dictt2:
                return True
                

        return False
                
            




        