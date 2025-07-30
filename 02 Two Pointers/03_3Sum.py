class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        if nums[0] > 0:
            print("no nonpositives")
            return ans
        if nums[-1] < 0:
            print ('no nonnegitives')
            return ans
        i = 0
        j = 1
        print(nums)
        first_non_neg = first_non_neg_in_sorted_list(nums)
        k = first_non_neg
        print("k: ", k, "(index of ",  nums[k], ")")
        nums_i = nums[i]
        while nums_i <= 0:
            k = max(first_non_neg, i + 2)
            print("k: ", k)#, "(index of ",  nums[k], ")")
            while k < len(nums):
                nums_at_j_must_be = -(nums[i] + nums[k])
                print("nums_at_j_must_be: ", nums_at_j_must_be)
                try:
                    j = nums.index(nums_at_j_must_be, i + 1, k)
                    print("j: ", j)
                    while True:
                        try:
                            q = ans.index([nums[i], nums[j], nums[k]])
                            print([nums[i], nums[j], nums[k]], " is already at ", q)
                        except:
                            ans.append([nums[i], nums[j], nums[k]])
                            print("added ", [nums[i], nums[j], nums[k]])
                        j+=1
                        if j == k or nums[j] != nums_at_j_must_be:
                            break
                except:
                    print(nums_at_j_must_be, " not found")
                k+=1
            i+=1
            try:
                nums_i = nums[i]
            except:
                break
            print("i: ", i)#, " which has a ", nums[i])
        return ans
