from collections import Counter

line = input().strip()

words = line.split()

filtered_words = []
for word in words:
    if word == 'end':
        break
    filtered_words.append(word)

word_counts = Counter(filtered_words)

repeated_words = [word for word, count in word_counts.items() if count > 1]

repeated_words.sort()

print(' '.join(repeated_words))
