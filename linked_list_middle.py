class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def middle(self):
        slow = self.head
        fast = self.head
        prev = self.head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast is not None:
            return slow.data
        else:
            return (slow.data + prev.data)/2

if __name__ == '__main__':
     llist = LinkedList()
     llist.head = Node(1)
     second = Node(2)
     third = Node(3)
     fourth = Node(4)
     fifth = Node(5)
     #sixth = Node(6)
     llist.head.next = second
     second.next = third
     third.next = fourth
     fourth.next = fifth
     #fifth.next = sixth
     middle = llist.middle()
     print(middle)