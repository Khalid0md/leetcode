def findBestPath(n, m, startRow, startColumn, endRow, endColumn, monsterRow, monsterColumn):
    # Write your code here
    #return the closest distance to any monster along the path
    #traverse through the grid. 
    #try best to traverse away from monsters using row and col calculations
    #traverse right then down then left then up then through a monster
    #keep count of toReturn int
    maxmin = 0
    monsters = []
    for i in range(len(monsterRow)):
        monsters.append([monsterRow[i], monsterColumn[i]])
    print(monsters)
    #or 
    #do every possible path using dfs
    #each path has a hashset of visited
    #get the max min distance from every value in hashset to where the monsters are
    #going to test in my IDE
    def dfs(r, c):
        #base case - outside or at end 
        nonlocal maxmin
        if (r < 0 or r >= n-1 or c < 0 or c >= m or (r == endRow and c == endColumn)):
            return
        #process
        mindis = min([abs(r-monster[0]) + abs(c-monster[1]) for monster in monsters])
        maxmin = max(maxmin, mindis)
        
        #recurse
        if r+1 < n and (r+1, c) != (endRow, endColumn): dfs(r+1, c)
        if c+1 < m and (r, c+1) != (endRow, endColumn): dfs(r, c+1)
        if r-1 >= 0 and (r-1, c) != (endRow, endColumn): dfs(r-1, c)
        if c-1 >= 0 and (r, c-1) != (endRow, endColumn): dfs(r, c-1)
        return maxmin
    
    return dfs(startRow, startColumn)

#how to not hit recursion limit? learn bfs, other methods
#how to turn a half answer like this into an answer?

print(findBestPath(4, 4, 0, 0, 3, 3, [0, 1], [2, 3]))