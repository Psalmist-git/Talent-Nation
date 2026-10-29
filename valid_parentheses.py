def valid_parentheses(text):
    stack = []
    check = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in check.values():
            stack.append(char)
        elif char in check:
            if not stack or stack[-1] != check[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(valid_parentheses("[()]"))
print(valid_parentheses("([)])"))
print(valid_parentheses("((()))"))
print(valid_parentheses("{[}"))
