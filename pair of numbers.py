def pairs(thislist,n):
    pairLst=[]
    while thislist:
        num=thislist.pop()
        diff=n-num
        if diff in thislist:
            pairLst.append((diff,num))
    return pairLst
thislist = [1,2,3,4,5,6,7,8,9,10]
n=12
print(pairs(thislist,n))