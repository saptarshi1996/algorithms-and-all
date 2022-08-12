from helper import (
    generate_random_list,
    generate_random_number,
)


def binary_search(nums: list[int], start: int, end: int, x: int):
    if start <= end:
        mid = (start + end) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return binary_search(nums, start, mid-1, x)
        elif nums[mid] < x:
            return binary_search(nums, mid+1, end, x)
    else:
        return -1


def main():

    rand = generate_random_number(0, 1000)
    nums = generate_random_list(1000, 2000, 9000)

    # sort array for BS to work.
    nums.sort()

    x = nums[rand]

    index = binary_search(nums, 0, len(nums)-1, x)
    print(f'{x} is at index {index}')


main()
