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
        for i in range(smallest, biggest):
            if i in note:
                current_run += 1
                last_one_was_1_less = True
            else:
                if current_run > ans:
                    ans = current_run
                current_run = 0
                last_one_was_1_less = False
        if current_run > ans:
            ans = current_run
        return ans



