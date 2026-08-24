class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)

        stack = []  # stores [temperature, index]

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                old_temp, old_index = stack.pop()

                result[old_index] = i - old_index

            stack.append([temp, i])

        return result