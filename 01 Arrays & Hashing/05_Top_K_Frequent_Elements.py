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



# #could add binary search
# class Tops_entry:
#     def __init__(self, count, num):
#         self.count = count #the amount of an int found
#         self.num = num #the actual int found
#     def sort(list): #maintains sorting of a list of tops_entry s. new item must be at index 0, as the rest is assumed to be sorted
#         l = len(list)
#         for i in range(l):
#             if i+1 > l - 1:
#                 return
#             elif list[i+1].count < list[i].count:
#                 temp = list[i+1]
#                 list[i+1] = list[i]
#                 list[i] = temp
#             else:
#                 return



            





        ######Tops_entry s will go here. They are condenders for making it into the solution
        # current_int = None #the int i'm currently seeing
        # i = 0
        # jump = 1; #amount to jump by, in case there are many of an int
        # count = 0; #the amount of the current int found
        # l = len(nums)
        # while True:    
        #     if i + jump < l and nums[i] == current_int:
        #         i+= jump
        #         count += jump
        #         jump*=2
        #     else:
        #         if jump == 1:
        #             count += 1
        #             # print("jump == 1")
        #             #we have found the next int
        #             if not tops or count > tops[0].count:
        #                 # print("tops == [] or count > tops[0].count")
        #                 current_int = nums[i]
        #                 #the amount of this int is enough to add it to the contenders
        #                 if tops:
        #                     if len(tops) == k:
        #                         if count > tops[0].count:
        #                             tops[0] = Tops_entry(count, current_int)
        #                             tops = Tops_entry.sort(tops)
        #                 else:
        #                     tops.insert(0, Tops_entry(count, current_int))
        #                     Tops_entry.sort(tops)
        #             count = 0
        #         jump = 1
        #     if i >= l:
        #         return list(tops.values())