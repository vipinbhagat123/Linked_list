class node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_ll(head):
    temp = head
    while (temp!=None):
        print(temp.data, end='->')
        temp =temp.next
    print()
    return 

def take_input():
    value = int(input("Enter the value of node:-"))
    head= None
    tail = None
    while (value!=-1):
        newNode = node(value)
        if(head==None):
            head = newNode
        else:
            temp = head
            while (temp.next!=None):
                temp = temp.next
            temp.next = newNode
        value = int(input("Enter the value of Node:-"))
    return head

def lenghtofll(head):
    temp = head
    ans=0
    while(temp!=None):
        temp = temp.next
        ans = ans+1
    return ans


newhead = take_input()
length=lenghtofll(newhead)
print_ll(newhead)
print(length)

