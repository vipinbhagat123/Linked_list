# creat a node of ll

class node:
    def __init__(self, value):
        self.data = value
        self.next = None
first = node(1)
second= node(2)
third=node(3)
first.next = second
second.next = third
print(first.data)
print(first.next.data)
print(first.next.next.data)