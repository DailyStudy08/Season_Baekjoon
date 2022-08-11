N = int(input())
card = [x for x in range(1, N+1)]
while len(card) != 1:
    del card[0]
    card.insert(N, card[0])
    del card[0]
print(card[0])