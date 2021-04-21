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
        # индекс добавленного/существующего ключа или -1 если не удалось
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

def My_Log(y):
    base = 2
    degree = 0
    while y != int(round(base ** degree)):
        degree += 0.5
    return int(round(degree))

def GenerateBBSTArray(a):
    if len(a) == 0:
        My_BSTarray = aBST(0)
        return My_BSTarray
    else:
        depth = (My_Log(len(a)+1)) - 1
        My_BSTarray = aBST(depth)
        a.sort()
        q = []
        q.append(a)
        def gen_tree():
            while len(q) != 0:
                tmp = q.pop()
                center = len(tmp) // 2
                My_BSTarray.AddKey(tmp[center])
                #a.remove(tmp[center])
                if len(tmp) > 3:
                    q.append(tmp[0:center])
                    q.append(tmp[center + 1: (center+center) +1 ])
                    gen_tree()
            return
        gen_tree()
        for i in range(0, len(a), 2):
            My_BSTarray.AddKey(a[i])
        return My_BSTarray.Tree

#a = [70, 10, 14, 15, 97, 71, 33, 32, 31, 35, 93, 73, 76, 94, 95]
a = [70,14,33,73,31,93,95]
#a = [70,70,70,70,70,70,70]
array_tree = GenerateBBSTArray(a)
print(type(array_tree))
for i in array_tree:
    print(i)
"""
"""
