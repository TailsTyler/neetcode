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

        