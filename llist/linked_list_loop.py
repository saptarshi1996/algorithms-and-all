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


def detect_loop_optimized(linked_list: LinkedList) -> bool:

    slow, fast = linked_list.head, linked_list.head

    while slow and fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():

    linked_list: LinkedList = generate_random_linked_list(100, 1000, 2000)

    # make loop in the linked list
    linked_list.head.next.next.next.next = linked_list.head.next.next

    loop = detect_loop_optimized(linked_list)
    print(loop)


main()
