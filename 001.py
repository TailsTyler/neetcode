class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force; works
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]
        
        # one pass
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[nums[i]] = i
        return []

        # # code golf
        #hash_map = {}
        #i = -1
        #c = 0
        #out = []
        #map(lambda x: (i := i + 1,
        #               c := target - x,
        #               (out, nums) := ([i, hash_map[c]], None) if c in hash_map else (out, nums),
        #               hash_map[nums[i]] := i)[-1], nums)
        #return out
        