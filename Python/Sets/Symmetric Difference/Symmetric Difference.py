a, b = [set(input().split()) for i in range(4)][1::2]
c = [i for i in (a.union(b)) if i not in a.intersection(b)]
d = [int(i) for i in c]
d.sort()
for i in d:
    print(i)
