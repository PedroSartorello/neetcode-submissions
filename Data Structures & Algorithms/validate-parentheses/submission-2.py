class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        aberto_para_fechado = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in aberto_para_fechado and len(stack) > 0:
                if not stack or stack[-1] != aberto_para_fechado[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
               
        return len(stack) == 0
        