class Solution:
    def isValid(self, s: str) -> bool:
        opens = '({['
        closes = ')}]'
        print(s)
        collection = []
        i = 0
        print("len(s): ", len(s))
        while i < len(s):
            print("i: ", i)
            try:
                open = opens.index(s[i])
            except:
                open = None
            if open != None:
                collection.append(open)
                print("collection:", collection)
            else:
                try:
                    print("collection[-1]: ", collection[-1])
                    print("closes.index(s[i]: ", closes.index(s[i]))
                    if collection[-1] == closes.index(s[i]):
                        collection = collection[0:-1]
                        print("collection:", collection)
                    else:
                        print("a")
                        return False
                except:
                    print("b")
                    return False
                    
            i+=1
            print("+")
        if collection == []:
            return True
        else:
            return False
# s="(]"
# sol = Solution()
# print(sol.isValid(s))

class MinStack:

    def __init__(self):
        self.l = []
        self.mins = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if self.mins == [] or val <= self.mins[-1]:
            self.mins.append(val)
        

    def pop(self) -> None:
        if self.l[-1] == self.mins[-1]:
            self.mins = self.mins[0:-1]
        self.l = self.l[0:-1]
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        if self.mins == []:
            return None
        else:
            return self.mins[-1]
        

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
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
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
