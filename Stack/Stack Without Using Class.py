# STACK WITHOUT USING CLASS 
import sys
top,l=0,[]
def push():
    if max_len!=globals()['top']:
        l.append(eval(input("Enter No:")))
        globals()['top']+=1
    else:
        print("Overflow")
def pop():
    if globals()['top']!=0:
        print("elememt to be deleted",l[top-1])
        l.pop(top-1)
        globals()['top']-=1
    else:
        print("underflow")
max_len=input("Enter max_len : ")
print('\n')
while True:
    print("1.push operation\n2.pop operation\n3.top element & size\n4.stack view\n5.exit\n")
    choice=int(input("UR choice : "))
    if choice==1:push()
    if choice==2:pop()
    if choice==3:print(f"TOP ELEMENT - {l[top-1]} & SIZE - {top}")
    if choice==4:print("stack view",*l)
    if choice==5:print(sys.exit())
    print('\n')
