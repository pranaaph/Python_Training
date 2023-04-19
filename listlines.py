with open("file.txt") as f:
    lst = f.readlines()
lst=[i.strip() for i in lst]
print(lst)