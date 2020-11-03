import re

n = int(input())

ls = []
for _ in range(n):
    ls.append(input())

for item in ls:
    try:
        re.compile(item)
        print(True)
    except re.error:
        print(False)