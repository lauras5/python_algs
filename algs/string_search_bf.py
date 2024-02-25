import time

def findPattern(text, pattern):
    pattern_len = len(pattern)
    text_len = len(text)
    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            return i
    return -1

# tests
str_a = b"abc"
txt_a = b"abcdefgh"
print(f"{str_a} in {txt_a} is {findPattern(txt_a, str_a)}")

str_b = b"cde"
print(f"{str_b} in {txt_a} is {findPattern(txt_a, str_b)}")

str_c = b"missing"  # fail to find returns -1
print(f"{str_c} in {txt_a} is {findPattern(txt_a, str_c)}")

# check if pattern is in file and count times it appears
def countPattern(pattern, filename):
    count = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            if (findPattern(line, pattern)) != -1:
                count += 1
    return count

pattern_to_find = 'radioactive'
file = 'curie_quotes.txt'

start_time = time.time()
result = countPattern(pattern_to_find, file)
end_time = time.time()

print(f"The pattern '{pattern_to_find}' appears {result} times in the file.")
print(f"Time taken: {end_time - start_time} seconds.")
