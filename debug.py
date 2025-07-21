import sys


class Solution:
    def is_nested(self, s):
        print("checking if nested: ", s)
        while len(s) > 0:
            if s[0:2] == '()':
                s = s[2:]
                print("left to check: ", s)
            else:
                return False
        return True
    def generateParenthesis(self, n: int) -> list[str]:
        ans = ['()']
        while n > 1: #grow the set one by one, starting with n=1
            for i in range(len(ans)): #consider each potential growth for each element
                potential = ans[i] + "()"
                if ans[-1] != potential:
                    ans.append(potential)
                print("ans[-1]: ", print(ans[-1]))
                if not self.is_nested(ans[-1]):
                    print("ans[-1] is not nested." )
                    potential = "()" + ans[i]
                    print("considering adding ", potential)
                    try:
                        if ans.index(potential) == -1:
                            print("ans.index(potential): ", ans.index(potential))
                            print("so won't add it")
                            pass
                    except:
                        print("so added it")
                        ans.append(potential)
                ans[i] = "(" + ans[i] + ")"
                print( ans)
            n-=1
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
        
