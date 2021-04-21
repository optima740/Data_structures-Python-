import My_stack as ms

class Queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # вставка в хвост
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return

    def size(self):
        return len(self.queue)

    def print_all(self):
        if self.size() != 0:
            for i in range(self.size()):
                print(self.queue[i])
        else:
            return

class QueueStack:
    def __init__(self):
        self.st1 = ms.Stack()
        self.st2 = ms.Stack()

    def enqueue(self, item):
        self.st1.push(item)

    def dequeue(self):
        while self.st1.size() > 0:
            self.st2.push(self.st1.pop())
        return self.st2.pop()

    def print_all(self):
        if self.st1.size() !=0:
            while self.st1.size() > 0:
                tmp = self.st1.pop()
                self.st2.push(tmp)
            while self.st2.size() > 0:
                print(self.st2.pop())
        elif self.st2 != 0:
            while self.st2.size() > 0:
                print(self.st2.pop())
        else:
            return

def rotateQueue(struct, N):
    for i in range(N):
        struct.enqueue(struct.dequeue())



q = Queue()

N = 5
size = 8

for i in range(1, size+1):
    q.enqueue(i)
rotateQueue(q, N)
q.print_all()

