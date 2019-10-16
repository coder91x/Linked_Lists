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


    def insert_after(self, prev_node, new_data):
        if prev_node == None:
            print("Element must be in Linked List")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        while self.head.next:
            self.head = self.head.next
        self.head = new_node

    def print_list(self):
        while self.head != None:
            print(self.head.data)
            self.head = self.head.next


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.append(9)
    l_list.push(7)
    l_list.push(5)
    l_list.push(3)
    l_list.insert_after(l_list.head.next , 8)

    l_list.print_list()



