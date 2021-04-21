class NativeCache:
    
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.len_table = 0

    def str_to_code(self, key):
        key = str(key).strip()
        sum = 0
        for i in key:
            sum = sum + ord(i)
        return sum

    def hash_fun(self, key):
         # в качестве key поступают строки!
         # всегда возвращает корректный индекс слота
        return self.str_to_code(key) % self.size

    def put(self, key, value):
         # гарантированно записываем
         # значение value по ключу key и возвращает индекс
        index = self.hash_fun(key)
        if (self.slots[index] != None and self.slots[index] == key) or (self.slots[index] == None):  #если в слоту такой же ключ либо слот пустой
            self.slots[index] = key
            self.values[index] = value
            return index
        elif self.slots[index] != None and self.slots[index] != key:  # если слот не пустой и в слоту другой ключ
            count = 0
            while count < self.size:
                if index + 1 <= self.size - 1:
                    index += 1
                else:
                    index = 0
                if self.slots[index] == None or self.slots[index] == key:
                    self.slots[index] = key
                    self.values[index] = value
                    return
                count += 1

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        index = self.hash_fun(key)
        if self.slots[index] != key:
            count = 0
            while count < self.size:
                if index + 1 <= self.size-1:
                    index += 1
                elif index + 1 > self.size-1:
                    index = 0
                if self.slots[index] == key:
                    return True
                count += 1
            return False
        else:
            return True

    def get(self, key):
        if self.is_key(key) == True:
            index = self.hash_fun(key)
            if self.slots[index] == key:
                return self.values[index]
            while self.slots[index] != key:
                if index + 1 <= self.size-1:
                    index += 1
                else:
                    index = 0
            return self.values[index]
        else:
            return

    def index_for_key(self, key):
        index_key = self.slots.index(key)
        if index_key != None:
            return index_key
        else:
            return

    def remove_item(self, index):
        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0
        self.len_table -= 1

    def add_to_cache(self, key, value):
        if self.len_table < self.size and self.is_key(key) == False:   #если кэш не заполнен до конца и ключа еще нет в кэше
            self.put(key, value)
            self.len_table += 1
            return
        elif self.len_table == self.size and self.is_key(key) == False:  #если кэш заполнен и ключа еще нет в кэше
            index = self.hits.index(min(self.hits))
            self.remove_item(index)
            self.slots[index] = key
            self.values[index] = value
            self.len_table += 1
            return
        self.put(key, value)       #если ключ уже существует

    def get_from_cache(self, key):
        if self.is_key(key):
            self.hits[self.index_for_key(key)] += 1
            return self.get(key)
        else:
            return
import unittest

class My_tests(unittest.TestCase):

    def test_add(self):
        c = NativeCache(10)
        for i in range(10):
            c.add_to_cache(i, 'vol' + str(i))
        self.assertEqual(c.len_table, 10, 'incorrect len_table')
        c = NativeCache(10)
        c.add_to_cache('123', 100)
        c.add_to_cache('234', 101)
        c.add_to_cache('345', 102)
        c.add_to_cache('456', 103)
        c.add_to_cache('567', 104)
        c.add_to_cache('678', 105)
        c.add_to_cache('789', 106)
        c.add_to_cache('890', 107)
        c.add_to_cache('901', 108)
        c.add_to_cache('012', 109)

        c.add_to_cache('111', 11)
        c.add_to_cache('222', 12)
        c.add_to_cache('333', 13)
        c.add_to_cache('444', 14)
        c.add_to_cache('555', 15)
        c.add_to_cache('666', 16)
        c.add_to_cache('777', 17)
        c.add_to_cache('888', 18)
        c.add_to_cache('999', 19)
        c.add_to_cache('000', 20)

    def test_get(self):
        c = NativeCache(10)
        c.add_to_cache('123', 100)
        c.add_to_cache('234', 101)
        c.add_to_cache('345', 102)
        c.add_to_cache('456', 103)
        c.add_to_cache('567', 104)
        c.add_to_cache('678', 105)
        c.add_to_cache('789', 106)
        c.add_to_cache('890', 107)
        c.add_to_cache('901', 108)
        c.add_to_cache('012', 109)

        c.get_from_cache('123')
        c.get_from_cache('234')
        c.get_from_cache('345')
        c.get_from_cache('456')
        c.get_from_cache('456')
        c.get_from_cache('567')
        c.get_from_cache('567')
        c.get_from_cache('567')
        c.get_from_cache('678')
        c.get_from_cache('789')
        c.get_from_cache('890')
        c.get_from_cache('012')

        self.assertEqual(min(c.hits), 0, 'incorrect min item from list hits')
        self.assertEqual(max(c.hits), 3, 'incorrect man item from list hits')
        index_min = c.hits.index(min(c.hits))
        value_remove = c.values[index_min]
        self.assertEqual(value_remove, 108, 'incorrect remove slots')

        c.add_to_cache('091', 1000)
        self.assertEqual(c.values[index_min], 1000, 'incorrect add after remove')
        self.assertEqual(c.hits.index(min(c.hits)), 4, 'incorrect min item from list hits')
        c.get_from_cache('091')
        c.get_from_cache('091')
        c.get_from_cache('091')
        c.get_from_cache('091')
        self.assertNotEqual(c.hits.index(min(c.hits)), 4, 'incorrect index min item after get')
        self.assertEqual(max(c.hits), 4, 'incorrect max item after get from list hits')


        print('slots:{}'.format(c.slots))
        print('values:{}'.format(c.values))
        print('hits:{}'.format(c.hits))

test = My_tests()
test.test_add()
test.test_get()

