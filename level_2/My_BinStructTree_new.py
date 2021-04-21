class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
                             # добавить новый узел левым потомком

class BST:

    def __init__(self, node=None):
        self.Root = node  # корень дерева, или None
        self.count_leaf = 0
        self.levels = 0

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind
        itemFind = BSTFind()
        if self.Root == None:
            return itemFind
        else:
            def find(node, key):
                if node.NodeKey < key and node.RightChild != None:
                    find(node.RightChild, key)
                elif node.NodeKey < key and node.RightChild == None:
                    itemFind.Node = node
                    itemFind.NodeHasKey = False
                    itemFind.ToLeft = False
                    return itemFind
                elif node.NodeKey > key and node.LeftChild != None:
                    find(node.LeftChild, key)
                elif node.NodeKey > key and node.LeftChild == None:
                    itemFind.Node = node
                    itemFind.NodeHasKey = False
                    itemFind.ToLeft = True
                    return itemFind
                else:
                    itemFind.Node = node
                    itemFind.NodeHasKey = True
                    return itemFind
                return itemFind
            return find(self.Root, key)

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        # false если ключ уже есть
        search_result = self.FindNodeByKey(key)
        if self.Root == None:
            newNode = BSTNode(key, val, None)
            self.Root = newNode
            return True
        elif search_result.NodeHasKey == True:
            return False
        elif search_result.NodeHasKey == False:
            if search_result.ToLeft == True:
                newNode = BSTNode(key, val, search_result.Node)
                search_result.Node.LeftChild = newNode
                newNode.Parent = search_result.Node
                return True
            else:
                newNode = BSTNode(key, val, search_result.Node)
                search_result.Node.RightChild = newNode
                newNode.Parent = search_result.Node
                return True

    def FinMinMax(self, FromNode, FindMax=False):
        # ищем максимальное/минимальное (узел) в поддереве
        if self.Root == None or FromNode == None:
            return None
        node = FromNode
        if FindMax == False:
            while node.LeftChild != None:
                node = node.LeftChild
            return node
        else:
            while node.RightChild != None:
                node = node.RightChild
            return node

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу если узел не найден
        if self.Root == None:
            return False
        else:
            def remove_leaf(del_node):  # функция удаления листа
                if del_node.Parent.LeftChild == del_node:
                    del_node.Parent.LeftChild = None
                    del_node.Parent = None
                else:
                    del_node.Parent.RightChild = None
                    del_node.Parent = None
                return True
            def remove_node_with_right_child(del_node): # функция удаления узла с одним правым потомком
                if del_node.Parent.LeftChild == del_node:
                    del_node.Parent.LeftChild = del_node.RightChild
                else:
                    del_node.Parent.RightChild = del_node.RightChild
                del_node.RightChild.Parent = del_node.Parent
                del_node.Parent = None
                del_node.RightChild = None
                return True
            def remove_node_with_left_child(del_node): # функция удаления узла с одним левым потомком
                if del_node.Parent.LeftChild == del_node:
                    del_node.Parent.LeftChild = del_node.LeftChild
                else:
                    del_node.Parent.RightChild = del_node.LeftChild
                del_node.LeftChild.Parent = del_node.Parent
                del_node.Parent = None
                del_node.LeftChild = None
                return True
            find_remove = self.FindNodeByKey(key)
            del_node = find_remove.Node
            if find_remove.NodeHasKey == False:
                return False
            elif del_node.Parent == None: # если удаляемый узел - корень
                self.Root = None
                return True
            elif del_node.RightChild == None and del_node.LeftChild == None:
                # если в удаляемом узле нет потомков
                return remove_leaf(del_node)
            elif (del_node.RightChild != None and del_node.LeftChild == None):
                # если в удаляемом узле есть один правый потомок
                return remove_node_with_right_child(del_node)
            elif (del_node.RightChild == None and del_node.LeftChild != None):
                # если в удаляемом узле есть один левый потомок
                return remove_node_with_left_child(del_node)
            elif (del_node.RightChild != None and del_node.LeftChild != None):
                # если в удаляемом узле есть оба потомка
                node = del_node.RightChild
                while True:
                    if (node.LeftChild == None and node.RightChild != None): # нашли узел только с правым потомком. Потомка перемещаем на место удаляемого
                        del_node.NodeKey = node.NodeKey
                        del_node.NodeValue = node.NodeValue
                        return remove_node_with_right_child(node)
                        #break

                    elif (node.LeftChild == None and node.RightChild == None):  # нашли лист. Его помещаем на место удаляемого узла.
                        del_node.NodeKey = node.NodeKey
                        del_node.NodeValue = node.NodeValue
                        return remove_leaf(node)
                        #break
                    node = node.LeftChild

    def Count(self):
        list_count = []
        if self.Root == None:
            return 0
        else:

            def find(node):
                # количество узлов в дереве
                list_count.append(1)
                if node.RightChild != None and node.LeftChild != None:
                    child = []
                    child.append(node.LeftChild)
                    child.append(node.RightChild)
                    for i in child:
                        find(i)
                elif node.RightChild != None and node.LeftChild == None:
                    find(node.RightChild)
                elif node.RightChild == None and node.LeftChild != None:
                    find(node.LeftChild)
                elif node.RightChild == None and node.LeftChild == None:
                    return list_count
                return list_count
            size = len(find(self.Root))
            return size

         
"""
My_BTS = BST()
My_BTS.AddKeyValue(70, 700)
My_BTS.AddKeyValue(93, 930)
My_BTS.AddKeyValue(31, 310)

rez = My_BTS.FindNodeByKey(92)

print('type', rez)

My_BTS.AddKeyValue(93, 930)
My_BTS.AddKeyValue(31, 310)
My_BTS.AddKeyValue(94, 940)
My_BTS.AddKeyValue(73, 730)
My_BTS.AddKeyValue(14, 140)
My_BTS.AddKeyValue(23, 230)
print("size: ", My_BTS.Count())
node_find = My_BTS.FindNodeByKey(93)
parent = node_find.Node.Parent
print('pointer from parent: ', node_find.Node.Parent.RightChild)
print('pointer on parent: ', node_find.Node.Parent)
print('pointer on child: ', node_find.Node.RightChild)
My_BTS.DeleteNodeByKey(93)
print('deleting')
print("size: ", My_BTS.Count())
print('pointer from parent: ', parent.RightChild)
print('pointer on parent: ', node_find.Node.Parent)
print('pointer on child: ', node_find.Node.RightChild)
print('key', node_find.Node.NodeKey)
print('key', node_find.Node.NodeValue)
"""

"""
My_BTS.AddKeyValue(93, 930)
My_BTS.AddKeyValue(31, 310)
My_BTS.AddKeyValue(94, 940)
My_BTS.AddKeyValue(73, 730)
My_BTS.AddKeyValue(14, 140)
My_BTS.AddKeyValue(23, 230)
"""
