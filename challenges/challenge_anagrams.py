def is_anagram(first_str, second_str):
    if not first_str and not second_str:
        return (first_str, second_str, False)

    first_sorted = merge_sort(first_str.lower())
    second_sorted = merge_sort(second_str.lower())
    equality = first_sorted == second_sorted

    return (first_sorted, second_sorted, equality)


def merge_sort(str):
    if len(str) <= 1:
        return str

    middle = len(str) // 2
    left_half = merge_sort(str[:middle])
    right_half = merge_sort(str[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return "".join(result)
