#this is a temporary place to put code while debugging it

import sys
import unittest

class Solution:

    def delete(self, i, position, speed):
        position.pop(i)
        speed.pop(i)
    def is_not_sorted(self, lst):
        return any(lst[i] > lst[i+1] for i in range(len(lst) - 1))
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        paired = list(zip(position, speed))
        paired.sort()   
        position, speed = zip(*paired)
        position = list(position)
        speed = list(speed)
        arrived = 0 #fleets that have made it to the target

        while self.is_not_sorted(speed): #if the speeds are a sorted list, cars will never each each other
            #advance all fleets forward by their speed amount
            for i in reversed(range(len(position))):
                position[i] += speed[i]
                #passed target
                if position[i] > target:
                    self.delete(i, position, speed)
                    arrived += 1
            #check for collisions
            for i in reversed(range(len(position) - 1)):
                #collision
                if position[i] >= position[i+1]:
                    self.delete(i, position, speed) #delete the one that used to be in the back cuz it is faster, and fleets go at the lower speed
        return arrived + len(position)
                          

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

target=16
position=[11,14,13,6]
speed=[2,2,6,7]

Your Output:

3

Expected output:

2
'''
        
