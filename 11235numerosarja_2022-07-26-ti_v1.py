list = []
list.append(1)
list.append(1)
#for i==3 to 10
#    list.append(list.pop[i-2] + list.pop[i-1])
#next

nextel = 0
for i in range(10):
    nextel = list[i] + list[i+1] 
    print(nextel)
    list.append(nextel)
    print(list[-2])
    print(list[-1])

#    if i > 10:
#        break

#for x in list:
#   print(x)

print(list)
