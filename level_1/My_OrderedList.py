class Node:
    
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        if v1 == v2:
            return 0
        elif v1 < v2:
            return -1
        else:
            return 1

    def add(self, value):
        n = Node(value)
        if self.head != None:
            node = self.head
            while node != None:
                if self.compare(node.value, value) == 0: # элемент который равен вставке
                    if node.next != None:
                        tmp_node_next = node.next
                        node.next = n
                        n.next = tmp_node_next
                        tmp_node_next.prev = n
                        n.prev = node
                        return
                    else:
                        node.next = n
                        n.next = None
                        n.prev = node
                        self.tail = n
                        return
                elif self.compare(node.value, value) > 0 and (self.__ascending == True):  # элемент который больше чем вставка (возрастание)
                    if node.prev != None:
                        tmp_node_prev = node.prev
                        tmp_node_prev.next = n
                        n.next = node
                        node.prev = n
                        n.prev = tmp_node_prev
                        return
                    else:
                        node.prev = n
                        n.prev = None
                        n.next = node
                        self.head = n
                        return
                elif self.compare(node.value, value) < 0 and (self.__ascending == False): # элемент который меньше чем вставка (убывание)
                    if node.prev != None:
                        tmp_node_prev = node.prev
                        tmp_node_prev.next = n
                        n.next = node
                        node.prev = n
                        n.prev = tmp_node_prev
                        return
                    else:
                        node.prev = n
                        n.prev = None
                        n.next = node
                        self.head = n
                        return
                node = node.next
            # вставка больше или меньше чем все элементы - вставляем в конец
            tmp_node_prev = self.tail
            tmp_node_prev.next = n
            n.next = None
            n.prev = tmp_node_prev
            self.tail = n
        else:
            self.head = n
            self.tail = n
            n.next = None
            n.prev = None

    def find(self, val):
        if self.__ascending == True:
            node = self.head
            while node != None:
                if node.value > val:
                    return
                elif node.value == val:
                    return node
                node = node.next
        else:
            node = self.head
            while node != None:
                if node.value < val:
                    return
                elif node.value == val:
                    return node
                node = node.next

    def delete(self, val):
        if self.len() > 0:
            node = self.find(val)
            if node != None and node.next != None and node.prev != None:
                tmp_next_node = node.next
                tmp_prev_node = node.prev
                tmp_prev_node.next = tmp_next_node
                tmp_next_node.prev = tmp_prev_node
                del(node)
                return
            elif node != None and node.next == None and node.prev != None:
                tmp_prev_node = node.prev
                tmp_prev_node.next = None
                self.tail = tmp_prev_node
                del(node)
                return
            elif node != None and node.next != None and node.prev == None:
                tmp_next_node = node.next
                self.head = tmp_next_node
                tmp_next_node.prev = None
                del(node)
                return
            elif node != None and node.next == None and node.prev == None:
                self.head = None
                self.tail = None
                del(node)
                return
            else:
                return
        else:
            return

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        str1 = str(v1).strip()
        str2 = str(v2).strip()

        if len(str1) > 0 and len(str2) > 0:
            if str1 < str2:
                return -1
            elif str1 == str2:
                return 0
            else:
                return 1
        elif len(str1) == 0 and len(str2) > 0:
            return -1
        elif len(str1) == 0 and len(str2) == 0:
            return 0
        elif len(str1) > 0 and len(str2) == 0:
            return 1



"""
ol = OrderedStringList(True)
ol.add('aaa')
ol.add(' ')
ol.add('aab')
ol.add('abc')
ol.add('      ')



ol.delete('abc')
ol.print_all_nodes()
"""




