def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    if needle in haystack:
        return haystack.index(needle)

print(strStr("leetcode","leet"))