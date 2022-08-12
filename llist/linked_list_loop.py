from linkedlist import LinkedList
from llist_helper import generate_random_linked_list
from listnode import ListNode


def detect_loop(linked_list: LinkedList) -> bool:

    memo = set()

    head: ListNode = linked_list.head

    while head is not None:
        if head in memo:
            return True
        memo.add(head)
        head = head.next

    return False


def main():

    linked_list: LinkedList = generate_random_linked_list(100, 1000, 2000)

    linked_list.head.next.next.next.next = linked_list.head.next.next

    loop = detect_loop(linked_list)
    print(loop)


main()
