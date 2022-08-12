from helper import (
    generate_random_list,
    is_list_sorted
)


def partition(nums, start, end) -> int:
    i, pivot = start-1, nums[end]
    for j in range(start, end):

        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[end] = nums[end], nums[i+1]
    return i+1


def quicksort(nums, start, end) -> list[int]:
    if start <= end:
        pi = partition(nums, start, end)
        quicksort(nums, start, pi-1)
        quicksort(nums, pi+1, end)

    return nums


def main():

    nums = generate_random_list(10, 100, 200)

    result = quicksort(nums, 0, len(nums) - 1)

    valid = is_list_sorted(result)

    print("List sorted" if valid else "List not sorted")


if __name__ == '__main__':
    main()
