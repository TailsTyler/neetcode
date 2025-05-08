class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + '#' + s
        print("encoded ", ans)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        while s != '':
            i = 0
            while s[i] != '#':
                i+=1
            # print("int(s[1:i]) ", int(s[1:i]))
            length = int(s[0:i])
            print("length ", length)
            ans.append(s[i + 1 : i + 1 + length])
            s = s[1 + i + length:]
        return ans


class Solution:
    # #initial solution
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = 1
    #     zeros = False
    #     nonzeros = False
    #     for n in nums:
    #         if n != 0:
    #             nonzeros = True
    #             product *= n
    #         else:
    #             if zeros:
    #                 product = 0
    #                 break
    #             zeros = True
    #     ans = []
    #     if not zeros:
    #         for n in nums:
    #             ans.append(int(product/n))
    #     else:
    #         if not nonzeros:
    #             for n in nums:
    #                 ans.append(0)
    #         else:
    #             for n in nums:
    #                 if n != 0:
    #                     ans.append(0)
    #                 else:
    #                     ans.append(product)
    #     return ans
        
    #no division and use only the ans array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [1] * len(nums)
        #get those prefixes!
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        print("prefixes: ", ans)
        #get those suffixes and use them to leave answers in their wake!  
        suffix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i]
            ans[i] *= suffix
            suffix *= temp
            print(suffix)
        return ans






class Solution:
    # def check(item, location):
    #     if item in location:
    #         print(item, "is in ", location)
    #         return False
    #     else:
    #         location[item] = "it doesnt matter what i am ;("
    #         print("added ", item, " to ", location)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board)
        rows = [{} for _ in range(len_board)]
        cols = [{} for _ in range(len(board[0]))]
        sub_boxes = 9
        sub_boxes = int(math.pow(sub_boxes, .5))
        sub_boxes = [[{} for j in range(sub_boxes)] for i in range(sub_boxes)]
        for i, r in enumerate(board):
            for j, x in enumerate(r):
                if x != '.':
                    if x in rows[i]:
                        print(x, "is in rows[", i, "]")
                        return False
                    else:
                        rows[i][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to rows[", i, "]")
                    if x in cols[j]:
                        print(x, "is in cols[", j, "]")
                        return False
                    else:
                        cols[j][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to cols[", j, "]")
                    i_box = i//3
                    j_box = j//3
                    if x in sub_boxes[i_box][j_box]:
                        print(x, "is in sub_boxes[", i_box, "]", "[", j_box, "]")
                        return False
                    else:
                        sub_boxes[i_box][j_box][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to sub_boxes[", i_box, "]", "[", j_box, "]")
                    
                # Solution.check(x, rows[i])
                # Solution.check(x, cols[j])
                # Solution.check(x, sub_boxes[i//3][j//3])
                
        return True







class Solution:
    # def check(item, location):
    #     if item in location:
    #         print(item, "is in ", location)
    #         return False
    #     else:
    #         location[item] = "it doesnt matter what i am ;("
    #         print("added ", item, " to ", location)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board)
        rows = [{} for _ in range(len_board)]
        cols = [{} for _ in range(len(board[0]))]
        sub_boxes = 9
        sub_boxes = int(math.pow(sub_boxes, .5))
        sub_boxes = [[{} for j in range(sub_boxes)] for i in range(sub_boxes)]
        for i, r in enumerate(board):
            for j, x in enumerate(r):
                if x != '.':
                    if x in rows[i]:
                        print(x, "is in rows[", i, "]")
                        return False
                    else:
                        rows[i][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to rows[", i, "]")
                    if x in cols[j]:
                        print(x, "is in cols[", j, "]")
                        return False
                    else:
                        cols[j][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to cols[", j, "]")
                    i_box = i//3
                    j_box = j//3
                    if x in sub_boxes[i_box][j_box]:
                        print(x, "is in sub_boxes[", i_box, "]", "[", j_box, "]")
                        return False
                    else:
                        sub_boxes[i_box][j_box][x] = "it doesnt matter what i am ;("
                        print("added ", x, " to sub_boxes[", i_box, "]", "[", j_box, "]")

                # Solution.check(x, rows[i])
                # Solution.check(x, cols[j])
                # Solution.check(x, sub_boxes[i//3][j//3])

        return True



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        note = {}
        if len(nums) == 0:
            return 0
        smallest = nums[0]
        biggest = nums[0]
        for n in nums:
            if n not in note:
                note[n] = n
                if n < smallest:
                    smallest = n
                elif n > biggest:
                    biggest = n
        print("len(note)", len(note))
        print("smallest ", smallest)
        print("biggest ", biggest)
        ans = 0
        current_run = 0
        last_one_was_1_less = False
        for i in range(smallest, biggest + 1):
            if ans > biggest + 1 - i + current_run:
                print("made sense to stop short")
                return ans
            if i in note:
                current_run += 1
                print(i, " in note so current_run now ", current_run)
                last_one_was_1_less = True
            else:
                if current_run > ans:
                    ans = current_run
                current_run = 0
                last_one_was_1_less = False
        if current_run > ans:
            ans = current_run
        return ans







def first_non_neg_in_sorted_list(sorted_list):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        # print("mid:", mid,"; sorted_list[mid]: ", sorted_list[mid])
        if sorted_list[mid] >= 0:
            if sorted_list[mid] == 0 and sorted_list[mid - 1] < 0:
                return mid
            else:
                right = mid - 1
        else:
            left = mid + 1
    return 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        if nums[0] > 0:
            print("no nonpositives")
            return ans
        if nums[-1] < 0:
            print ('no nonnegitives')
            return ans
        i = 0
        j = 1
        print(nums)
        first_non_neg = first_non_neg_in_sorted_list(nums)
        k = first_non_neg
        print("k: ", k, "(index of ",  nums[k], ")")
        nums_i = nums[i]
        while nums_i <= 0:
            k = max(first_non_neg, i + 2)
            print("k: ", k)#, "(index of ",  nums[k], ")")
            while k < len(nums):
                nums_at_j_must_be = -(nums[i] + nums[k])
                print("nums_at_j_must_be: ", nums_at_j_must_be)
                try:
                    j = nums.index(nums_at_j_must_be, i + 1, k)
                    print("j: ", j)
                    while True:
                        try:
                            q = ans.index([nums[i], nums[j], nums[k]])
                            print([nums[i], nums[j], nums[k]], " is already at ", q)
                        except:
                            ans.append([nums[i], nums[j], nums[k]])
                            print("added ", [nums[i], nums[j], nums[k]])
                        j+=1
                        if j == k or nums[j] != nums_at_j_must_be:
                            break
                except:
                    print(nums_at_j_must_be, " not found")
                k+=1
            i+=1
            try:
                nums_i = nums[i]
            except:
                break
            print("i: ", i)#, " which has a ", nums[i])
        return ans





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





class Solution:
    @staticmethod
    def count_water(l, r, height) -> int:
        if l > 0 and r > 0:
            d = r - l
        else:
            return 0
        if r > l:
            rectangle = l * d
        else:
            rectangle = r * d
        stuff_in_between = 0
        for i in range(l + 1, r):
            stuff_in_between += height[i]
        return rectangle - stuff_in_between
    def trap(self, height: List[int]) -> int:
        l = 0 #index of left side of a possible pool
        r = 0 #index of current spot being considered for the right side of a pool
        t = 0 # index of rightmost tallest found so far to the right of l. Used to find pools when there is no wall as high as height[l]
        water = 0 #water found
        while True:
            if height[r] >= height[t]:
                t = r
            if r > l + 1 and height[r] >= height[l]: #found the right side of a pool because it is as high as the left
                Solution.count_water(l, r, height)
                print("water == ", water)
                #reset values because now seaarching for next pool
                t = r
                l = r
            elif r == len(height) - 1: 
                #look for pools where the right side is lower than the left
                if t > l:
                    water += Solution.count_water(l, t, height)
                    print("water == ", water)
                    l = t
                    r = t
            else:
                r += 1
                print("r == ", r)
                
        return water
