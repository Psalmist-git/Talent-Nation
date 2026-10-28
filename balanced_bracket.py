def balanced_brackets(text):
   
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in text:

        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:

            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop() 
            
 
    return len(stack) == 0

print(balanced_brackets("hello"))
print(balanced_brackets("[()]"))
print(balanced_brackets("([)])"))
print(balanced_brackets("((hello)"))