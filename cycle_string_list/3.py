list = [int(i) for i in input().split()]
list.sort()
index = []
flag = 0

if len(list) == 1 or len(list) == 0:
    exit()

for i in range(len(list)):
    if list.count(list[i]) >= 2:
        flag = 1
        index.append(list[i])
    elif list.count(list[i]) < 2:
        continue

if flag == 1:
    repeat_element = index[-1]
    count = 1

    for i in range(len(index)-1):
        if index[i + 1] == repeat_element:
            count += 1
            continue
        elif index[i + 1] != repeat_element:
            repeat_element = index[i+1]
            print(repeat_element, end=' ')

    if len(index) == count:
        print(repeat_element)
        exit()