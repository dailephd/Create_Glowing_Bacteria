#  write your code here 
path = "C:/Users/daile/PycharmProjects/Create Glowing Bacteria/Topics/Reading files/Summer/data/dataset/input.txt"
f = open(path,"r")
count=0
for line in f.readlines():
    if (line == "summer\n"):
        count+=1
print(count)