# STACK USING LINKED LIST
import sys
class Node:
    def __init__(s,data):
        s.data=data
        s.next=None
        s.prev=None
class Stack:
    def __init__(s):
        s.head=None
    def push(s):
        data=eval(input("Enter data: "))
        if s.head is None:
            s.head=Node(data)
        else:
            new_node=Node(data)
            s.head.prev=new_node
            new_node.next=s.head
            new_node.prev=None
            s.head=new_node    
    def pop(s):
        if s.head is None:
            return None
        else:
            temp=s.head.next
            s.head=s.head.next
            s.head.prev=None
            return temp
    def top(s):
        return s.head.data
    def size(s):
        temp=s.head
        c=0
        while temp is not None:
            c+=1
            temp=temp.next
        return c
    def stackview(s):
        temp=s.head
        while temp is not None:
            print(temp.data,end = " ")
            temp=temp.next
        
s=Stack()
while True:
    print("1.push operation\n2.pop operation\n3.top element & size\n4.stack view\n5.exit\n")
    choice=int(input("UR choice : "))
    if choice==1:s.push()
    if choice==2:s.pop()
    if choice==3:print(f"TOP ELEMENT - {s.top()} & SIZE - {s.size()}")
    if choice==4:s.stackview()
    if choice==5:print(sys.exit())
    print('\n')
