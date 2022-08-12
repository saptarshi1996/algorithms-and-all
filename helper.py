import random


def generate_random_list(size, lower, upper):
    ls = [int(random.randint(lower, upper)) for _ in range(size)]
    return ls


def generate_random_number(lower, upper):
    return int(random.randint(lower, upper))
