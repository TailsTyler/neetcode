#this is a temporary place to put code while debugging it

import sys
import unittest

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

t = 10
p = [4,1,0,7]
s = [2,2,1,1]

s = Solution()
print(s.carFleet(t, p, s))

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
        
