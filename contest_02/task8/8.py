def are_anagrams(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    if len(str_num1) != len(str_num2):
        return "NO"

    return "YES" if sorted(str_num1) == sorted(str_num2) else "NO"


num1, num2 = input().split()
print(are_anagrams(num1, num2))
