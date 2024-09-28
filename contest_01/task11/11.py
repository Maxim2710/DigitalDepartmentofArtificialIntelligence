a, b, c = map(int, input().split())

distance_to_b = abs(a - b)
distance_to_c = abs(a - c)

if distance_to_b < distance_to_c:
    print(f"B {distance_to_b}")
else:
    print(f"C {distance_to_c}")
