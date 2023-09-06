def longestPalindrome(self, s: str) -> str:
        length = len(s)
        grid = [[0]*length for i in range(length)]
        res = ""
        maxLen = 1

        #populate len = 1 and 2
        for i in range(length):
            grid[i][i] = 1
        
        for i in range(length-1):
            if s[i] == s[i+1]:
                grid[i][i+1] = 1
                maxLen = 2
                res = s[i:i+2]

        #implement pattern
        # check 0 - 2 and then 0 - 3 and so on
        for j in range(2, length):
            i = 0
            while i < j - 1:
                if grid[i+1][j-1] == 1 and s[i] == s[j]:
                    grid[i][j] = 1
                    if j - i + 1 > maxLen:
                         maxLen = j - i + 1
                         res = s[i:j+1]
                i += 1
             

        #iteration is wrong
                                         
        for li in grid:
             print(li)

        return [res, maxLen]

print(longestPalindrome(longestPalindrome, "cbbd"))