from aocd import get_data

arr = get_data(session = '53616c7465645f5fe308c0f36408b8c4fb84bc55ed1b482a6a45f20fe883c99c8bb11b37dc4c985d66b44e2277ac01d271aaa671b2de7b38748d6c56bae89519', day=1, year=2022)
#print(arr)
max = 0
temp = 0
sums = []
arr = arr.split('\n\n')
for i in range(len(arr)):
    if (arr[i] != '\n\n'):
        next = arr[i].split('\n')
        for x in range(len(next)):
            temp = temp + int(next[x])
        if (temp > max):
            max = temp
    sums.append(temp)
    temp = 0
sums.sort(reverse=True)

print(sums[0])
print(sums[1])
print(sums[2])
max = sums[0] + sums[1] + sums[2]
print(max) 
