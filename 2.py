cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ls = [0, 1]
    for _ in range(n - 2):
        ls.append(ls[-1] + ls[-2])
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        return ls


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))