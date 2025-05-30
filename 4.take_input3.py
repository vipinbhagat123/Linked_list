class node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head
    while(temp!=None):
        print(temp.data, end='->')
        temp = temp.next
    print()
    return 

def tak_input():
    value = int(input("Enter the value of node:-"))
    head = None
    tail = None
    while(value!=-1):
        newNode = node(value)
        if (head==None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        value = int(input("Enter the value of Node:-"))
    return head

newhead=tak_input()
print_ll(newhead)