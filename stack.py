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