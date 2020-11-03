# from collections import namedtuple
# N = int(input());student = namedtuple('student',input().strip().split())
# print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

n = int(input())
ls = input()

s = set()
for item in ls:
    if item not in s:
        s.add(item)

print(len(s))
