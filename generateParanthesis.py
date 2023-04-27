class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #can:
        #add open if open < n
        #add closed if closed < open
        #stop when both == n

        res = []

        def backtrack(openN, closedN, stack):
            if openN == closedN == n:
                res.append("".join(stack))
                return #end this stack trace

            if openN < n:
                #stack.append('(') what's the difference betweeen appending then passing and passing with a +?
                backtrack(openN+1, closedN, stack + ['(']) #backtrack here right away! re-eval if we reached base case
                #stack.pop() #why? ##?go through all stack traces 1 by 1 and figure out how this resets the stack

            if closedN < openN:
                #stack.append(')') python lists are pass by reference, need to create new list when calling so that  every  recursive  call has it's own stack
                backtrack(openN, closedN+1, stack + [')'])
                #stack.pop() #why?

        backtrack(0, 0, [])
        return res

        #LC's solution of stack.pop() is faster because he is not creating multiple stacks but using the same stack and cleaning it up (stack.pop) all the way back as those stack traces get popped off the top to be empty and ready  for the next recursive function call

        #Time complexity:
        #Space complexity: