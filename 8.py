n = int(input())
s = set(map(int, input().split()))
x = int(input())

for _ in range(x):
    op = input()
    com = op.split()
    if len(com) > 1:
        getattr(s, com[0])(int(com[1]))
    else:
        getattr(s, com[0])()

sm = 0
for element in s:
    sm += element

print(sm)
