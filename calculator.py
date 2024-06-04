def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def percentage(x,y=100):
    return x*(y/100)
while True:



    op = int(input("1.Add\n"
                   "2.Sub\n"
                   "3.Multiply\n"
                   "4.Divide\n"
                   "5.Percentage\n"
                   "6.Exit\n"
                   "Enter your choice:"))
    if op in[1,2,3,4,5,6]:
        n1 = float(input("Enter the first number:"))
        n2 = float(input("Enter the second number:"))
    if op==1:
        ans=add(n1,n2)
    elif op==2:
        ans=sub(n1,n2)
    elif op==3:
        ans=multiply(n1,n2)
    elif op==4:
        ans=divide(n1,n2)
    elif op==5:
        ans=percentage(n1,n2)
    elif op==6:
        break
    else:
        print("please enter a valid choice")

    if op>=1 or op<6:
        print("Your answer is ",ans)
