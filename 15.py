n = int(input())
s = set(map(int, input().split()))
x = int(input())

ls = [input() for _ in range(x * 2)]

for i in range(x * 2):
    if (i + 1) % 2 == 0:
        s2 = set(map(int, ls[i].split()))
        getattr(s, ls[i - 1].split()[0])(s2)

sm = 0
for element in s:
    sm += int(element)
    
print(sm)
