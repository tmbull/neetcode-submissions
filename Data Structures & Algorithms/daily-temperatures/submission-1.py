class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # naive solution
            # iterate ahead from each value until a warmer temperature is found (O(n^2))
        # intuation - iterate backwards?
        # Use a stack to store values/indices where temperatore decreases?
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                top_i, top_t = stack.pop()
                result[top_i] = i - top_i
            stack.append((i, temp))

        return result




