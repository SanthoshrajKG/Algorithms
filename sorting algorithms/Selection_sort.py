#selection_sort
lst=[4,8,1,3,8,9,0,15,67,1,3,27]
l=len(lst)
for i in range(l):
    min_val=10000
    for j in range(i,l):
        if(lst[j]<=min_val):
            min_val=lst[j]
            ind=j 
    temp=lst[i]
    lst[i]=min_val
    lst[ind]=temp
print(lst)
            
            
            
        
        
