import sys
import unittest



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
            if i == 2:
                pass
            if temperatures[i] > temperatures[i - 1] and ans[i - 1] == 0:
                nonlowest_i = i #an index of a day that could have colder unsolved days before it 
                ans[i - 1] = 1
                if temperatures[i] > high:
                    new_high_i = i
                    high = temperatures[new_high_i]
                i_to_return_to = i
                i -= 1
                while i > high_i:
                    if  ans[i - 1] == 0 and temperatures[i - 1] < temperatures[nonlowest_i]:
                        ans[i - 1] = nonlowest_i - i + 1
                    i -= 1
                i = i_to_return_to
                try:
                    high_i = new_high_i
                    i = new_high_i + 1
                except:
                    pass
                high = temperatures[high_i]
            else:
                i += 1
        return ans


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
        
