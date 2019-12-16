
from typing import List

class Solution:

    """
    1) Start in the leftmost column
    2) If all queens are placed
        return true
    3) Try all rows in the current column.  Do following for every tried row.
        a) If the queen can be placed safely in this row then mark this [row, 
            column] as part of the solution and recursively check if placing  
            queen here leads to a solution.
        b) If placing the queen in [row, column] leads to a solution then return 
            true.
        c) If placing queen doesn't lead to a solution then unmark this [row, 
            column] (Backtrack) and go to step (a) to try other rows.
    3) If all rows have been tried and nothing worked, return false to trigger 
        backtracking.
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        # fresh
        # place in the first row

        # List[List[str]]
        result=[]
 
        def placeQueen(board, rownum):

            for i in range(1,n+1):
                board[rownum]= '.'*(i-1)+'Q'+'.'*(n-i)
                # print(board)
                if self.isLegalBoard(board):
                    board1=[row for row in board]
                    if rownum==n-1:
                        result.append(board1)
                    else:
                        placeQueen(board1, rownum+1)
                board[rownum]='.'*n
        board=['.'*n for j in range(n)]
        # print(board)
        placeQueen(board, 0)

        return result

    
    def isLegalBoard(self, board):
        n=len(board)
        rows, cols,d1s, d2s=[],[],[],[]
        for row in range(n):
            for col in range(n):
                if board[row][col]=='Q':                        
                    # the serial no of the diagonals-- d1, d2
                    d1 = row + col #0,0 is on diagonal 0, (1,0),(0,1) is on diagonal 1, (2,0),(1,1), (0,2) are on diagonal 2 and so on.
                    d2 = row-col
                    if row in rows or col in cols or d1 in d1s or d2 in d2s:
                        return False 
                    else:
                        rows.append(row)
                        cols.append(col)
                        d1s.append(d1)
                        d2s.append(d2)
        return True


    
                

# b1=[[0,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,0]]
# b1=['.Q..','...Q','Q...','Q...']

s=Solution()
# print(s.isLegalBoard(b1))


inp=int(input())
results=s.solveNQueens(inp)



# for result in results:
#     for row in result:
#         print(row)
#     print("----")

print(len(results))
