

class Solution:
    @staticmethod
    def count_water(back, front, direction, height) -> int:
        if height[back] > 0 and height[front] > 0:
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
        while bool(self.front > self.back) == forward and self.front != self.stop + self.direction:
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
        if len(height) == 1:
            return 0
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
height=[4,2,0,3,2,5]
sol = Solution()
print(sol.trap(height))

'''
Wrong Answer

Passed test cases: 7 / 22

Last executed test case

Input:

height=[4,2,3]

stdout:

self.stop =  2
forward: True
True
front ==  1
back ==  0


next
front ==  2
back ==  0


next
turning around. stop =  0 

self.front = self.back + self.direction =  1 

forward: False
True
front ==  1
back ==  2


next
front ==  0
back ==  2


counting water with self.back =  2  and self.front =  0
d =  1
rectangle = height[front] * d =  4  *  1  =  4
height[ 0 ] is  4  brings stuff_in_between to  2
new water = rectangle - stuff_in_between =  4  -  2
water ==  2

Your Output:

2

Expected output:

1
'''