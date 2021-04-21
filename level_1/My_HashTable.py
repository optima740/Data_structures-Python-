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
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        return self.str_to_int(value) % self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
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
        return None

    def put(self, value):
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить
        value = str(value).strip()
        index_put = self.seek_slot(value)
        if index_put != None:
            self.slots[index_put] = value
            return index_put
        else:
            return None
        
    def find(self, value):
        # находит индекс слота со значением, или None
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
