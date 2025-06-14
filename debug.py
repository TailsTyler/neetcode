

class Solution:
    @staticmethod
    def count_water(l, r, height) -> int:
        if l > 0 and r > 0:
            d = r - l - 1
            print("d = ", d)
        else:
            return 0
        if r > l:
            rectangle = height[l] * d
            print("rectangle = height[l] * d = ", height[l], " * ", d, " = ", height[l] * d)
        else:
            rectangle = height[r] * d
            print("rectangle = height[r] * d = ", height[r], " * ", d, " = ", height[r] * d)
        stuff_in_between = 0
        for i in range(l + 1, r):
            stuff_in_between += height[i]
            print("height[", i, "] brings stuff_in_between to ", stuff_in_between)
        print("new water = rectangle - stuff_in_between = ", rectangle, " - ", stuff_in_between)
        return rectangle - stuff_in_between
    #for passing all the way thru the first time, then backwarks to stop
    def walk(self) -> None:
        while self.front != self.stop:
            if self.height[self.front] >= self.height[self.t]:
                print("self.height[self.front] >= self.height[t]:")
                t = self.front
            if self.front > self.back + 1 and self.height[self.front] >= self.height[self.back]: #found the right side of a pool because it is as high as the left
                print("counting water with l = ", self.back, " and self.front = ", self.front)
                self.water += Solution.count_water(self.back, t, self.height)
                print("water == ", self.water)
                #reset values because now searching for next pool
                t = self.front
                self.back = self.front
            else:
                self.front += self.direction
                print("front == ", self.front)
                print("back == ", self.back)
                print("t == ", self.t)
                print('\n')
    def trap(self, height: list[int]) -> int:
        self.height = height
        self.water = 0 #water found

        self.direction = 1 #unit with sign indicating
        self.stop = len(height) - 1 #where to stop on this pass
        self.back = 0 #index of back, first-reached-in-this-pass side of a possible pool
        for i, h in enumerate(height):
            if h > 0:
                self.back = i
                print("back = ", self.back)
                break
        #index of current spot being considered for the front side of a pool, ie the side that is new and farther in the direction of the pass
        self.front = self.back + self.direction
        # index of rightmost tallest found so far to the right of l. Used to find pools when there is no wall as high as height[l]
        self.t = self.front
        #first, forward, full pass
        self.walk()
        self.stop = self.t
        print("turning around. stop = ", self.stop)
        self.direction = -1
        for i, h in enumerate(reversed(self.height)):
            if h > 0:
                self.back = i
                print("back = ", self.back)
                break
        self.front = self.back + self.direction
        self.t = self.back
        #second, backwards pass to the stop point: the high point
        self.walk()
        return water
#height = [0,2,0,3,1,0,1,3,2,1]
height=[0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))

'''
Wrong Answer

Passed test cases: 1 / 22

Last executed test case

Input:
            1   1 2 1     1
height=[0,1,0,2,1,0,1,3,2,1,2,1]
        0 1 2 3 4 5 6 7 8 9 1011

stdout:

l =  1
height[r] >= height[t]:
r ==  1
l ==  1
t ==  0


height[r] >= height[t]:
r ==  2
l ==  1
t ==  1


r ==  3
l ==  1
t ==  1


height[r] >= height[t]:
counting water with l= 1  and r= 3
d =  1
rectangle = height[l] * d =  1  *  1  =  1
height[ 2 ] brings stuff_in_between to  0
new water = rectangle - stuff_in_between =  1  -  0
water ==  1
height[r] >= height[t]:
r ==  4
l ==  3
t ==  3


r ==  5
l ==  3
t ==  3


r ==  6
l ==  3
t ==  3


r ==  7
l ==  3
t ==  3


height[r] >= height[t]:
counting water with l= 3  and r= 7
d =  3
rectangle = height[l] * d =  2  *  3  =  6
height[ 4 ] brings stuff_in_between to  1
height[ 5 ] brings stuff_in_between to  1
height[ 6 ] brings stuff_in_between to  2
new water = rectangle - stuff_in_between =  6  -  2
water ==  5
height[r] >= height[t]:
r ==  8
l ==  7
t ==  7


r ==  9
l ==  7
t ==  7


r ==  10
l ==  7
t ==  7


r ==  11
l ==  7
t ==  7


Your Output:

5

Expected output:

6
'''