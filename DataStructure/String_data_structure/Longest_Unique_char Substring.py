# TODO: Question 1 Longest Unique char Substring -
#  Given a string s, find the length of the longest substring
#  without repeating characters.


def max_unique_length(str1):

    start = 0
    max_len = 0
    seen = {}
    for i in range(len(str1)):
        char = str1[i]
        if char in seen:
            start = max(start, seen[char]+1)
        max_len = max(max_len, i-start+1)
        seen[char] = i
    return max_len

print(max_unique_length('pqbrstbuvwpvy'))