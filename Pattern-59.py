num=int(input("Enter a number:-"))
for i in range(1,num+1):
    print(" "*(num-i),end=" ")
    for j in range(0,i):
        print(chr(65+num+j-i),end=" ")
    print()
for k in range(1,num):
    print(" "*k,end=" ")
    for l in range(1,num+1-k):
        print(chr(65+k+l),end=" ")
    print()