############# 영원한 고통의 시간초과 ##############

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
three = []
for i in range(1<<N):
    subset = []
    for j in range(N):
        if i & (1<<j):
            subset.append(card_list[j])
    if len(subset) == 3:
        three.append(subset)
result = []
for k in range(len(three)):
   if sum(three[k]) <= M:
        result.append(sum(three[k]))
result.sort()
print(result[-1])


#######################################################
