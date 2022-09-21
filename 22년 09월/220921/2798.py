# ############# 영원한 고통의 시간초과 ##############

# N, M = map(int, input().split())
# card_list = list(map(int, input().split()))
# three = []
# for i in range(1<<N):                                  # for 문 반복만 따지면 2^n * n 이자나?
#     subset = []                                        # 차라리 for문을 3개 써서 n^3 을 하는게 더 나을 것 같음 그래도 모든 case에 대해서 조사해볼 수 있음
#     for j in range(N):                                 # n 최대 100일 때 100^3 과 2^100 을 비교해보면 이해 될거고 
#         if i & (1<<j):                                 # 너가 하는건 100개의 원소에서 2개씩 뽑든 6개 씩 뽑든 77개씩 뽑든 모든 case 에 대해서 (모든 부분집합)
#             subset.append(card_list[j])                # 다시 3개인 경우만 추려서 계산 하는 것임.. 
#     if len(subset) == 3:
#         three.append(subset)
# result = []
# for k in range(len(three)):
#    if sum(three[k]) <= M:
#         result.append(sum(three[k]))
# result.sort()
# print(result[-1])


# #######################################################
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0
for i in range(N - 2):
    for j in range(i + 1, N -1):
        for k in range(j + 1, N):
            if result < card_list[i] + card_list[j] + card_list[k] <= M:
                result = card_list[i] + card_list[j] + card_list[k]
print(result)

