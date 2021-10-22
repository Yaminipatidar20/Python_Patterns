num=int(input("Enter a number:-"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(65+num-i+j),end=" ")
    print()
for a in range(1,num+1):
    for k in range(1,num-a+1):
        print(chr(64+k+a),end=" ")
    print()