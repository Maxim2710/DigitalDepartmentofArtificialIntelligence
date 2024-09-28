input_string = input().strip()

normalized_string = input_string.lower()

if normalized_string == normalized_string[::-1]:
    print("YES")
else:
    print("NO")
