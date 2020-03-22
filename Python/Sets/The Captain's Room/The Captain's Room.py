
family_member_num = int(input())
rooms = list(map(int, input().split()))
room_set = set(rooms)
a = (family_member_num*sum(room_set)-sum(rooms)) // (family_member_num -1)
print(a)