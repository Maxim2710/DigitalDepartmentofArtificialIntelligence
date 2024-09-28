def leg_count_in_longest_sequence(legs):
    if not legs:
        return None

    max_length = 0
    max_number = legs[0]

    current_length = 1
    current_number = legs[0]

    for i in range(1, len(legs)):
        if legs[i] == current_number:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_number = current_number
            current_number = legs[i]
            current_length = 1

    if current_length > max_length:
        max_number = current_number

    return max_number


legs = [int(i) for i in input().split()]
print(leg_count_in_longest_sequence(legs))
