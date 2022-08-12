from helper import generate_random_number

from linkedlist import LinkedList


def generate_random_linked_list(size: int, lower: int, upper: int) -> LinkedList:
    linked_list = LinkedList()
    for i in range(size):
        number = generate_random_number(lower, upper)
        linked_list.push_back(number)
    return linked_list
