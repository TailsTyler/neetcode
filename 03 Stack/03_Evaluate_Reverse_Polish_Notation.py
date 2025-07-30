class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        nums = []
        while tokens != []:
            try:
                nums.append(int(tokens[0]))
                print("nums increased to ", nums)
            except:
                op = tokens[0]
                if op == '+':
                    nums[-2] = nums[-2] + nums[-1]
                elif op == '-':
                    nums[-2] = nums[-2] - nums[-1]
                elif op == '*':
                    nums[-2] = nums[-2] * nums[-1]
                elif op == '/':
                    nums[-2] = int(nums[-2] / nums[-1])
                else:
                    print('error 1')
                nums = nums[0:-1]
                print("op ", op, " occured, making nums ", nums)
            tokens = tokens[1:]
        if len(nums) != 1:
            print("error: len(nums) = ", len(nums))
        return nums[0]

        