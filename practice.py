list = ['a','b','c','d','e','f']
for i in range(0,len(list)):
    list[i]=ord(list[i])


for i in range(len(list)):
    for j in range(0,len(list)-i-1):
        if list[j] > list[j+1]:
            list[j],list[j+1]=list[j+1],list[i]


for i in range(0,len(list)):
    list[i]=chr(list[i])
print(list)