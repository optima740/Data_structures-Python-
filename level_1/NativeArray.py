class NativeDictionary:
    
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

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
        # значение value по ключу key
        index = self.hash_fun(key)
        if self.slots[index] != None and self.slots[index] != key:
            count = 0
            while count < self.size:
                if index + 1 <= self.size-1:
                    index += 1
                else:
                    index = 0
                if self.slots[index] == None or self.slots[index] == key:
                    self.slots[index] = key
                    self.values[index] = value
                    return
                count += 1
            return print('Prevyshen RAZMER')
        elif self.slots[index] != None and self.slots[index] == key:
            self.slots[index] = key
            self.values[index] = value
            return
        elif self.slots[index] == None:
            self.slots[index] = key
            self.values[index] = value
            return
         
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
        # возвращает value для key,
        # или None если ключ не найден
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
         

"""
na = NativeDictionary(11)
na.put('aaa', 100)
na.put('bb', 1000)
na.put('333', 99)
na.put('cccc', 1001)
na.put('abc', 1)
na.put('999', 0)
na.put('qwerty', 123)
na.put('_wert_', 321)
na.put('vvv', 777)
na.put('pppp', 222)
na.put('z', 111)
"""





