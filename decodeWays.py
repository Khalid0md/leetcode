def numDecodings(self, s: str) -> int:
        #recursion and memoization decision tree
        if not s: return 0
        def take(w):
            if len(w) < 1:
                return 1
            if w[0:1] == "0":
                return 0
            if int(w[0:2]) < 27:
                first = take(w[1:])
                second = take(w[2:])
                return first + second
            else:
                 return take(w[1:])
        count = take(s)
        return count
    
print(numDecodings(numDecodings, "12"))