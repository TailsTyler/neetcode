class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        note = {}
        # for i, n in enumerate(numbers):
        #     if not n in note:
        #         note[n] = i
        front = 0
        back = len(numbers) - 1
        while front != back:
            if numbers[front] + numbers[back] == target:
                return [front + 1, back + 1]
            elif numbers[front] + numbers[back] < target:
                front += 1
            else:
                back -= 1
        return "error"



        