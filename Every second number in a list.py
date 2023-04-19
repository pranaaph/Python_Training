thislist = [1,2,3,4,5,6,7,8,9,10]
second_number=2-1
i=0
length=len(thislist)
while length >0:
    i=(second_number+i) % length
    print(thislist.pop(i))
    length -=1

