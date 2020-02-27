class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:

        def auto_size(L):
            n = 1
            for i in range(1, L+1):
                n = (n*2)+1
            return n
        tree_size = auto_size(depth)
        self.Tree = [None] * tree_size  # массив ключей


    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        q = []
        if self.Tree[0] == None:
            return None
        else:
            i = 0
            index = 0
            q.append(self.Tree[0])
            while len(q) != 0 or i < len(self.Tree):
                node = q.pop(0)
                if key < node and (i * 2) + 1 < len(self.Tree):
                    if self.Tree[(i * 2) + 1] != None:
                        q.append(self.Tree[(i * 2) + 1])
                        i = (i * 2) + 1
                    elif self.Tree[(i * 2) + 1] == None:
                        i = (i * 2) + 1
                        return -i
                elif key > node and (i * 2) + 1 < len(self.Tree):
                    if self.Tree[(i * 2) + 2] != None:
                        q.append(self.Tree[(i * 2) + 2])
                        i = (i * 2) + 2
                    elif self.Tree[(i * 2) + 2] == None:
                        i = (i * 2) + 2
                        return -i
                elif key == node:
                    return i
                else:
                    return None # не найден



    def AddKey(self, key):
        # добавляем ключ в массив
        if self.Tree[0] == None:
            self.Tree[0] = key
            return 0
        else:
            index = self.FindKeyIndex(key)
            if index != None:
                if index < 0:
                    index = index * (-1)
                    self.Tree[index] = key
                    return index
                elif index >= 0:
                    return index
            else:

                return -1

    def print_all(self):
        for i in self.Tree:
            print(i)
        # индекс добавленного/существующего ключа или -1 если не удалось
    
"""
a_bst = aBST(3)

a_bst.AddKey(50)
a_bst.AddKey(25)
a_bst.AddKey(75)
a_bst.AddKey(37)
a_bst.AddKey(62)
a_bst.AddKey(84)
a_bst.AddKey(31)
a_bst.AddKey(43)
a_bst.AddKey(55)
a_bst.AddKey(92)
a_bst.AddKey(100)
a_bst.print_all()

find_result = a_bst.FindKeyIndex(100)
print('type find_result', find_result)

"""