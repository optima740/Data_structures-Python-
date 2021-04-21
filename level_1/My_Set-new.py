class PowerSet:

    def __init__(self):
        self.size_n = 20000
        self.slots = dict((None, None) for x in range(self.size_n))
        self.size_count = 0

    def size(self):
        # количество элементов в множестве
        return self.size_count       

    def seek_slot(self, value):
        index_value = self.slots.get(value)
        if index_value != None:
            return index_value
        else:
            return None

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        index_value = self.seek_slot(value)
        if index_value != None:
            return True
        else:
            return False        

    def put(self, value):
        # всегда срабатывает
        carrent_value = self.seek_slot(value)
        if carrent_value != value:
            self.slots[value] = value
            self.size_count += 1      

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        index_value = self.get(value)
        if index_value:
            self.slots.pop(value)
            self.size_count -= 1
            return True
        else:
            return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        set3 = PowerSet()
        key1 = self.slots.keys()
        for i in key1:
            val = set2.seek_slot(i)
            if val and val != None:
                set3.put(val)
        return set3

    def union(self, set2):
        # объединение текущего множества и set2
        set3 = PowerSet()
        key1 = self.slots.keys()
        key2 = set2.slots.keys()
        for i in key1:
            if i != None:
                set3.put(i)
        for i in key2:
            if i != None:
                set3.put(i)
        return set3

    def difference(self, set2):
        # разница текущего множества и set2
        set3 = PowerSet()
        key1 = self.slots.keys()
        for i in key1:
            if i != None and set2.get(i) == False:
                set3.put(i)
        return set3

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        key2 = set2.slots.keys()
        for i in key2:
            if i != None and self.get(i) == False:
                return False
        return True

"""
set1 = PowerSet()
set2 = PowerSet()

set1.put('789')
set1.put('888')
set1.put('987')
set1.put('879')


set1.remove('789')

set1.remove('888')
set1.remove('987')
set1.remove('879')
set1.remove('8791234')


print("ok")


set2.put('aaa')
set2.put('azz')
set2.put('azzyuio')
set2.put('ab___m')
set2.put('789')

set1.issubset(set2)
print(set1.size())
"""
