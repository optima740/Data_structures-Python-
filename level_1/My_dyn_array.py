import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if self.__len__()!=0:
            if i > self.count or i < 0:
                raise IndexError('Index is out of bounds')
            elif i == self.count:
                self.append(itm)
            else:
                if self.count == self.capacity:
                    self.resize(2 * self.capacity)
                tmp_loc = self.make_array(self.count-i)
                j = 0
                for k in range(i, self.count):
                    tmp_loc[j] = self.array[k]
                    j+=1
                self.array[i] = itm
                j = 0
                for k in range(i+1, self.count+1):
                    self.array[k] = tmp_loc[j]
                    j+=1
                self.count +=1
        elif self.__len__()==0 and i == 0:
            self.append(itm)
        else:
            raise IndexError('Index is out of bounds')
            return

    def delete(self, i):
        capacity_to_del= int(self.capacity/1.5)
        if self.__len__()!=0:
            if i >= self.count or i < 0:
                raise IndexError('Index is out of bounds')
            elif i == (self.count-1):
                if i == 0 and self.count == 1:
                    self.count = 0
                    self.array = self.make_array(self.capacity)
                    return
                tmp_loc = self.make_array(self.count-1)
                for k in range(0, i):
                    tmp_loc[k] = self.array[k]
                self.array = tmp_loc
                self.count -=1
                if self.count < (0.5 * self.capacity) and self.capacity>16:
                    if capacity_to_del > 16:
                        self.resize(capacity_to_del)
                        return
                    else:
                        self.resize(16)
            else:
                tmp_loc = self.make_array(self.count-1)
                j = 0
                for k in range(self.count):
                    if k != i:
                        tmp_loc[j] = self.array[k]
                        j+=1
                self.array = tmp_loc
                self.count -=1
                if self.count < (0.5 * self.capacity) and self.capacity>16:
                    if capacity_to_del > 16:
                        self.resize(capacity_to_del)
                        return
                    else:
                        self.resize(16)
                return
        else:
            raise IndexError('Index is out of bounds')
            return

"""
da = DynArray()
for i in range(17):
    da.append(i)
    #print(da[i])
print('count:', da.count)
print('capacity:', da.capacity)
print('delete')
#da.insert(17,99)

da.delete(0)
da.delete(0)
da.delete(0)
da.delete(0)
da.delete(0)
da.delete(0)
da.delete(0)
da.insert(0,99)
da.insert(0,99)
da.insert(0,99)
da.insert(0,99)
da.insert(0,99)
da.insert(0,99)
da.insert(0,99)
print('count:', da.count)
print('capacity:', da.capacity)

for i in range(15,-1,-1):
    da.delete(i)

for i in range(15,-1,-1):
    da.delete(i)
da.insert(12,99)
print('count:', da.count)
print('capacity:', da.capacity)
for i in range(da.count):
    print(da[i])

print('count:', da.count)
print('capacity:', da.capacity)

da.delete(12)
da.delete(15)

print('count:', da.count)
print('capacity:', da.capacity)
for i in range(da.count):
    print(da[i])
for i in range(15, 22):
    da.append(i)

print('count:', da.count)
print('capacity:', da.capacity)

"""
