s=input().split()
count=0
for i in s:
    if i >='0' and i<='9':
        count+=1
if count== len(s):
    print("string contains only digits")
else:
    print("string donot contain only digits")
    
