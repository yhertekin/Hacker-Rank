if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list()
    for i in arr:
        l.append(i)
    
    m = max(l)
    a = [e for e in l if e != m]
    print(max(a))
