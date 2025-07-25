import sys

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        print(temperatures)
        l = len(temperatures)
        ans = [0] * l
        high = temperatures[0]
        high_i = 0
        i = 1
        count = 0
        print (ans)
        while i < len(temperatures):
            if temperatures[i] > high:
                new_high_i = i
                print("new_high_i: ", new_high_i)
                high = temperatures[new_high_i]
                print("high: ", high)
                ans[i - 1] = 1
                print("ans[i - 1] = 1: ", ans)
                i -= 1
                while i > high_i and temperatures[i - 1] <= temperatures[i]:
                    print("i > high_i and temperatures[i - 1] <= temperatures[i]")
                    if  ans[i - 1] == 0:
                        ans[i - 1] = ans[i] + 1
                        print("ans[1]: ", ans)
                    i -= 1
                high_i = new_high_i
                print("high_i: ", high_i)
                i = new_high_i + 1
                print("high: ", high, " new_high_i: ", new_high_i)
                print("in i:", i)
            else:
                i += 1
                print("out i:", i)
        return ans


s = Solution()
n = [30,38,30,36,35,40,28]  # gets the first argument after the script name, like  "python3 debug.py n"
print(s.dailyTemperatures(n))

            
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
        
