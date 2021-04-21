class Deque:
    
    def __init__(self):
        self.deque= []

    def addFront(self, item):
        # добавление в голову
        self.deque.insert(0, item)    

    def addTail(self, item):
        # добавление в хвост
        self.deque.append(item)
        
    def removeFront(self):
        # удаление из головы
        if self.size() > 0:
            return self.deque.pop(0)
        else:
            return None # если очередь пуста

    def removeTail(self):
        # удаление из хвоста
        if self.size() > 0:
            return self.deque.pop(self.size()-1)
        else:
            return None # если очередь пуста

    def size(self):
        # размер очереди
        if len(self.deque)> 0:
            return len(self.deque)
        else:
            return 0 

    def print_all(self):
        if self.size() > 0:
            for i in range(self.size()):
                print(self.deque[i])
        else:
            return None

def test_add_rmv_front(N):
    dq = Deque()
    dq.addFront(100)
    if dq.size() == 1:
        if dq.removeFront() == 100 and dq.size() == 0:
            print("Test add in empty - OK")
        else:
            print("Test add in empty - Fail")
    else:
        print("Test add in empty - Fail")
    dq = Deque()
    if dq.size() == 0 and dq.removeFront() == None:
        print("Test rmv in empty - OK")
    else:
        print("Test rmv in empty - Fail")
    for i in range(1 ,N+1):
        dq.addFront(i)
    if dq.size() == N:
        print('Test zapolnenie to N - OK ')
    else:
        print('Test zapolnenie to N - Fail ')
    dq.addFront(99)
    if dq.size() == N+1:
        if dq.removeFront() == 99 and dq.size() == N:
            if dq.removeFront() == N and dq.size() == N-1:
                print('Test 0 index add/rmv - OK')
            else:
                print('Test 0 index add/rmv - Fail')
    else:
        print('Test 0 index - Fail')


def test_add_rmv_tail(N):
    dq = Deque()
    dq.addTail(100)
    if dq.size() == 1:
        if dq.removeTail() == 100 and dq.size() == 0:
            print("Test add-tail in empty - OK")
        else:
            print("Test add-tail in empty - Fail")
    else:
        print("Test add-tail in empty - Fail")
    dq = Deque()
    if dq.size() == 0 and dq.removeTail() == None:
        print("Test rmv-tail in empty - OK")
    else:
        print("Test rmv-tail in empty - Fail")

    for i in range(1 ,N+1):
        dq.addTail(i)
    if dq.size() == N:
        print('Test zapolnenie to N - OK ')
    else:
        print('Test zapolnenie to N - Fail ')
    dq.addTail(111)
    if dq.size() == N+1:
        if dq.removeTail() == 111 and dq.size() == N:
            if dq.removeTail() == N and dq.size() == N-1:
                print('Test end index add/rmv - OK')
            else:
                print('Test end index add/rmv - Fail')
        else:
            print('Test end index add/rmv - Fail')
    else:
        print('Test end index - Fail')

def polindrome(string):
    if len(string) > 0:
        string = ''.join(string.split())
        dq = Deque()
        for i in string:
            dq.addTail(i)
        for i in range(int(dq.size()/2)):
            head = dq.removeFront()
            tail = dq.removeTail()
            if head == tail:
                dq.addFront(head)
                dq.addTail(tail)
            else:
                dq.addFront(head)
                dq.addTail(tail)
                return False
        return True
    else:
        return None







