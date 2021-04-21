class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

class SimpleTree:
    def __init__(self, root=None):
        self.Root = root  # корень, может быть None
        self.count_leaf = 0
        self.levels = 0

    def AddChild(self, ParentNode, NewChild):
        if ParentNode == None and self.Root == None:
            self.Root = NewChild
            self.Root.Parent = None
        elif ParentNode == None and self.Root != None:
            NewChild.Parent = None
            self.Root.Parent = NewChild
            temp_root = self.Root
            self.Root = NewChild
            self.Root.Children.append(temp_root)
        elif ParentNode != None:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode
        # код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == self.Root:
            self.Root = None
        else:
            temp_parent = NodeToDelete.Parent
            for i in temp_parent.Children:
                if i == NodeToDelete:
                    temp_parent.Children.remove(i)
            NodeToDelete.Parent = None
        # код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        list_all_nodes = []
        if self.Root == None:
            return []
        elif len(self.Root.Children) == 0:
            list_all_nodes.append(self.Root)
            return list_all_nodes
        else:
            def find(struct):
                list_all_nodes.append(struct)
                if len(struct.Children) > 0:
                    for child in struct.Children:
                        find(child)
                return list_all_nodes
            return find(self.Root)
        # код выдачи всех узлов дерева в определённом порядке

    def FindNodesByValue(self, val):
        if self.Root == None:
            return []
        else:
            list_find_nodes = []
            def find(struct, val):
                if len(struct.Children) > 0 and struct.NodeValue != val:
                    for child in struct.Children:
                        if child.NodeValue == val:
                            list_find_nodes.append(child)
                            return list_find_nodes
                        find(child, val)
                elif struct.NodeValue == val:
                    list_find_nodes.append(struct)
                    return list_find_nodes
                else:
                    return []
            find(self.Root, val)
            return list_find_nodes
        # ваш код поиска узлов по значению

    def MoveNode(self, OriginalNode, NewParent):
        if len(self.Root.Children) == 0 or OriginalNode == self.Root or self.Count() == 0:
            return
        else:
            temp_parent = OriginalNode.Parent
            for child in temp_parent.Children:
                if child == OriginalNode:
                    temp_parent.Children.remove(child)
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

        # код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent

    def Count(self):
        list_count = []
        if self.Root == None:
            return 0
        else:
            def find(struct):
                list_count.append(1)
                if len(struct.Children) > 0:
                    for node in struct.Children:
                        find(node)
                return list_count
            size = len(find(self.Root))
            return size
        # количество всех узлов в дереве

    def LeafCount(self):
        if self.Root == None:
            return 0
        elif len(self.Root.Children) == 0:
            return 1
        else:
            def find(struct, count):
                if len(struct.Children) > 0:
                    for child in struct.Children:
                        count = find(child, count)
                else:
                    count += 1
                return count
            return find(self.Root, self.count_leaf)
        # количество листьев в дереве
    def GetLevel(self):
        if self.Root == None:
            return 0
        elif len(self.Root.Children) == 0:
            return 1
        list_current_nods = self.GetAllNodes()
        list_count = []
        for node in list_current_nods:
            count = 0
            while node.Parent != None:
                node = node.Parent
                count += 1
            list_count.append(count)
        return max(list_count)


