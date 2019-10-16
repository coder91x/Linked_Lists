class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_position(self, position):
        temp = self.head
        if temp is not None:
            if position == 0:
                self.head = temp.next
                temp.data = None
                return


            for i in range(position-1):
                temp = temp.next
                if temp is None:
                    break
            if temp is None:
                return
            if temp.next is None:
                    return
            next = temp.next.next
            temp.next = None
            temp.next = next

    def printlist(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(8)
    llist.push(9)
    llist.push(10)
    llist.delete_at_position(3)
    llist.printlist()

