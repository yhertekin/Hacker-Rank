test_case_num = int(input())
for i in range(test_case_num):
    first_set_num = int(input())
    first_set = set(map(int, input().split()))
    second_set_num = int(input())
    second_set = set(map(int, input().split()))

    print(first_set <= second_set)
