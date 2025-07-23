import sys


s = Solution()
n = int(sys.argv[1])  # gets the first argument after the script name, like  "python3 debug.py n"
print(s.generateParenthesis(n))

            
'''
old plan that did not work bc could not generate "(())(())":
if 1 return () else return prev except replace each one [.] with: (.), .(), and if .() was not sym, then ()+., too 

'''
        
