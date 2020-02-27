# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class HashTable:
    def __init__(self, sz, stp):
        self.size_n = sz
        self.step = stp
        self.slots = [None] * self.size_n

    def str_to_int(self, value):
        value = str(value).strip()
        sum = 0
        for i in value:
            sum = sum + ord(i)
        return sum

    def hash_fun(self, value):
        return self.str_to_int(value) % self.size_n
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
    def seek_slot(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size_n - 1:
            if self.slots[index] == None:
                return index
            if index + self.step > self.size_n-1:
                index = (index+self.step) - (self.size_n)
            else:
                index += self.step
            count += 1
        # находит индекс пустого слота для значения, или None
        return None

    def put(self, value):
        value = str(value).strip()
        index_put = self.seek_slot(value)
        if index_put != None:
            self.slots[index_put] = value
            return index_put

        else:
            return None
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить

    def find(self, value):
        value = str(value).strip()
        find_index = self.hash_fun(value)
        count = 0
        while count <= self.size_n-1:
            if self.slots[find_index] == value:
                return find_index
            if find_index + self.step > self.size_n-1:
                find_index = (find_index+self.step) - (self.size_n)
            else:
                find_index += self.step
            count += 1
        return
        # находит индекс слота со значением, или None

class PowerSet(HashTable):

    def __init__(self):
        super(PowerSet, self).__init__(20000, 1)
        self.util_index = []
        self.size_count = 0
    def size(self):

        return self.size_count
        # количество элементов в множестве
    def seek_slot(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size_n - 1:
            if self.slots[index] == None or self.slots[index] == value:
                return index

            if index + self.step > self.size_n-1:
                index = (index+self.step) - (self.size_n)
            else:
                index += self.step
            count += 1
        # находит индекс пустого слота для значения, или индекс слота с таким-же значением, и возвращает этот индекс, или None - в противном случае.
        return None

    def put(self, value):
        value = str(value).strip()
        index_put = self.seek_slot(value)
        if index_put != None and self.slots[index_put] == value:
            self.slots[index_put] = value
        elif index_put != None:
            self.slots[index_put] = value
            self.size_count += 1
            self.util_index.append(index_put)
            return index_put
        else:
            return None
        # всегда срабатывает

    def get(self, value):
        value = str(value).strip()
        index_get = self.seek_for_del(value)
        if index_get != None and self.slots[index_get] == value:
            return True
        else:

            return False
        # возвращает True если value имеется в множестве,
        # иначе False
    def seek_for_del(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size_n - 1:
            if  self.slots[index] == value:
                return index
            if index + self.step > self.size_n - 1:
                index = (index + self.step) - (self.size_n)
            else:
                index += self.step
            count += 1
        return None

    def remove(self, value):
        value = str(value).strip()
        if self.get(value):
            index_remove = self.seek_for_del(value)
            if index_remove!= None and self.slots[index_remove] == value:
                self.slots[index_remove] = None
                self.size_count -= 1
                self.util_index.remove(index_remove)
                return True
            else:
                return False
        else:
            return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value):
                set3.put(value)
        return set3

    def union(self, set2):
        # объединение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            set3.put(value)
        for i in set2.util_index:
            value = set2.slots[i]
            set3.put(value)
        return set3

    def difference(self, set2):
        # разница текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value) == False:
                set3.put(value)
        return set3

    def issubset(self, set2):
        for i in set2.util_index:
            value = set2.slots[i]
            if self.get(value) == False:
                return False
        return True
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
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