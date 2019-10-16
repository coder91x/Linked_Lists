class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverselist(self):
        while self.head != None:
            print(f"{self.head.data}")
            self.head = self.head.next

if __name__ == '__main__':
    llist1 = LinkedList()
    llist1.head = Node("Aniruddha")
    second = Node("is")
    third = Node("a")
    fourth = Node("crazy")
    fifth = Node("boy")
    llist1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    llist1.traverselist()



