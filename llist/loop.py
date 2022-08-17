from llist.linkedlist import (
    LinkedList,
    ListNode
)


def detect_loop_naive(llist: LinkedList):
    memo = set()

    n = llist.head

    while n is not None:
        if n in memo:
            return True
        memo.add(n)
        n = n.next
    
    return False


def detect_loop(llist: LinkedList):

    slow, fast = llist.head, llist.head

    while slow and fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():

    llist = LinkedList()

    llist.push_back(12)
    llist.push_back(10)

    # # make loop
    # list.head.next.next = llist.head.next

    naive = detect_loop_naive(llist)
    print(naive)

    loop = detect_loop(llist)
    print(loop)


main()
