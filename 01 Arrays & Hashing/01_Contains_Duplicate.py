class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        firsts = []
        for n in nums:
            try:
                x = firsts.index(n)
                return True
            except:
                firsts.append(n)
        return False
         