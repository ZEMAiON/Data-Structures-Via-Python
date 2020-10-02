# QUEUE USING WITHOUT CLASS 
import sys
front,rear,l=0,0,[]
def enqueue():
    if globals()['rear']!=max_len:
        l.append(eval(input("Enter No:")))
        globals()['rear']+=1
    else:
        print("Overflow")
def dequeue():
    if globals()['front']+1<=globals()['rear']:
        print("elememt to be deleted",l[front])
        l.pop(front)
        l.insert(0,"#")
        globals()['front']+=1
    else:
        print("underflow")
max_len=eval(input("Enter max_len : "))
print('\n')
while True:
    print("1.enqueue operation\n2.dequeue operation\n3.queue view\n4.exit\n")
    choice=int(input("UR choice : "))
    if choice==1:enqueue()
    if choice==2:dequeue()
    if choice==3:print("QUEUE VIEW",*l)
    if choice==4:print(sys.exit())
    print('\n')
