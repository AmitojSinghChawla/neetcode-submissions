class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for sublist in board:
            seen=set()
            for item in sublist:
                if item == "." :
                    continue
                if item in seen:
                    return False
                seen.add(item)
        
        for c_value in range(9):
            seen = set()
            for r in range(9):
                item = board[r][c_value]
                if item == ".":
                    continue
                if item in seen:
                    return False
                seen.add(item)

        for br in range(3):              
            for bc in range(3):          
                seen = set()             
                for i in range(3):       
                    for j in range(3):
                        item = board[br*3 + i][bc*3 + j]
                        if item == "." :
                            continue
                        if item in seen:
                            return False
                        seen.add(item)

        return True

        