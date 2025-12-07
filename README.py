# A.-Choosing-Teams
n, k = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
for i in range(n):
	tot = lst[i] + k
	if tot <= 5:
		count += 1
print(count // 3)
