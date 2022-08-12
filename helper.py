import random


def generate_random_list(size, lower, upper) -> list[int]:
    return [int(random.randint(lower, upper)) for _ in range(size)]


def generate_random_number(lower, upper) -> int:
    return int(random.randint(lower, upper))


def is_list_sorted(ls: list[int]) -> bool:
    size = len(ls)
    for i in range(size-1):
        if ls[i+1] < ls[i]:
            return False
    return True
