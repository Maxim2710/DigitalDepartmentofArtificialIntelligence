def number_to_excel_column(n):
    column_name = []

    while n > 0:
        n -= 1
        remainder = n % 26
        column_name.append(chr(remainder + ord('A')))
        n //= 26

    return ''.join(reversed(column_name))


n = int(input())
print(number_to_excel_column(n))
