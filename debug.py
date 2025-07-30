#this is a temporary place to put code while debugging it

import sys
import unittest




s = Solution()
n = [1,2,3,4]  # gets the first argument after the script name, like  "python3 debug.py n"
print(s.dailyTemperatures(n))

# if __name__ == "__main__":
#     unittest.main()

            
'''
Input:

temperatures=

stdout:

[30, 38, 30, 36, 35, 40, 28]
[0, 0, 0, 0, 0, 0, 0]
high:  30
ans[i - 1] = 1:  [1, 0, 0, 0, 0, 0, 0]
i[2]: 3
high:  35
ans[i - 1] = 1:  [1, 0, 1, 0, 0, 0, 0]
ans[1]:  [1, 2, 1, 0, 0, 0, 0]
ans[1]:  [3, 2, 1, 0, 0, 0, 0]
i[2]: 5
high:  28
ans[i - 1] = 1:  [3, 2, 1, 0, 1, 0, 0]
ans[1]:  [3, 2, 1, 2, 1, 0, 0]
ans[1]:  [3, 2, 3, 2, 1, 0, 0]
ans[1]:  [3, 4, 3, 2, 1, 0, 0]
ans[1]:  [5, 4, 3, 2, 1, 0, 0]
i[2]: 7

Your Output:

[5,4,3,2,1,0,0]

Expected output:

[1,4,1,2,1,0,0]

'''
        
