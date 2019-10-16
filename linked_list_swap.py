class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def swap(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX is None or currY is None:
            return

        if prevX is not None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY is not None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp


    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    list = LinkedList()
    list.push(8)
    list.push(9)
    list.push(12)
    list.push(45)
    list.swap(45,12)
    list.print_list()


