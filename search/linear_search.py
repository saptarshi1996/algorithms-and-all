from helper import (
    generate_random_list,
    generate_random_number,
)


def linear_search(nums: list[int], x: int) -> int:
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def main():

    rand = generate_random_number(0, 1000)
    nums = generate_random_list(1000, 2000, 9000)

    x = nums[rand]

    index = linear_search(nums, x)
    print(f'{x} is at index {index}')


main()
