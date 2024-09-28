from collections import Counter

def print_histogram(text):
    count = Counter(text)

    sorted_chars = sorted(count.keys())

    max_freq = max(count.values(), default=0)

    for level in range(max_freq, 0, -1):
        line = ''
        for char in sorted_chars:
            if count[char] >= level:
                line += '#'
            else:
                line += ' '
        print(line.rstrip())

    print(''.join(sorted_chars))

text = input().rstrip('\n')
print_histogram(text)
