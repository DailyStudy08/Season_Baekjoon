clock, minute = map(int, input().split())
if minute < 45:
    clock -= 1
    if clock == -1:
        clock = 23
    minute += 60
print(clock, minute - 45)