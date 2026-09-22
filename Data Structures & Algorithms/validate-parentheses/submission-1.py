class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in "({[":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                
                ch = stack.pop()
                if ch == "(" and b == ")" or \
                ch == "{" and b == "}" or \
                ch == "[" and b == "]":
                    continue
                else:
                    return False

        return len(stack) == 0


        