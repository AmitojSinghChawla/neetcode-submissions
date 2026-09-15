class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:
            if arr[-1] < target:
                continue
            
            else:
                array = arr
                l = 0
                r = len(array) - 1

                while l<=r:
                    m = (l+r) //2
                    
                    if target == array[m]:
                        return True
                    elif target < array[m]:
                        r = m - 1
                    else:
                        l = m + 1
                
                else:
                    return False

        else:
            return False
                

                    
                