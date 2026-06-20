class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)
        stack = [] # monotonic stack

        for i in range(len(temperatures)):
            # remove from stack when we encounter a temp greater than last temp on stack
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop()
                answer[t] = i - t

            # always get the next temp
            stack.append(i)

        return answer

