class Node:
    def __init__(self, data):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp =self.head
        if temp is not None:
            if temp.data == key:
                temp.data = None
                self.head = temp.next
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None


    def printlist(self):
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(4)
    llist.push(3)
    llist.delete(5)
    llist.printlist()

