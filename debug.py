

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
    def pass(self) -> None:
        if not stop:
            back = 0 #index of back, first-reached-in-this-pass side of a possible pool. no stop so this is the first, full pass
        else:
            back = len(height) - 1 #this is the second, backwards pass to the stop point
        for i, h in enumerate(height):
            if h > 0:
                l = i
                print("l = ", back)
                break
        front = l + 1 #index of current spot being considered for the front side of a pool, ie the side that is new and farther in the direction of the pass
        t = front # index of rightmost tallest found so far to the right of l. Used to find pools when there is no wall as high as height[l]
        while front != len(height) - 1:
            if height[front] >= height[t]:
                print("height[front] >= height[t]:")
                t = r
            if front > l + 1 and height[front] >= height[l]: #found the right side of a pool because it is as high as the left
                print("counting water with l = ", l, " and front = ", front)
                water += Solution.count_water(l, t, height)
                print("water == ", water)
                #reset values because now searching for next pool
                t = front
                l = front
            else:
                front += 1
                print("front == ", front)
                print("l == ", l)
                print("t == ", t)
                print('\n')
        #go backwards to highest point
        if not stop:
            pass(self)
            
            
    def trap(self, height: list[int]) -> int:
        self.stop = None #where to stop early on the second, backwards pass, at the high point
        self.water = 0 #water found
        self.front =
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