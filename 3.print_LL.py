class node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head
    while(temp!=None):
        print(temp.data, end='->')
        temp = temp.next
    return

first = node(1)
second = node(2)
third = node(3)

first.next = second
second.next = third

head = first

print_ll(head)