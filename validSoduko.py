class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use a hashmap col  -> set for every row, every column
        #use a hashmap for each block
        #index rows and columns as blocks
        #Hashmap (bi, bj) -> HashSet
        #0 1 2
        #1
        #2
#take actual index and divide it by 3 (round down) to get block  index
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        blocks = collections.defaultdict(set) #key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in blocks[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                blocks[(r//3,c//3)].add(board[r][c])
        
        return True

        #can i optimize further by using a hasDuplicates or isUnique
        #or some other way of finding out if there are dupes? to avoid
        #the O(n^2)
		
				
        #Time complexity: O(n^2) where n is size of array
        #Space complexity: O(n^2) worst case if we store every square