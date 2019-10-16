class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    list = Linked_List()
    list.push(8)
    list.push(7)
    list.push(2)
    list.reverse_list()
    list.printlist()

