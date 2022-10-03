class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        empty = 2147483647
        gate = 0
        wall = -1
        q = []
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        m , n = len(rooms) , len(rooms[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    q.append([i,j])
                    
        while (q != []):
            point = q.pop(0)
            row , col = point[0] , point[1]
            for d in directions:
                r , c = row + d[0], col + d[1]
                if(r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != empty):
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append([r,c])
