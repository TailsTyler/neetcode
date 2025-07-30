class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements:
                print([complements[nums[i]], nums[i]])
                return [complements[nums[i]], i]
            else:
                complements[target - nums[i]] = i 
            print(nums[i])
            print("c: ", complements)
        return None