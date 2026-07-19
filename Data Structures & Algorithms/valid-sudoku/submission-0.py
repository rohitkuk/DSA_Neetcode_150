from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #creating hashsets
        rows  = defaultdict(set)
        cols  = defaultdict(set)
        boxes  = defaultdict(set)

        #traversing through the grid for nonempty cell
        for r in range(len(board[0])):
            for c in range(len(board[0])):
                value = board[r][c]
                if value != ".":
                    if (value in rows[r]) or (value in cols[c]) or (value in boxes[(r//3, c//3)]):
                        return False
                    else:
                        rows[r].add(value)
                        cols[c].add(value)
                        boxes[(r//3, c//3)].add(value)
                else:
                    continue
        return True
        

