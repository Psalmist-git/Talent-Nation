def first_unique(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    for char in text:
        if char_count[char] == 1:
            return char
    return None

print(first_unique("leetcode"))
print(first_unique("aabbcddee"))
print(first_unique("aabbcc"))