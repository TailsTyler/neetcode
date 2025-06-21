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