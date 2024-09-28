def compress_string(s):
    if not s:
        return ""

    compressed = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        compressed.append(s[i])
        if count > 1:
            compressed.append(str(count))
        i += 1

    return ''.join(compressed)


s = input()
print(compress_string(s))
