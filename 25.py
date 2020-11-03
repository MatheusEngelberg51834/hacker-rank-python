if __name__ == '__main__':

    score_list = []
    score_list1 = []
    ls = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list1.append(score)
        lsitem = name + ' ' + str(score)
        ls.append(lsitem.split())

    for item in score_list1:
        if item not in score_list:
            score_list.append(item)

    score_list.sort()

    out = []

    for ls1 in ls:
        if float(score_list[1]) == float((ls1[1])):
            out.append(ls1[0])

    out.sort()

    for o in out:
        print(o)