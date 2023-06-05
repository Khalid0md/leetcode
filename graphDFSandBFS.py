# creating an adjacency list
from collections import deque


airports = 'PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM'.split(' ')

routes = [
    ['PHX', 'LAX'],
    ['PHX', 'JFK'],
    ['JFK', 'OKC'],
    ['JFK', 'HEL'],
    ['JFK', 'LOS'],
    ['MEX', 'LAX'],
    ['MEX', 'BKK'],
    ['MEX', 'LIM'],
    ['MEX', 'EZE'],
    ['LIM', 'BKK']
]

adjacencyList = {}

def addEdge(origin, destination):
    adjacencyList[origin].append(destination)
    adjacencyList[destination].append(origin)

#create graph
for airport in airports:
    adjacencyList[airport] = []

for route in routes:
    addEdge(route[0], route[1])

print(adjacencyList)

#BFS - iterative
#queue, initally has root, remove each element and add it's children if they exist,
#keep going until queue is empty
def bfs(start):
    queue = deque(start)

    visted = set()

    while(len(queue) > 0):
        print(queue)
        airport = queue.popleft()
        destinations = adjacencyList[airport]
        for destination in destinations:
            
            print(destination)
            if destination == "BKK":
                print("found it")
            
            if destination not in visted:
                visted.add(destination)
                queue.append(destination)
                
#dfs - recursive
#go deep into each node, then backtrack and follow same pattern
def dfs(start, setty):
    if start in setty:
        return
    setty.add(start)
    destinations = adjacencyList[start]

    for destination in destinations:
        if destination == "BKK":
            print("found it")
        if destination not in setty:
            dfs(destination, setty)

empset = set()
dfs("PHX", empset)
# bfs(["PHX"])