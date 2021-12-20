import numpy as np


class Stack:
    def __init__(self, sizeOf=6):
        self.stack = np.full([sizeOf], np.inf)
        self.endOfStack = 0
        self.maxSize = sizeOf

    def append(self, param):
        if self.endOfStack == self.maxSize:
            print("Stos przepełniony")
        else:
            self.stack[self.endOfStack] = param
            self.endOfStack = self.endOfStack + 1

    def pop(self):
        if self.endOfStack == 0:
            print("Stos pusty")
        else:
            self.endOfStack = self.endOfStack - 1
            temp = self.stack[self.endOfStack]
            self.stack[self.endOfStack] = np.inf
            return temp

    def search(self, param):
        return [x for x in range(len(self.stack)) if self.stack[x] == param]


class Queue:
    def __init__(self, sizeOf=6):
        self.queue = np.full([sizeOf + 1], np.inf)
        self.head = 0
        self.tail = 0
        self.maxSize = sizeOf

    def enqueue(self, param):
        if self.head == self.tail + 1 or (self.tail == self.maxSize and self.head == 0):
            print("Kolejka przepełniona")
            return
        if self.tail != self.maxSize:
            self.tail = self.tail + 1
        else:
            self.tail = 0
        self.queue[self.tail] = param

    def dequeue(self):
        if self.head == self.tail:
            print("kolejka pusta")
        if self.head != self.maxSize:
            self.head = self.head + 1
        else:
            self.head = 0
        temp = self.queue[self.head]
        self.queue[self.head] = np.inf
        return temp

    def search(self, param):
        return [x for x in range(len(self.queue)) if self.queue[x] == param]


class PriorityQueue:
    def __init__(self, sizeOf=6):
        self.queue = np.full([sizeOf + 1], np.inf)
        self.head = 0
        self.tail = 0
        self.maxSize = sizeOf

    def enqueue(self, param):
        if self.head == self.tail + 1 or (self.tail == self.maxSize and self.head == 0):
            print("Kolejka przepełniona")
            return
        if self.tail != self.maxSize:
            self.tail = self.tail + 1
        else:
            self.tail = 0
        self.queue[self.tail] = param

    def search(self, param):
        return [x for x in range(len(self.queue)) if self.queue[x] == param]

    def dequeue(self):
        if self.head == self.tail:
            print("kolejka pusta")
            return
        if self.head != self.maxSize:
            self.head = self.head + 1
        else:
            self.head = 0
        minimalIndex = np.where(self.queue == np.amin(self.queue))[0][0]
        temp = self.queue[minimalIndex]
        self.queue[minimalIndex] = self.queue[self.head]
        self.queue[self.head] = np.inf
        return temp


class oneWayList:
    def __init__(self, x, next=None):
        self.next = next
        self.value = x

    def show(self):
        if self.next:
            if x := self.next.show():
                return f"{self.value}, {x}" if self.value else x
        else:
            return self.value

    def add(self, x, index=-1):
        if index == -1:
            if not self.next:
                self.next = oneWayList(x)
                return
            else:
                return self.next.add(x)
        elif index > 0:
            return self.next.add(x, index - 1)
        elif index == 0:
            self.next = oneWayList(x, self.next)
            return

    def search(self, param, index=-1):
        if self.next:
            if x := self.next.search(param, index + 1):
                return f"{index}, {x}" if self.value == param else x
        else:
            return index

    def delete(self, index=-1):
        if index == -1:
            if self.next.next:
                return self.next.delete()
            else:
                x = self.next.value
                self.next = None
                return x
        if index == 0:
            temp = self.next
            self.next = self.next.next
            return temp.value
        return self.next.delete(index - 1)


def main():
    st = Stack(5)
    st.append(1)
    st.append(2)
    st.append(1)
    st.append(1)
    st.append(2)
    print(st.search(1))
    oWL = oneWayList(None)
    oWL.add(4)
    oWL.add(4)
    oWL.add(1, 1)
    oWL.add(2, 0)
    print(oWL.search(4))
    print(oWL.show())


if __name__ == "__main__":
    main()
