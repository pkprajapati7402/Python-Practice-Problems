class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        freshOranges = 0 
        Q = []
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    freshOranges += 1 
                elif grid[row][col] == 2:
                    Q.append([row, col, 0])
 
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        result = 0
 
        while Q:
            curr = Q.pop(0)
            result = max(result, curr[2])
 
            for index in range(4):
                newRow = curr[0] + dx[index]
                newCol = curr[1] + dy[index] 
                if newRow < 0 or newCol < 0 or newRow >= m or newCol >= n or grid[newRow][newCol] == 2 or grid[newRow][newCol] == 0:
                    continue 
                grid[newRow][newCol] = 2 
                freshOranges -= 1
                Q.append([newRow, newCol, curr[2] + 1])
 
        if freshOranges > 0:
            return -1 
        return result