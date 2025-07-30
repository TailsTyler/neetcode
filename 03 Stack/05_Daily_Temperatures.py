class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        print(temperatures)
        l = len(temperatures)
        ans = [0] * l
        high = temperatures[0]
        high_i = 0
        i = 1
        count = 0
        print (ans)
        while i < len(temperatures):
            if i == 2:
                pass
            if temperatures[i] > temperatures[i - 1] and ans[i - 1] == 0:
                nonlowest_i = i #an index of a day that could have colder unsolved days before it 
                ans[i - 1] = 1
                if temperatures[i] > high:
                    new_high_i = i
                    high = temperatures[new_high_i]
                i_to_return_to = i
                i -= 1
                while i > high_i:
                    if  ans[i - 1] == 0 and temperatures[i - 1] < temperatures[nonlowest_i]:
                        ans[i - 1] = nonlowest_i - i + 1
                    i -= 1
                i = i_to_return_to
                try:
                    high_i = new_high_i
                    i = new_high_i + 1
                except:
                    pass
                high = temperatures[high_i]
            else:
                i += 1
        return ans