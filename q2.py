a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    e=int(input("Enter element" + str(x+1) + ":"))
    a.append(e)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print(unique)
