class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha = [] #found_letter_groups_alphabetical
        ans = []
        for s in strs:
            try:
                i = alpha.index(sorted(s))
                ans[i].append(s)
            except:
                alpha.append(sorted(s))
                ans.append([s])
        return ans
                
