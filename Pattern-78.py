num=int(input("Enter a number:-"))
for i in range(1,num+1):
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for p in range(1,num):
    print(" "*p,end=" ")
    for q in range(1,num+1-p):
       print(num-p,end=" ")
    print()