class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        new_item = Node(item)
        if self.is_empty():
            self.head = new_item
            self.tail = new_item
            self.size += 1
            return True
        current = self.head
        while current:
            if current.item == item:
                return False
            if current.item > item:
                # insert new item before current node
                if current == self.head:
                    self.head = new_item
                    new_item.next = current
                    current.prev = new_item
                else:
                    new_item.prev = current.prev
                    current.prev.next = new_item
                    new_item.next = current
                    current.prev = new_item
                self.size += 1
                return True
            if current == self.tail:
                # insert new item after the last node
                current.next = new_item
                new_item.prev = current
                self.tail = new_item
                self.size += 1
                return True
            current = current.next

    def remove(self, item):
        current = self.head
        while current:
            if current.item == item:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return None

    def pop(self, index):
        if index < 0 or index >= self.size:
            raise IndexError
        current = self.head
        for i in range(index):
            current = current.next
        item = current.item
        self.remove(item)
        return item

    def search(self, item):
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False

    def python_list(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.item)
            current = current.next
        return lst

    def python_list_reversed(self):
        current = self.tail
        lst = []
        while current:
            lst.append(current.item)
            current = current.prev
        return lst

    def get_size(self):
        return self.size
