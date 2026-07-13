class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i != bracket_dict[stack[-1]]:
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False
        return True