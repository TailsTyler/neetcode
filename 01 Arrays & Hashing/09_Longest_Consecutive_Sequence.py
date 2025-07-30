class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        note = {}
        if len(nums) == 0:
            return 0
        smallest = nums[0]
        biggest = nums[0]
        for n in nums:
            if n not in note:
                note[n] = n
                if n < smallest:
                    smallest = n
                elif n > biggest:
                    biggest = n
        print("len(note)", len(note))
        print("smallest ", smallest)
        print("biggest ", biggest)
        ans = 0
        current_run = 0
        last_one_was_1_less = False
        for i in range(smallest, biggest + 1):
            if ans > biggest + 1 - i + current_run:
                print("made sense to stop short")
                return ans
            if i in note:
                current_run += 1
                print(i, " in note so current_run now ", current_run)
                last_one_was_1_less = True
            else:
                if current_run > ans:
                    ans = current_run
                current_run = 0
                last_one_was_1_less = False
        if current_run > ans:
            ans = current_run
        return ans



        