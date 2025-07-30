class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in s:
            try:
                i = t.index(x)
                # print("got to 1")
                t = t[:i] + t[i + 1:]
                # print(t)
            except:
                # print("s: ", s)
                # print("t: ", t)
                return False
        # print("got to end")
        if t == '':
            return True
        else:
            # print(t);
            return False
        