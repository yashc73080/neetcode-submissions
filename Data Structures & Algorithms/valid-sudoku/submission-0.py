from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                current = int(board[i][j]) if board[i][j] != '.' else 0

                if current == 0:
                    continue

                # Check number
                if current < 1 or current > 9:
                    return False

                # Check rows
                if current in rows[i]:
                    return False
                else:
                    rows[i].add(current)
                
                # Check columns
                if current in cols[j]:
                    return False
                else:
                    cols[j].add(current)

                # Check box
                row_index = i // 3
                col_index = j // 3
                if current in boxes[(row_index, col_index)]:
                    return False
                else:
                    boxes[(row_index, col_index)].add(current)

        return True