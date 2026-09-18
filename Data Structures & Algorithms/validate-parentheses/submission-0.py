class Solution:
    def isValid(self, s: str) -> bool:
        char_check={']':'[', '}':'{', ')':'('}
        stack=[]

        for char in s:
            if char in char_check:
                if stack and stack[-1] == char_check[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0