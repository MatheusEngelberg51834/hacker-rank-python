if __name__ == '__main__':
    N = int(input())
    ls = []
    for _ in range(N):
        com = list(input().split())
        if com[0] == 'insert':
            getattr(ls, com[0])(int(com[1]), int(com[2]))
        elif com[0] == 'print':
            print(ls)
        elif com[0] == 'remove' or 'append':
            getattr(ls, com[0])(int(com[1]))
        else:
            getattr(ls, com[0])
            
            