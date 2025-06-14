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
    def trap(self, height: list[int]) -> int:
        l = 0 #index of left side of a possible pool
        for i, h in enumerate(height):
            if h > 0:
                l = i
                print("l = ", l)
                break
        r = 0 #index of current spot being considered for the right side of a pool
        t = 0 # index of rightmost tallest found so far to the right of l. Used to find pools when there is no wall as high as height[l]
        water = 0 #water found
        while r != len(height) - 1:
            if height[r] >= height[t]:
                print("height[r] >= height[t]:")
                t = r
            if r > l + 1 and height[r] >= height[l]: #found the right side of a pool because it is as high as the left
                print("counting water with l = ", l, " and r = ", r)
                water += Solution.count_water(l, t, height)
                print("water == ", water)
                #reset values because now searching for next pool
                t = r
                l = r
            else:
                r += 1
                print("r == ", r)
                print("l == ", l)
                print("t == ", t)
                print('\n')
        #go backwards to highest point
        stop = t
        print("turning around. stop = ", stop)
        l = r - 1
        t = r
        while l != stop - 1:
            if height[l] >= height[t]:
                print("height[l] >= height[t]:")
                t = l
            if l > r + 1 and height[l] >= height[r]: #found the left side of a pool because it is as high as the right
                print("counting water with r =", r, " and l =", l)
                water += Solution.count_water(r, t, height)
                print("water == ", water)
                #reset values because now searching for next pool
                t = l
                r = l
            else:
                l -= 1
                print("l == ", l)
                print("r == ", r)
                print("t == ", t)
                print('\n')
        return water
#height = [0,2,0,3,1,0,1,3,2,1]
height=[0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))
