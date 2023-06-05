from typing import (
    List,
)
from collections import deque

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

def walls_and_gates(rooms):
    #-1 wall
    #0 gate
    #INF empty room
    #holy... BFS with visited set, starting from the gates, that's smart
    #need to BFS from both gates at the same time
    #BFS from gates, then from 1's, then from 2's... etc
    ROWS, COLS = len(rooms), len(rooms[0])
    visited = set()
    q = deque()

    def bfs(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or rooms[r][c] == -1:
            return
        visited.add((r, c))
        q.append([r,c])
        

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append([r, c])
                visited.add((r,c))
            
    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            rooms[r][c] = dist
            bfs(r + 1, c)
            bfs(r - 1, c)
            bfs(r, c + 1)
            bfs(r, c - 1)
        dist +=1

    
