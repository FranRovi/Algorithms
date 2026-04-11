# Leet Code Algo 3242. Design Neighbor Sum Service.

class NeighborSum:

    def __init__(self, grid):
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid 
        

    def adjacentSum(self, value):
        temp = 0
        coord = [0,0]
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == value:
                    coord[0] = i
                    coord[1] = j
                    break
        if coord[0] - 1 >= 0:
            temp += self.grid[coord[0]-1][coord[1]]
        if coord[0] + 1 < self.rows:
            temp += self.grid[coord[0]+1][coord[1]]
        if coord[1] - 1 >= 0:
            temp += self.grid[coord[0]][coord[1]-1]
        if coord[1] + 1 < self.columns:
            temp += self.grid[coord[0]][coord[1]+1]
        return temp

        
    def diagonalSum(self, value):
        temp = 0
        coord = [0,0]
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == value:
                    coord[0] = i
                    coord[1] = j
                    break
        if coord[0] - 1 >= 0 and coord[1] - 1 >= 0:
            temp += self.grid[coord[0]-1][coord[1]-1]
        if coord[0] + 1 < self.rows and coord[1] + 1 < self.columns :
            temp += self.grid[coord[0]+1][coord[1]+1]
        if coord[0] - 1 >= 0 and coord[1] + 1 < self.columns :
            temp += self.grid[coord[0]-1][coord[1]+1]
        if coord[0] + 1 < self.rows and coord[1] - 1 >= 0:
            temp += self.grid[coord[0]+1][coord[1]-1]
        return temp