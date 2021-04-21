import bitarray as bit

class BloomFilter:

    def __init__(self, f_len):
        # создаём битовый массив длиной f_len ...
        self.filter_len = f_len
        self.bit_array = bit.bitarray()
        for i in range(self.filter_len):
            self.bit_array.append(0)

    def hash1(self, str1):
        # 17
        code = 0
        for c in str1:
            code = ((code * 17) + ord(c)) % self.filter_len
        return code

    def hash2(self, str1):
        # 223
        code = 0
        for c in str1:
            code = ((code * 223) + ord(c)) % self.filter_len
        return code

    def add(self, str1):
        # добавляем строку str1 в фильтр
        str1 = str(str1).strip()
        self.bit_array[self.hash1(str1)] = 1
        self.bit_array[self.hash2(str1)] = 1
        
    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        str1 = str(str1).strip()
        hash_index1 = self.hash1(str1)
        hash_index2 = self.hash2(str1)
        if self.bit_array[hash_index1] == 1 and self.bit_array[hash_index2] == 1:
            return True
        else:
            return False
       

"""
fb = BloomFilter(32)
fb.add("0123456789")
fb.add("1234567890")
fb.add("2345678901")
fb.add("3456789012")
fb.add("4567890123")
fb.add("5678901234")
fb.add("6789012345")
fb.add("7890123456")
fb.add("8901234567")
fb.add("9012345678")
"""
