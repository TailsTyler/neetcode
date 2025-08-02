#this is a temporary place to put code while debugging it

import sys
import unittest

class Solution:

    def is_not_sorted(self, lst):
        return any(lst[i] > lst[i+1] for i in range(len(lst) - 1))
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        paired = list(zip(position, speed))
        paired.sort()   
        position, speed = zip(*paired)
        position = list(position)
        speed = list(speed)
        right_completion_time = (target - position[-1]) / speed[-1]
        for i in reversed(range(len(position) - 1)):
            left_completion_time = (target - position[i]) / speed[i]
            #remove the faster cars in collisions
            if left_completion_time <= right_completion_time:
                position.pop(i)
                speed.pop(i)
            else:
                right_completion_time = left_completion_time
        return len(position)
                          

        # Unzip
        # sorted_weights, sorted_names = zip(*paired)
        
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3


target=31
position=[5,26,18,25,29,21,22,12,19,6]
speed=[7,6,6,4,3,4,9,7,6,4]

x = Solution()
print(x.carFleet(target, position, speed))

# if __name__ == "__main__":
#     unittest.main()

            
'''
[5, 6, 12, 18, 19, 21, 22, 25, 26, 29]
13  10 19  24  25  25  31  29  32  32 
[7, 4,  7,  6,  6,  4,  9,  4,  6,  3]
Input:

target=31
position=[5,26,18,25,29,21,22,12,19,6]
speed=[7,6,6,4,3,4,9,7,6,4]

Your Output:

4

Expected output:

6
'''
        
