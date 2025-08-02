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
        





        '''

        old solution before watching video that was convoluted but only failed on advanced tests like the one below


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
            #check for collisions
            for i in reversed(range(len(position) - 1)):
                #collision
                if position[i] >= position[i+1]:
                    self.delete(i, position, speed) #delete the one that used to be in the back cuz it is faster, and fleets go at the lower speed
            #remove any that have reached the target, now that collisions are dealt with
            for i in reversed(range(len(position))):
                if position[i] >= target:
                    self.delete(i, position, speed)
                    arrived += 1
                else:
                    break
        return arrived + len(position)
'''
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