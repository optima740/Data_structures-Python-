class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def str_to_int(self, value):
        value = str(value).strip()
        sum = 0
        for i in value:
            sum = sum + ord(i)
        return sum

    def hash_fun(self, value):
        return self.str_to_int(value) % self.size
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
    def seek_slot(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size - 1:
            if self.slots[index] == None:
                return index
            if index + self.step > self.size-1:
                index = (index+self.step) - (self.size)
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
        while count <= self.size-1:
            if self.slots[find_index] == value:
                return find_index
            if find_index + self.step > self.size-1:
                find_index = (find_index+self.step) - (self.size)
            else:
                find_index += self.step
            count += 1
        return


        # находит индекс слота со значением, или None
ht = HashTable(9,3)

ht.put('aa')
ht.put('aaa')
ht.put('baa')
ht.put('bbbbbb')
ht.put('cbcbcb')
ht.put('cccc')
ht.put('hh')
ht.put('z')
ht.put('pppp')
print(ht.find('bbbbbb'))
print(ht.find('z'))
print(ht.find('aa'))
print('stop')
