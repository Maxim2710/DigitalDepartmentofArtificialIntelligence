def print_wave_pattern(N):
    num = 1
    on_r = 3
    cnt_str = 1
    regulator = 1

    while num <= N:
        for _ in range(cnt_str):
            if num > N:
                return
            print(num, end=' ')
            num += 1
        print()

        cnt_str += regulator
        if cnt_str < 1:
            regulator = 1
            cnt_str = 2
            on_r += 1
        elif cnt_str >= on_r:
            regulator = -1
            cnt_str -= 2


N = int(input())
print_wave_pattern(N)
