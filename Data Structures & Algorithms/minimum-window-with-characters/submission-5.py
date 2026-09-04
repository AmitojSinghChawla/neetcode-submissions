class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        if t == "" :
            return ""

        dictt, window = {},{}

        for i in range(len(t)):
            dictt[t[i]] = 1 + dictt.get(t[i],0)
        
        have , need = 0, len(dictt)

        result, result_len = [-1,-1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in dictt and window[c] == dictt[c]:
                have +=1

            while have == need:
                if (r - l + 1) < result_len :
                    result = [l,r]
                    result_len = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in dictt and window[s[l]] < dictt[s[l]] :
                    have -=1

                l +=1

        l ,r = result

        return s[l : r + 1] if result_len != float("infinity") else ""

