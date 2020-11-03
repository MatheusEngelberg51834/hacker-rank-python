if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    x_ls = [i for i in range(x + 1)]
    y_ls = [j for j in range(y + 1)]
    z_ls = [k for k in range(z + 1)]

    perms = [[x, y, z] for x in x_ls for y in y_ls for z in z_ls]
    out = []

    for perm in perms:
        if sum(perm) != n:
            out.append(perm)

    print(out)