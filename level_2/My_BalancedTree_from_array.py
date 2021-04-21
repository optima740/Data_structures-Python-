class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла

class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком

class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

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

    def AddKey(self, key):
        # добавляем ключ-значение в дерево
        # false если ключ уже есть
        search_result = self.FindNodeByKey(key)
        if self.Root == None:
            newNode = BSTNode(key, None)
            self.Root = newNode
            newNode.Level = 1
            return True
        elif search_result.NodeHasKey == True:
            return False
        elif search_result.NodeHasKey == False:
            if search_result.ToLeft == True:
                newNode = BSTNode(key, search_result.Node)
                search_result.Node.LeftChild = newNode
                newNode.Parent = search_result.Node
                newNode.Level = search_result.Node.Level + 1
                return True
            else:
                newNode = BSTNode(key, search_result.Node)
                search_result.Node.RightChild = newNode
                newNode.Parent = search_result.Node
                newNode.Level = search_result.Node.Level + 1
                return True

    def GenerateTree(self, a):
        # создаём сбалансирование дерево с нуля из неотсортированного массива a
        if len(a) == 0:
            return
        else:
            #My_balancedBST = BalancedBST()
            a.sort()
            q = []
            q.append(a)
            def gen_tree():
                while len(q) != 0:
                    tmp = q.pop(0)
                    center = len(tmp) // 2
                    self.AddKey(tmp[center])
                    # a.remove(tmp[center])
                    if len(tmp) > 3:
                        q.append(tmp[0:center])
                        q.append(tmp[center + 1: (center + center) + 1])
                        gen_tree()
                return
            gen_tree()
            for i in range(0, len(a), 2):
                self.AddKey(a[i])

    def IsBalanced(self, root_node):
        # сбалансировано ли дерево с корнем root_node
        if root_node == None:
            return False
        else:
            deep = [0, 0]
            def find(node, deep):
                if node.RightChild != None  and  node.LeftChild != None:

                    deep[0] = node.LeftChild.Level
                    deep[1] = node.RightChild.Level
                    child = []
                    child.append(node.LeftChild)
                    child.append(node.RightChild)
                    for i in child:
                        find(i, deep)

                elif node.RightChild != None and node.LeftChild == None:
                    deep[1] = node.RightChild.Level
                    return deep
                elif node.RightChild == None and node.LeftChild != None:
                    deep[0] = node.LeftChild.Level
                    return deep
                elif node.RightChild == None and node.LeftChild == None:
                    return deep
                return deep

            result = find(root_node, deep)
            if (result[0] == result[1]) or abs(result[0] - result[1]) == 1:
                return True
            else:
                return False
                
    def  GetAllNodes(self):
        q = []
        list_all = []
        if self.Root == None:
            return list_all
        else:
            q.append(self.Root)
            while len(q) != 0:
                node = q.pop(0)
                list_all.append(node)
                if node.LeftChild != None:
                    q.append(node.LeftChild)
                if node.RightChild != None:
                    q.append(node.RightChild)
            return list_all

"""
a = [70, 10, 14, 15, 97, 71, 33, 32, 31, 35, 93, 73, 76, 94, 95]
#a = [70, 10, 14, 15, 71, 33, 32, 31, 35, 93, 73, 76, 94, 97, 95]
#a = [70,14,33,73,31,93,95]
#a = [70,70,70,70,70,70,70]

my_tree = BalancedBST()
my_tree.GenerateTree(a)
all = my_tree.GetAllNodes()
for i in all:
    print(i.NodeKey)
print(my_tree.IsBalanced(my_tree.Root.RightChild.RightChild.RightChild))

#print(my_tree.PrintAllNodes())

"""

