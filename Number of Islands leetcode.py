class Solution:
 
    def markAllOnesInThisIsland(self, grid, row, col, totalRows, totalCols):
        Q = [[row, col]]
        grid[row][col] = "0"
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
 
        while Q:
            curr = Q.pop(0)
 
            for index in range(4):
                newRow = curr[0] + dx[index]
                newCol = curr[1] + dy[index]
                if newRow < 0 or newCol < 0 or newRow >= totalRows or newCol >= totalCols or grid[newRow][newCol] == "0":
                    continue 
                grid[newRow][newCol] = "0"
                Q.append([newRow, newCol])
 
 
    def numIslands(self, grid: List[List[str]]) -> int:
        totalRows = len(grid)
        totalCols = len(grid[0])
        totalIslands = 0 
 
        for row in range(totalRows):
            for col in range(totalCols):
                if grid[row][col] == "1":
                    self.markAllOnesInThisIsland(grid, row, col, totalRows, totalCols)
                    totalIslands += 1
 
        return totalIslands