# 런타임 에러

# N = int(input())
# A = list(map(int, input().split()))
# lst = [0] * 100001 # 배운 거 써보려 했는데 역시 너무 크네요 ㅋㅋ
# for num in A:
#     lst[num] += 1
# M = int(input())
# B = list(map(int, input().split()))
# for mnum in B:
#     if lst[mnum] > 0:
#         print('1')
#     else:
#         print('0')



# 시간 초과

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))
# for mnum in B:
#     if mnum in A:
#         print('1')
#     else:
#         print('0')



# 통과

N = input()
A = input().split()
dictn = {}
for a in A:
    dictn[a] = 1 
M = input()
B = input().split()
for b in B:
    print(dictn.get(b, 0))


