class Solution:
    def isValid(self, s: str) -> bool:
        opens = '({['
        closes = ')}]'
        print(s)
        collection = []
        i = 0
        while i < len(s) - 1:
            try:
                open = opens.index(s[i])
            except:
                open = None
            if open:
                collection.append(open)
            else:
                try:
                    if collection[-1] == closes.index(s[i]):
                        collection = collection[1:]
                    else:
                        print("a")
                        return False
                except:
                    return False
                    print("b")
            i+=1
        return True
s="([{}])"
sol = Solution()
print(sol.isValid(s))