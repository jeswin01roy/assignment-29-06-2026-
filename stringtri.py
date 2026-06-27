print("\t\t string triangle")
s=input("enter a string : ")
l=len(s)
pos=0                                               
for i in range(1,l+1):                                   
    print()                                       
    for j in range(1,i+1):
        if(pos < l):
            print(s[pos],end=" ")
            pos = pos + 1

#         # output:
#         #    a
#         #    p p
#         #    l e
        
               
print("\t\tString Triangle")

s = input("Enter a string: ")
l = len(s)

for i in range(0, l ):
    print()
    for j in range(0, i+1 ):
            print(s[j], end=" ")

            # output:
            # a
            # a p
            # a p p
            # a p p l
            # a p p l e