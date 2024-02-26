import time

# achieve linear time complexity
def computeLPSArray(pattern):
    pattern_len = len(pattern)
    lps = [0] * pattern_len
    length = 0
    i = 1
    while i < pattern_len:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def findPattern(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    lps = computeLPSArray(pattern)
    i = 0
    j = 0
    while i < text_len:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == pattern_len:
            return i - j
        elif i < text_len and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def countPattern(pattern, filename):
    count = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            if findPattern(line, pattern) != -1:
                count += 1
    return count

# Test with the file
pattern_to_find = "radioactive"
file_name = "curie_quotes.txt"

start_time = time.time()
result = countPattern(pattern_to_find, file_name)
end_time = time.time()
print(f"The pattern '{pattern_to_find}' appears {result} times in the file.")
print(f"Time taken: {end_time - start_time} seconds.")
