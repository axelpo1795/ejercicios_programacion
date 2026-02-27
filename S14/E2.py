class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, value):
        new_node = Node(value, None, self.head)
        if self.head is None:
            # empty deque
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, value):
        new_node = Node(value, self.tail, None)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop from empty deque")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return value

    def pop_right(self):
        if self.tail is None:
            raise IndexError("pop from empty deque")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return value

    def print_deque(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

# Example usage when run directly
if __name__ == "__main__":
    d = Deque()
    d.push_left(1)
    d.push_right(2)
    d.push_left(0)
    d.push_right(3)
    print("Deque contents:")
    d.print_deque()
    print("Pop left:", d.pop_left())
    print("Pop right:", d.pop_right())
    print("After pops:")
    d.print_deque()