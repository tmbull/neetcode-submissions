class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        # iterate through list
            # for each temp, iterate forward until a higher temp is found
            # result[i] = j
        # how to use a stack?

        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                topT, topI = stack.pop()
                result[topI] = i - topI
            stack.append((t, i))

        return result