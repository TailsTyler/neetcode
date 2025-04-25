class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {} #frequencies. key is the int found; value is the amount counted
        for x in nums:
            if x in freqs:
                freqs[x] += 1
            else:
                freqs[x] = 1
        amounts = []
        for x in freqs:
            amounts.append([freqs[x], x ])
        amounts = sorted(amounts)
        removed = 0
        ans = []
        while removed < k:
            ans.append(amounts.pop(-1)[1])
            removed+=1
        return ans