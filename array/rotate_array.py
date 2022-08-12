from helper import (
    generate_random_list,
    generate_random_number,
)


def reverse(ls: list[int], start: int, end: int) -> list[int]:
    while start <= end:
        ls[start], ls[end] = ls[end], ls[start]
        start += 1
        end -= 1
    return ls


def rotate(ls: list[int], k: int) -> list[int]:

    size = len(ls)

    ls = reverse(ls, 0, size-1)
    ls = reverse(ls, 0, k-1)
    ls = reverse(ls, k, size-1)

    return ls


def main():

    k = generate_random_number(20000, 90000)
    ls = generate_random_list(10000, 10000, 100000)

    result = rotate(ls, k)
    print(*result)


main()
