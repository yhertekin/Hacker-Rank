super_set = set(map(int, input().split()))
number_of_sets = int(input())
case = True
for i in range(number_of_sets):
    test_set = set(map(int, input().split()))
    if not super_set.issuperset(test_set):
        case = False

print(case)
