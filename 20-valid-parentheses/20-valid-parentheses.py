class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for word in s:
            if word in dic.values():
                stack.append(word)
            elif stack and dic[word] == stack[-1]:
                stack.pop()
            else: return False

        if stack:
            return False
        return True