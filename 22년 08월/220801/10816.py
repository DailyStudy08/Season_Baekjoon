import sys
N = input()
for sg in sys.stdin:
    sg_lst = sg.split()
    break
M = int(input())
for card in sys.stdin:
    card_lst = card.split()
    break
for i in card_lst:
    print(sg_lst.count(i), end=' ')