class Solution:
    seperator = 'noice'
    l = len(seperator)
    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += s + seperator
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        while s not '':
            if s[0:l] == seperator:
                s = s[l:]
            ans.append(s[0])
            s = s[1:]
        return ans




