class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        while True:
            d = r - l
            new_area = min(heights[l], heights[r]) * d
            if new_area > area:
                area = new_area

                print("area is now ", area, " since heights[l] == ", heights[l], " and heights[r] == ", heights[r], " and the distance is ", d)
            if heights[l] < heights[r]:
                l+=1
                print("left is now ", heights[l])
            else:
                r-=1
                print("right is now ", heights[r])
            if l == r:
                break
        return area