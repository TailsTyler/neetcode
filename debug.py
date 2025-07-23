import sys


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        '''open_n, closed_n: num of type of parens so far
        w: an element in the answer being worked on. eg if n == 2, '((' is an element being worked on that will become '(())' and then be added to the ans'''
        def tree(open_n, closed_n, w):
            if open_n == closed_n == n:
                ans.append(w)
                return
            elif open_n < n:
                w += '('
                tree(open_n + 1, closed_n, w)
                w = ''
            if closed_n < open_n:
                w += ')'
                tree(open_n, closed_n + 1, w)
                w = ''
        tree(0, 0, '')
        return ans

s = Solution()
n = int(sys.argv[1])  # gets the first argument after the script name, like  "python3 debug.py n"
print(s.generateParenthesis(n))

            
'''
if 1 return () else return prev except replace each one [.] with: (.), .(), and if .() was not sym, then ()+., too 


Your Output:

["(((())))","((()()))","((())())","(()(()))","(()()())","((()))()","()((()))","(()())()","()(()())","(())()()","()(())()","()()(())","()()()()"]

Expected output:

["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

----






'''
        
