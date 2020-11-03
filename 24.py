x = int(input())

ls = list(map(int, input().split()))

print(ls)

n = int(input())

total_cash = 0

for _ in range(n):
    buy = list(input().strip())
    if buy[0] in ls:
        total_cash += buy[1]
        ls.remove(buy[0])

print(total_cash)