# SINGLY_LINKED_LIST 21 SEPT 2020

import sys

class Node:
    # class for creating new nodes
    
	def __init__(s,data):
        s.data=data
        s.next=None

class SinglyLinkedList:
    # class to create singly linked list
    
	def __init__(s):
    	s.head=None
    
	def insertionfromend(s):
        # checking whether list is empty
        if s.head == None:
            # creating a new node
            s.head=Node(int(input("Enter element to be inserted -> ")))
			print("Inserted successfully")
        else:
            # creating a varible through which iteration will be done  
            temp=s.head
            # creating a new node
            new_node=Node(int(input("Enter element to be inserted -> ")))
            # iterating over nodes and reaching out to last node
            while temp.next is not None:
                temp=temp.next
            # inserting data at the end
            temp.next=new_node
			print("Inserted successfully")
    
	def insertionfromfront(s):
        # checking whether list is empty
        if s.head is None:
            # creating a new node
            s.head=Node(int(input("Enter element to be inserted -> ")))
			print("Inserted successfully")
        else:
            # creating a new node
            new_node=Node(int(input("Enter element to be inserted -> ")))
            # first linking new_node with the address stored in head and then assign new_node address in head
            new_node.next=s.head
            s.head=new_node
			print("Inserted successfully")
    
	def insertionatspecifiedposition(s):
            data,pos=[int(x) for x in input("Enter data n then position: ").split()]
            not_found=True
            # checking whether list is empty
            if s.head is None:
                s.head=Node(data)
				print("Updated successfully")
            # checking if data is at position "1"
            elif pos==1:
                new_node=Node(data)
                new_node.next=s.head
                s.head=new_node
				print("Updated successfully")
            # iterating over and inserting at that appropriate position    
            elif s.head is not None:
                p=1
                temp=s.head
                new_node=Node(data)
                while temp is not None:
                    if p+1==pos:
                        new_node.next=temp.next
                        temp.next=new_node
                        not_found=false
                    temp=temp.next
                    p+=1
				print("Updated successfully")
            if not_found:print("Out of range input")
    
	def deletionfromend(s):
        # creating a varible through which iteration will be done 
        temp=s.head
        # checking whether list is empty
        if s.head is None:print("UNDERFLOW!!!")
        else:
            # iterating over nodes and reaching out to second last node
            while temp.next.next is not None:
                temp=temp.next
            # assign None in second last node address part 
            temp.next=None
            print("Element removed successfully")  
    
	def deletionfromfront(s):
        # checking whether list is empty
        if s.head is None:print("UNDERFLOW!!!")
        else:
            # creating a varible through which iteration will be done 
            temp=s.head
            # assigning second node address to head 
            s.head=temp.next
        print("Element removed successfully")
    
	def deletionfromspecifiedposition(s):
        temp,p,not_found=s.head,1,True
        pos=int(input("Enter the position data you want to delete -> "))
        # checking whether list is empty
        if s.head is None:print("UNDERFLOW!!!")    
        # checking whether deleting position is first node
        elif pos==1:
            s.head=temp.next
			print("Element removed successfully")
        else:
            # checking over other nodes via iterating over deleting position 
            while temp is not None:
                if pos==p+1:
                    not_found=False
                    temp.next=temp.next.next
                temp=temp.next
                p+=1
            print("Element removed successfully")
        if not_found:print("Out of range input")
    
	def searchingofposition(s):
        temp,p,not_found=s.head,1,True
        data_1=int(input("Enter the data whose position you want to know -> "))
        # checking whether list is empty
        if s.head is None:print("UNDERFLOW!!!")
        else:
            # iterating over and checking the position of node using a variable
            while temp is not None:
                if temp.data == data_1:
                    not_found=False
                    print(f"{temp.data} is at {p}")
                temp=temp.next
                p+=1
        if not_found:print("No such element present")
    
	def updateatspecifiedposition(s):
        temp,p,not_found=s.head,1,True
        pos , data_1,=[int(i) for i in input("Enter the position and then data value to be updated at that position -> ").split()] 
        # checking whether list is empty
        if s.head is None:print("UNDERFLOW!!!")
        # checking whether position that is to be updated is first node
        elif pos==1:
            s.head.data=data_1
			print("Data updated successsfully")
        else:
            # checking over other nodes via iterating over position to be updated
            while temp is not None:
                if p+1==pos:
                    not_found=False
                    temp.next.data=data_1
                temp=temp.next
                p+=1  
            print("Data updated successsfully")
        if not_found:print("Irrelevant position entered")
    
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
	    # selecting a node and comparing that node with rest of linked list nodes if duplicacy found that node is being skipped
            while temp is not None:
                curr=temp
                index=temp.next
                while index is not None:
                    if temp.data==index.data:
                        curr.next=index.next
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
    
	def swaptwonodes(s):
        n1,n2=[int(i) for i in input("Enter to values of that nodes which u want to swoop -> ").split()]
        prevNode1 = None  
        prevNode2 = None 
        # creating varibles through which iteration will be done
        node1 = s.head  
        node2 = s.head  
        #checks if list is empty  
        if(s.head == None):  
            print("UNDERFLOW!!")    
        #if n1 and n2 are equal, then list will remain the same  
        if(n1 == n2):  
            pass     
        #search for node1  
        while(node1 != None and node1.data != n1):  
            prevNode1 = node1  
            node1 = node1.next      
        #search for node2  
        while(node2 != None and node2.data != n2):  
            prevNode2 = node2  
            node2 = node2.next       
        if(node1 != None and node2 != None):   
            #if previous node to node1 is not None then, it will point to node2  
            if(prevNode1 != None):  
                prevNode1.next = node2  
            else:  
                s.head  = node2       
            #if previous node to node2 is not None then, it will point to node1  
            if(prevNode2 != None):  
                prevNode2.next = node1  
            else:  
                s.head  = node1       
            #swaps the next nodes of node1 and node2  
            temp = node1.next   
            node1.next = node2.next   
            node2.next = temp  
            print("Swapped successfully")
        else:  
            print("Swapping is not possible");
    
	def listview(s):
        # creating a varible through which iteration will be done
        temp=s.head
        # checking whether list is empty
        if s.head is None:print("List is empty")
        # iterting over nodes and printing data
        while temp is not None:
            print(temp.data,end = " ")
            temp=temp.next       
s1=SinglyLinkedList() 
while True:
    print("1.inseretion from end\n2.insertion from front\n3.insertion at specified position\n4.list view\n5.deletion from end\n6.deletion from front\n7.deletion from specified position\n8.search of an element position\n9.updating element at specified position\n10.to see list in reverse order")
    print("11.to check whether list is palindrome or not\n12.to find max and min value\n13.to remove duplicate\n14.to sort the list\n15.to swap two values\n16.exit\n")
    choice=int(input("UR choice : "))
    if choice not in range(1,17)
        print("You opted out of provided options")
    else:
        if choice==1:s1.insertionfromend()
        if choice==2:s1.insertionfromfront()
        if choice==3:s1.insertionatspecifiedposition()
        if choice==4:s1.listview()
        if choice==5:s1.deletionfromend()
        if choice==6:s1.deletionfromfront()
        if choice==7:s1.deletionfromspecifiedposition()
        if choice==8:s1.searchingofposition()
        if choice==9:s1.updateatspecifiedposition()
        if choice==10:s1.reverselist(s1.head)
        if choice==11:s1.palindromecheck()
        if choice==12:s1.maxandmin()
        if choice==13:s1.duplicateremoval()
        if choice==14:s1.sortList()
        if choice==15:s1.swaptwonodes()
        if choice==16:sys.exit()    
    print('\n')
