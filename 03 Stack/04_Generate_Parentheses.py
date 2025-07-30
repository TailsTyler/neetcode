class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        '''open_n, closed_n: num of type of parens so far
        w: an element in the answer being worked on. eg if n == 2, '((' is an element being worked on that will become '(())' and then be added to the ans'''
        def tree(open_n, closed_n, w):
            if open_n == closed_n == n:
                ans.append(w)
                print("ans: ", ans)
                return
            if open_n < n:
                w += '('
                tree(open_n + 1, closed_n, w)
                w = w[0:-1]
            if closed_n < open_n:
                w += ')'
                tree(open_n, closed_n + 1, w)
                w = w[0:-1]
        tree(0, 0, '')
        return ans