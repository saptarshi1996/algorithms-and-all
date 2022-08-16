from llist.linkedlist import (
    ListNode,
    LinkedList,
)

def reverse_recursive_helper(current, prev):

    if current is None:
        return prev

    next_node = current.next
    current.next = prev

    return reverse_recursive_helper(next_node, current)

def reverse_recursive(head: ListNode):
    return reverse_recursive_helper(head, None)

def reverse_iterative(head: ListNode):
    current = head
    prev, next_node = None, None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

def main():

    llist = LinkedList()

    llist.push_back(32)
    llist.push_back(10)
    llist.push_back(12)
    llist.push_back(18)
    llist.push_back(20)

    llist.push_front(21)

    llist.print_list()

    llist.head = reverse_iterative(llist.head)
    llist.print_list()

    llist.head = reverse_recursive(llist.head)
    llist.print_list()

main()
