#An array is given by user from 1-100 by missing one number
#let us take array name as 'a'
a=[]
for i in range(1,101):
    if i!= 25:
        a.append(i)
for i in range(1,101):
    if i not in a:
        print("misssing number is :",i)
        break
