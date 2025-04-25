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


class Solution:
    # #initial solution
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = 1
    #     zeros = False
    #     nonzeros = False
    #     for n in nums:
    #         if n != 0:
    #             nonzeros = True
    #             product *= n
    #         else:
    #             if zeros:
    #                 product = 0
    #                 break
    #             zeros = True
    #     ans = []
    #     if not zeros:
    #         for n in nums:
    #             ans.append(int(product/n))
    #     else:
    #         if not nonzeros:
    #             for n in nums:
    #                 ans.append(0)
    #         else:
    #             for n in nums:
    #                 if n != 0:
    #                     ans.append(0)
    #                 else:
    #                     ans.append(product)
    #     return ans
        
    #no division and use only the ans array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [1] * len(nums)
        #get those prefixes!
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i-1]
        print("prefixes: ", ans)
        #get those suffixes and use them to leave answers in their wake!  
        suffix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i]
            ans[i] *= suffix
            suffix *= temp
            print(suffix)
        return ans
        

