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




