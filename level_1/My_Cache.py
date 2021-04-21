class NativeCache:
    
    def __init__(self, sz):
        self.size_n = sz
        self.slots = {}
        self.len_slots = 0

    def chek_item(self, value):
        item = self.slots.get(value)
        if item != None:
            return True
        else:
            return False

    def add_item(self, value):
        if self.len_slots < self.size_n and self.chek_item(value) == False:
            self.slots[value] = 1
            self.len_slots += 1
        elif self.chek_item(value) == True:
            self.slots[value] += 1
        elif self.len_slots == self.size_n and self.chek_item(value) == False:
            list_value = list(self.slots.values())
            min_val = min(list_value)
            index = list_value.index(min_val)
            list_key = list(self.slots.keys())
            key2del = list_key[index]
            self.slots.pop(key2del)
            self.slots[value] = 1

    











