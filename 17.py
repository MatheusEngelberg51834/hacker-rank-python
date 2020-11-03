a = set(map(int, input().split()))
n = int(input())

ls = []

for _ in range(n):
    b = set(map(int, input().split()))
    ls.append(a.issuperset(b))

boolean = True

for element in ls:
    if element == False:
        boolean = False

print(boolean)