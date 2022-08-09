# ###     기존의 실패 내역  
# import sys
# N = input()
# for sg in sys.stdin:
#     sg_lst = sg.split()
#     break
# M = int(input())
# for card in sys.stdin:
#     card_lst = card.split()
#     break
# for i in card_lst:
#     print(sg_lst.count(i), end=' ')

###        ↓ 지용님이 도움 주신 주석
    
# # 한 개의 input 도 sys 를 활용하는 것이 빠른 것으로 알고 있습니다.
# # count 함수는 O(n) 입니다.
# # 꽤 시간을 줄여야 하기 때문에  밑의 for 문들은 join 과 list comprehension 등을 활용 하거나 빈 string 에다가 추가하는 방식이 어떨까 싶습니다.
# # 파이썬의 dictionary 는 해쉬맵의 특성을 가집니다. 해쉬맵의 접근은 상수 시간안에 가능한게 특징입니다.

####            ↓      sys로 여는 건 배웠지만 입력은 아직 안 배운 것 같아
####                   일단 input은 그대로 사용하고 대신 dictionary를 통한 접근으로 수정하여 성공



N = int(input())
s_card = list(map(int, input().split()))
M = int(input())
c_card = list(map(int, input().split()))

for_result = {}

for card in s_card:
    if card in for_result:
        for_result[card] += 1
    else:
        for_result[card] = 1

for el in c_card:
    print(for_result.get(el, 0), end=' ')