from itertools import repeat

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = []

    for item in integer_list:
        t.append(item)

    t = tuple(t)

    print(hash(t))

   
    
    