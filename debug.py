#this is a temporary place to put code while debugging it

import sys
import unittest

class Solution:
    def delete(self, i):
        self.position.pop(i)
        self.speed.pop(i)
    def is_not_sorted(self, lst):
        return any(lst[i] > lst[i+1] for i in range(len(lst) - 1))
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        paired = list(zip(self.position, self.speed))
        paired.sort()   
        self.position, self.speed = zip(*paired)
        self.position = list(self.position)
        self.speed = list(self.speed)
        arrived = 0 #fleets that have made it to the target

        while self.is_not_sorted(speed): #if the speeds are a sorted list, cars will never each each other
            #advance all fleets forward by their speed amount
            for i in reversed(range(len(self.position))):
                self.position[i] += self.speed[i]
                #passed target
                if self.position[i] > target:
                    self.delete(i)
                    arrived += 1
            #check for collisions
            for i in reversed(range(len(self.position) - 1)):
                #collision
                if self.position[i] >= self.position[i+1]:
                    self.delete(i) #delete the one that used to be in the back cuz it is faster, and fleets go at the lower speed
        return arrived + len(self.position)
                          

        # Unzip
        # sorted_weights, sorted_names = zip(*paired)
        
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

t = 10
p = [4,1,0,7]
''' [6,3,1,8]
    [8,5,2,9] 
    [10,7,3,10]'''
s = [2,2,1,1]

x = Solution()
print(x.carFleet(t, p, s))

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
        
