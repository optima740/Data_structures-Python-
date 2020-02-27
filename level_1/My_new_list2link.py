class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

class LinkedList2:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.next = None
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            self.head.prev = None
            self.head.next = None
            self.tail = item
        else:
            tmp = self.head
            self.head.prev = item
            self.head = item
            item.next = tmp
            item.prev = None

    def delete_to(self, node_del):

        node_prev = node_del.prev
        node_next = node_del.next
        if node_prev != None and node_next != None:
            node_prev.next = node_del.next
            node_next.prev = node_prev
        elif node_prev == None and node_next != None:
            self.head = node_del.next
            self.head.prev = None
        elif node_prev != None and node_next == None:
            self.tail = node_del.prev
            self.tail.next = None
        elif node_prev == None and node_next == None:
            self.head = None
            self.tail = None
        return

    def delete(self, val, all=False):
        if self.len() != 0:
            if (all ==False):
                node_del = self.find(val)
                if node_del !=None:
                    self.delete_to(node_del)
                else:
                    return None
            else:
                node_del = self.find_all(val)
                if node_del != None:
                    for node in node_del:
                        self.delete_to(node)
                else:
                    return None
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
        if len(list_out)!=0:
            return list_out
        else:
            return None




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

        if self.len() == 0 and afterNode==None:
            self.add_in_head(newNode)
            return
        elif self.len() !=0 and afterNode==None:
            self.add_in_tail(newNode)
            return
        elif self.len() != 0 and afterNode != None:

            node_next = afterNode.next

            if node_next!=None:
                afterNode.next = newNode
                node_next.prev = newNode
                newNode.next = node_next

                newNode.prev = afterNode
            elif node_next == None:
                afterNode.next = newNode
                self.tail = newNode
                newNode.next = None
                newNode.prev = afterNode
            return




"""
my_list = LinkedList2()

my_list.add_in_head(Node(99))


my_list.add_in_tail(Node(101))

#my_list.add_in_tail(Node(100))
node = my_list.find(1)
my_list.insert(node, Node(1111))

#my_list.add_in_head(Node(98))
#my_list.delete(100)
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