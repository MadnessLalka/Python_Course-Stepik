list = [int(i) for i in input().split()]

if len(list) == 1:
    print(list[0])
else:
    sum = 0
    for i in range(len(list)-1):
        sum = list[i-1] + list[i+1]
        print(sum, end='\t')
    print(list[-2] + list[0])
