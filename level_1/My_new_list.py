class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            self.head.next = None
            self.tail = item
        else:
            tmp = self.head
            self.head = item
            self.head.next = tmp

    def delete(self, val, all=False):
        if self.len() != 0:
            node = self.head
            prev = None
            while node != None:
                if node.value == val:
                    if prev != None:
                        tmp = node.next
                        del(node)
                        prev.next = tmp
                        node = tmp
                        if tmp == None:
                            self.tail = prev
                    else:
                        tmp = node.next
                        del(node)
                        self.head = tmp
                        node = tmp
                        if tmp == None:
                            self.tail = tmp
                    if (all == False):
                        return
                else:
                    prev = node
                    node = node.next
        else:
            return

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        list_out = []
        node = self.head
        while node is not None:
            if node.value == val:
                list_out.append(node)
            node = node.next
        return list_out

    def clean(self):
        if self.len()!=0:
            node = self.head
            while node != None:
                tmp = node.next
                del(node)
                self.head = tmp
                node = self.head
            #self.head = None
            if self.len()==0:
                self.tail = None
                return
        else:
            return

    def len(self):
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while node != None:
                count+=1
                node = node.next
            return count

    def insert(self, afterNode, newNode):
        if self.len() == 0 or self.head == None or afterNode==None:
            self.add_in_head(newNode)
            return
        if afterNode != None:
            node = afterNode
            tmp = node.next
            if tmp!=None:
                node.next = newNode
                newNode.next = tmp
            else:
                node.next = newNode
                self.tail = newNode
                newNode.next = None




"""
my_list = LinkedList()
my_list.add_in_head(Node(98))
my_list.add_in_head(Node(97))
my_list.add_in_head(Node(96))
my_list.add_in_head(Node(96))
my_list.add_in_head(Node(96))
my_list.print_all_nodes()
print(my_list.len())
p = my_list.find_all(96)
print(p)

my_list.delete(98)
my_list.print_all_nodes()
print(my_list.len())
findNode = my_list.find(97)
my_list.insert(findNode, Node(1111))
my_list.delete(1111)
my_list.print_all_nodes()
print(my_list.len())

my_list.add_in_tail(Node(99))
my_list.add_in_tail(Node(100))
my_list.add_in_tail(Node(103))
my_list.print_all_nodes()
print(my_list.len())
#my_list.clean()
my_list.print_all_nodes()
print(my_list.len())
my_list.add_in_tail(Node(10333))
#p = my_list.find_all(100)
#print(p)
findNode = my_list.find(103)
my_list.insert(findNode, Node(1111))
my_list.print_all_nodes()
print(my_list.len())
my_list.clean()
my_list.add_in_tail(Node(12345))
my_list.print_all_nodes()
print(my_list.len())
"""
