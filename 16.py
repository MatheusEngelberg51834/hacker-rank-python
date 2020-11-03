n = int(input())

for _ in range(n):
    an = int(input())
    #while len(a) < an:
    a = set(map(int, input().split()))
    bn = int(input())
    #while len(b) < bn:
    b = set(map(int, input().split()))
    print(a.issubset(b))

