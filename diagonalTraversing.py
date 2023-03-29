class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if mat == None and len(mat) == 0:
            return []
        m = len(mat)
        n = len(mat[0])
        
        result = [0 for i in range(m*n)]
        
        row = 0
        col = 0
        index = 0
        Dir = 1
    #dir 1 indicates upward direction and dir -1 indicates downward direction
        while index < m*n:
            result[index] = mat[row][col]
            index += 1
            if Dir == 1:
                if col == n-1:
                    Dir = -1
                    row = row+1
                elif row == 0:
                    Dir = -1
                    col = col + 1
                else:
                    row = row - 1
                    col = col + 1
            else:
                if row == m-1:
                    Dir = 1
                    col = col+1
                elif col == 0:
                    Dir = 1
                    row = row+1
                else:
                    row = row + 1
                    col = col - 1
                
        return result
        
        
#time complexity --> O(m*n)
#space complexity ---> O(1)      