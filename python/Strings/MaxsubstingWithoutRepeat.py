def sub(s):
    seen = {}
    left = 0
    max_len = 0
    start_index = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left

    return s[start_index:start_index+max_len], max_len

a="pwwkew"
r=sub(a)
print(r[0])
print(r[1])
