num=int(input("Enter a number:-"))
for i in range(1,num+1):
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()