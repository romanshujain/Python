givenlist = input("Please Enter the numbers: ")
givenlist1 = givenlist.split(",")
finallist = []
finaldict = {}
count = 0
uniquelist =[]

for i in givenlist1:
    if i in uniquelist:
        continue
    else:
        uniquelist.append(i)


for j in uniquelist:
    count1 = 0
    for k in givenlist1:
        if int(k) == int(j):
            count1+= 1
        else:
            continue
    print(j,count1)
    finaldict.update(j = count1)

print(finaldict)
