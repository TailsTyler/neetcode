

class Solution:
    @staticmethod
    def count_water(back, front, direction, height) -> int:
        if back > 0 and front > 0:
            d = abs(front - back) - 1
            print("d = ", d)
        else:
            return 0
        if front > back:
            rectangle = height[back] * d
            print("rectangle = height[back] * d = ", height[back], " * ", d, " = ", height[back] * d)
        else:
            rectangle = height[front] * d
            print("rectangle = height[front] * d = ", height[front], " * ", d, " = ", height[front] * d)
        stuff_in_between = 0
        i = back + direction
        while i != front:
            stuff_in_between += height[i]
            i+=direction
            print("height[", i, "] is ", height[i], " brings stuff_in_between to ", stuff_in_between)
        print("new water = rectangle - stuff_in_between = ", rectangle, " - ", stuff_in_between)
        return rectangle - stuff_in_between
    #for passing all the way thru the first time, then backwarks to stop
    def walk(self) -> None:
        if self.direction == 1:
            forward = True
        else:
            forward = False
        print("forward:", forward)
        print(bool(self.front > self.back) == forward and self.front != self.stop)
        while bool(self.front > self.back) == forward and self.front != self.stop:
            print("front == ", self.front)
            print("back == ", self.back)
            print("\n")
            if self.height[self.front] >= self.height[self.back]: #found the right side of a pool because it is as high as the left
                print("counting water with self.back = ", self.back, " and self.front = ", self.front)
                self.water += Solution.count_water(self.back, self.front, self.direction, self.height)
                print("water == ", self.water)
                #reset values because now searching for next pool
                self.back = self.front
                self.front = self.back + self.direction
            else:
                print("next")
                self.front += self.direction

    def trap(self, height: list[int]) -> int:
        self.height = height
        self.water = 0 #water found

        self.direction = 1 #unit with sign indicating
        self.stop = len(height) - 1 #where to stop on this pass
        print("self.stop = ", self.stop)
        self.back = 0 #index of back, first-reached-in-this-pass side of a possible pool
        for i, h in enumerate(height):
            if h > 0:
                self.back = i
                break
        #index of current spot being considered for the front side of a pool, ie the side that is new and farther in the direction of the pass
        self.front = self.back + self.direction
        #first, forward, full pass
        self.walk()
        self.stop = self.back
        print("turning around. stop = ", self.stop, "\n")
        self.direction = -1
        self.back = len(height) - 1
        while height[self.back] == 0 and self.back >= 0:
            self.back += self.direction
        self.front = self.back + self.direction
        print("self.front = self.back + self.direction = ", self.front, "\n")
        #second, backwards pass to the stop point: the high point
        self.walk()
        return self.water
#height = [0,2,0,3,1,0,1,3,2,1]
height=[0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))

'''
Traceback (most recent call last):
  File "/box/script.py", line 96, in main
    output = solution.trap(input)
             ^^^^^^^^^^^^^^^^^^^^
  File "/box/script.py", line 75, in trap
    self.walk()
  File "/box/script.py", line 49, in walk
    if self.height[self.front] >= self.height[self.back]: #found the right side of a pool because it is as high as the left
       ~~~~~~~~~~~^^^^^^^^^^^^
IndexError: list index out of range

Last executed test case

Input:
          2 4 1 2 = 9
height=[4,2,0,3,2,5]
        0 1 2 3 4 5

stdout:

self.stop =  5
forward: True
True
front ==  1
back ==  0


next
front ==  2
back ==  0


next
front ==  3
back ==  0


next
front ==  4
back ==  0


next
turning around. stop =  0 

self.front = self.back + self.direction =  4 

forward: False
True
front ==  4
back ==  5


next
front ==  3
back ==  5


next
front ==  2
back ==  5


next
front ==  1
back ==  5


next

Your Output:

0

Expected output:

9
'''