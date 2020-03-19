if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l = []
    for item in integer_list:
        l.append(item)
    
    t = tuple(l)
    print(hash(t))
