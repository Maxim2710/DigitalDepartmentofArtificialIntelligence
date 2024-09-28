def main():
    n1, n2 = map(int, input().split())

    print("    |", end="")
    for i in range(n2):
        print(f" {i + 1:3}", end="")
    print()

    print("   --", end="")
    for _ in range(n2):
        print("----", end="")
    print()

    for i in range(n1):
        print(f"{i + 1:4}|", end="")
        for j in range(n2):
            print(f" {((i + 1) * (j + 1)):3}", end="")
        print()

if __name__ == "__main__":
    main()
