# N = int(input())
# card = [x for x in range(1, N+1)]
# while len(card) != 1:
#     del card[0]
#     card.insert(N, card[0])
#     del card[0]
# print(card[0])




# del 함수 insert 함수가 O(N) 이여
# while 도 지금 N 번만큼 내부 로직이 도니까 O(N^2) 이겠지?
# https://wayhome25.github.io/python/2017/06/14/time-complexity/ 내장 함수 써도 되는데 내장 함수가 대강 얼마나 시간 잡아먹을지 고려 해야돼
# 즉 다른 대안이 없는데 (무조건 문제에서 요구하는 핵심 로직에서 써야하는데) 구현하기는 싫을 때 내장함수를 써
#  뭐 전처리 과정처럼 얼마 반복안할 것 같을 때는 걍 써도 됨
# 근데 위와 같은 경우에는 충분히 대안이 있을 듯?  예를 들어 insert 대신 append

############## 이것도 시간초과라니

# N = int(input())
# card = [x for x in range(1, N+1)]
# while len(card) != 1:
#     card.pop(0)
#     a = card.pop(0)
#     card.append(a)
# print(card[0])

#####################################

# N = int(input())
# card = [x for x in range(1, N+1)]
# for _ in range(N-1):
#     card.pop(0)
#     a = card.pop(0)
#     card.append(a)
# print(card[0])


#########################################

# N = int(input())
# card = []
# cnt = 0
# while cnt != N:
#     cnt += 1
#     card.append(cnt)

# for _ in range(N-1):
#     card.pop(0)
#     a = card.pop(0)
#     card.append(a)
# print(card[0])

####################
# import sys
# N = int(sys.stdin.readline())
# card = [x for x in range(1, N+1)]
# for _ in range(N-1):
#     card.pop(0)
#     a = card.pop(0)
#     card.append(a)
# print(card[0])


# 덱을 쓰면 되나봄... 이후에 다시 수정합니다...