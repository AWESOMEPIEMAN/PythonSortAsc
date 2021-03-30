list_num = []

Number = int(input("Number of elements : "))
for i in range(1, Number + 1):
    y = int(input("Value of Element %d : " % i))
    list_num.append(y)

for i in range(Number):
    for j in range(i + 1, Number):
        if(list_num[i] > list_num[j]):
            temp = list_num[i]
            list_num[i] = list_num[j]
            list_num[j] = temp

print("Sorted elements in Ascending order : ", list_num)
