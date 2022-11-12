lst=[5,3,1,7,9,2]
l=len(lst)
for i in range(l):
  for j in range(l):
    if(lst[i]>lst[j]):
      temp=lst[i]
      lst[i]=lst[j]
      lst[j]=temp
print(lst)
    
