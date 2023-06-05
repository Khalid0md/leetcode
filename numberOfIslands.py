class Solution:
   
    def numIslands(self, grid) -> int:
        #check all recursively
        #for a given block, check all adjacent cells, if they are all 0's, or the edge, then your starting block is an island, if it's a 1, then check it
        if not grid:
            return 0
        islands = 0

        def dfs(m, n):
            #if island has ended either with a 0 for water or one of the edges,
            if (m < 0 or n < 0 or m == len(grid) or n == len(grid[0]) or grid[m][n] == "0"):
                return 
            #else process
            grid[m][n] = "0"

            #call dfs
            dfs(m + 1, n)
            dfs(m - 1, n)
            dfs(m, n + 1)
            dfs(m, n - 1)
            return
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    print("islands incremented")
                    dfs(m, n)
                    islands += 1
        
        return islands
    
    print(numIslands(numIslands, [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))