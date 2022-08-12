from listnode import ListNode


class LinkedList:

    def __init__(self):
        self.head: ListNode = None

    def push_back(self, value):

        new_node: ListNode = ListNode(value)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return

        last: ListNode = self.head
        while last.next is not None:
            last = last.next

        new_node.next = last.next
        last.next = new_node

    def push_front(self, value):
        new_node: ListNode = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        n: ListNode = self.head
        while n is not None:
            print(n.value, end=' ')
            n = n.next
        print()
