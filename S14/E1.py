class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def print_stack(self):
        """Traverse and print all values from top to bottom."""
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

# Example usage, can be removed or commented out in production
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack contents:")
    s.print_stack()
    print("Pop:", s.pop())
    print("After pop:")
    s.print_stack()