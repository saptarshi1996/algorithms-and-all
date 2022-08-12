from llist.linkedlist import LinkedList
from llist.listnode import ListNode


def reverse_list_recursive_helper(current: ListNode, prev: ListNode):

    if current is None:
        return prev

    next_node = current.next
    current.next = prev
    return reverse_list_recursive_helper(next_node, current)


def reverse_list_recursive(head: ListNode):
    return reverse_list_recursive_helper(head, None)


def reverse_list_iterative(head: ListNode):

    current = head
    prev, next_node = None, None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def main():

    linked_list = LinkedList()

    linked_list.push_back(2)
    linked_list.push_back(10)
    linked_list.push_back(7)
    linked_list.push_back(5)
    linked_list.push_back(12)
    linked_list.push_back(9)

    linked_list.print_list()

    result = reverse_list_iterative(linked_list.head)
    linked_list.head = result

    linked_list.print_list()

    result_recursive = reverse_list_recursive(linked_list.head)
    linked_list.head = result_recursive

    linked_list.print_list()


if __name__ == '__main__':
    main()