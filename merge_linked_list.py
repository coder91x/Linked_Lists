class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        while self.head.next is not None:
            self.head = self.head.next
            self.head = new_node

    def insert_after(self, prev_node ,new_data):
        if prev_node is None:
            print('Element should be present in Linked List')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

def sorted_merge(head1, head2):
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = sorted_merge(head1.next, head2)
    else:
        temp = head2
        temp.next = sorted_merge(head1, head2.next)
    return temp

if __name__ == '__main__':
    list1 = Linked_List()
    list2 = Linked_List()
    list1.append(8)
    list1.append(6)
    list1.push(5)
    list1.push(2)
    list2.append(10)
    list2.push(4)
    list2.push(1)
    list2.insert_after(list2.head,2)
    list3 = Linked_List()
    list3.head = sorted_merge(list1.head, list2.head)
    list3.printlist()




