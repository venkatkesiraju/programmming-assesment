sen=input("enter a sentence:").split()
s=" "
for i in range(len(sen)):
   sen[i]=sen[i][::-1]
s=s.join(sen)
print(s)
