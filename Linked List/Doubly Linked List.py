# DOUBLY_LINKED_LIST 20 SEPT 2020

import sys

class Node:
    # class for creating new nodes
    def __init__(s,data):
        s.data=data
        s.prev=None
        s.next=None

class DoublyLinkedList:
    # class to create singly linked list
    def __init__(s):
        s.head=None
    
    def insertionfromend(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty if yes then creating and adding new node
        if s.head is None:
            s.head=Node(int(input("Enter element to be inserted -> ")))
            print("Inserted successfully")
        else:
            # creating a new node
            new_node=Node(int(input("Enter element to be inserted -> ")))
            # iterating over nodes and reaching out to last node
            while temp.next is not None:
                temp=temp.next
            # inserting data at the end    
            temp.next=new_node
            new_node.prev=temp
            print("Inserted successfully")
    
    def insertionfromfront(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty if yes then creating and adding new node
        if s.head is None:
            s.head=Node(int(input("Enter element to be inserted -> ")))
            print("Inserted successfully")
        else:
            # creating a new node
            new_node=Node(int(input("Enter element to be inserted -> ")))
            # first linking new_node with the address stored in head and then assign new_node address in head
            new_node.next=s.head
            s.head.prev=new_node
            s.head=new_node
            print("Inserted successfully")
    
    def insertionatspecifiedposition(s):
        # creating a varible through which iteration will be done
        temp,p,not_found,pos=s.head,1,True,int(input("Enter position - > "))
        # checking whether list is empty if yes then creating and adding new node
        if s.head is None:
            print("Enter element to be inserted since list is empty so it'll be added first position automatically ")
            s.head=Node(int(data))
        # checking over first position if condition is true adding the new_node there 
        elif pos == 1:
            not_found=False
            s.insertionfromfront()
            print("Inserted successfully")
        else:
            # creating a new node
            data_1 = int(input("Enter data to be inserted -> "))
            new_node=Node(data_1)
            # iterating over the rest of the list and adding new_node at specified position 
            while temp is not None:
                if pos == p+1:
                    not_found=False
                    new_node.next=temp.next
                    temp.next.prev=new_node
                    new_node.prev=temp
                    temp.next=new_node
                temp=temp.next
                p+=1
            print("Inserted successfully")
        if not_found:print("irrelevant position w.r.t list")
    
    def deletionfromend(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        # iterating over list till second last and assigning 2nd last address None
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            print("Element removed successfully")
    
    def deletionfromfront(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        else:
            # removing all traces of 1st node existence
            s.head=temp.next
            temp.next.prev=None
            print("Element removed successfully")
    
    def deletionfromspecifiedposition(s):
        # creating a varible through which iteration will be done
        temp,p,not_found,pos=s.head,1,True,int(input("Enter the position data you want to delete -> "))
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        # checking over first position 
        elif pos==1:
            not_found=False
            s.deletionfromfront(s)
            print("Element removed succesfully")
        else:
            # iterating over list checking for position node to be removed 
            while temp is not None:
                if p+1==pos:
                    not_found=False
                    temp.next=temp.next.next
                    temp.next.prev=temp
                temp=temp.next
                p+=1
            print("Element removed succesfully")
        if not_found:print("Irrelevant position w.r.t list")
    
    def searchingofposition(s):
        # creating a varible through which iteration will be done
        temp,p,not_found,data_1=s.head,1,True,int(input("Enter the element position you want to know -> "))
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        else:
            # iterating over list checking for position via data 
            while temp is not None:
                if temp.data==data_1:
                    not_found=False
                    print(f"{temp.data} is at {p}")
                temp=temp.next
                p+=1
        if not_found:print("Irrelevant element w.r.t list")
    
    def updateatspecifiedposition(s):
        # creating a varible through which iteration will be done
        temp,p,not_found,pos=s.head,1,True,int(input("Enter the position data you want to update -> "))
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        # checking over first position if condition satisified then updating node value
        elif pos == 1:
            not_found=False
            s.head.data=int(input("Enter element to be inserted -> "))
            print("Data updated successfully")
        else:
            # iterating over list checking for position
            while temp is not None:
                if pos == p:
                    non_found=False
                    temp.data=int(input("Enter element to be inserted -> "))
                temp=temp.next
                p+=1
            print("Data updated successfully")
        if not_found:print("Irrelevant position w.r.t list")
    
    def reverselist(s,temp):
        # using recursion to print reverse
        # creating a varible through which iteration will be done and a list too
        if s.head is None:print("UNDERFLOW!!")
        else:
            if temp.next is None:
                print(temp.data,end=" ")
                return
            s.reverselist(temp.next)
            print(temp.data,end=" ")  
    
    def palindromecheck(s):
        # creating a varible through which iteration will be done and a list too
        temp = s.head
        s_ = ""
        #checks if list is empty 
        if s.head is None:print("UNDERFLOW!!")
        else:
            while temp is not None:
                # concatenating linked list data into string variable
                s_+=str(temp.data)
                temp=temp.next
        # checking for palindrome
        print("Palindrome sequence found" if s_==s_[::-1] else "No palinrome sequence found")            
    
    def maxandmin(s):
        # creating a varible through which iteration will be done and a list too
        temp,l = s.head,[]
        #checks if list is empty  
        if s.head is None:print("UNDERFLOW!!")
        else:
            # appending all linked list data part in python list and calling predefined function
            while temp is not None:
                l.append(temp.data) 
                temp=temp.next
        print(f"Max value in list : {max(l)}\nMin value in list : {min(l)}\n")
    
    def duplicateremoval(s):
        temp,curr,index=s.head,None,None
        #checks if list is empty 
        if s.head is None:print("UNDERFLOW!!")
        else:
            while temp is not None:
                curr=temp
                index=temp.next
                while index is not None:
                    if temp.data==index.data:
                        curr.next=index.next
                        index.prev=curr
                    else:
                        curr=index
                    index = index.next
                temp=temp.next
        print("Duplicate removed")
    
    def sortList(s):   
        # sorting is done on the basis of comparsion of two variables iterated over list 
        temp,index = s.head,None;  
        #checks if list is empty 
        if s.head is None:print("UNDERFLOW!!")
        else:
            while temp is not None: 
                # index is point just next node that is pointed by temp
                index = temp.next;
                # iterating index over list from assigned address
                while index is not None:
                    # comparing data  
                    if(temp.data > index.data): 
                        # swapping values
                        temp.data,index.data = index.data,temp.data
                    index = index.next;  
                temp = temp.next;   
        print("List is sorted") 
    
    def listview(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty
        if s.head is None:print("Underflow!!")
        else:
            # iterting over nodes and printing data
            while temp is not None:
                print(temp.data,end = " ")
                temp=temp.next

d=DoublyLinkedList()

while True:
    print("1.inseretion from end\n2.insertion from front\n3.insertion at specified position\n4.list view\n5.deletion from end\n6.deletion from front\n7.deletion from specified position\n8.search of an element position\n9.updating element at specified position\n10.to see list in reverse order")
    print("11.to check whether list is palindrome or not\n12.to find max and min value\n13.to remove duplicate\n14.to sort the list\n15.exit\n")
    choice=int(input("UR choice : "))
    if choice not in range(1,17):
        print("You opted out of provided options")
    else:
        if choice==1:d.insertionfromend()
        if choice==2:d.insertionfromfront()
        if choice==3:d.insertionatspecifiedposition()
        if choice==4:d.listview()
        if choice==5:d.deletionfromend()
        if choice==6:d.deletionfromfront()
        if choice==7:d.deletionfromspecifiedposition()
        if choice==8:d.searchingofposition()
        if choice==9:d.updateatspecifiedposition()
        if choice==10:d.reverselist(d.head)
        if choice==11:d.palindromecheck()
        if choice==12:d.maxandmin()
        if choice==13:d.duplicateremoval()
        if choice==14:d.sortList()
        if choice==15:sys.exit()    
    print('\n') 
