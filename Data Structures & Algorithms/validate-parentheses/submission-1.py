class Solution:
    def isValid(self, s: str) -> bool:
        # handle edge cases
        if len(s)%2==1:
            return False
        
        pairs = {
                ")": "(",
                "]": "[",
                "}": "{"
            }

        stack = []
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or pairs[ch] != stack[-1]:
                    return False
                
                stack.pop()
        return len(stack) == 0         
