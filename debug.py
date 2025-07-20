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
        while n > 1:
            for i in range(len(ans)):
                ans.append(ans[i] + "()")
                print("ans[-1]: ", print(ans[-1]))
                if not self.is_nested(ans[-1]):
                    print("here")
                    potential = "()" + ans[i]
                    try:
                        if ans.index(potential) == -1:
                            pass
                    except:
                        ans.append(potential)
                ans[i] = "(" + ans[i] + ")"
                print("ans: ", ans)
            n-=1
        return ans

s = Solution()
n = int(sys.argv[1])  # gets the first argument after the script name
print(s.generateParenthesis(n))

            
'''
if 1 retun () else return prev except for each one, (.), .+(), and if .+() was not sym, then ()+., too 


Your Output:

["(((())))","((()()))","((())())","(()(()))","(()()())","((()))()","()((()))","(()())()","()(()())","(())()()","()(())()","()(())()","()()(())","()()()()"]

Expected output:

["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

['(((())))', '((()()))', '((())())', '(()()())', '((()))()', '(()())()', '(())()()', '()()()()']

----

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
['((()))', '(()())', '(())()', '()()()']




'''
        