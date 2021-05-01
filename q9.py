n=int(input("enter number of elements:"))
a=[]
for i in range(0,n):
    s=int(input())
    a.append(s)
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
