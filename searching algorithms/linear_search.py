def linearsearch():
    for i in range(n):
        if(list[i]==n):
            return i
    return("Not in list")
n=int(input("enter no of elements in list.."))
list=[]
for i in range(n):
    e=int(input("enter the elements"))
    list.append(e)
find=int(input("enter the element to find"))
print(linearsearch(list,n))
