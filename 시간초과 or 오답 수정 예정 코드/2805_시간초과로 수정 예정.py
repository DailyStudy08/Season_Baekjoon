N,M = map(int, input().split())
lst = list(map(int, input().split()))
wood = sorted(lst)
a = wood[-1] -1
c = 0
while c < M:
    for w in wood:
        if w - a > 0:    # 큰 수를 맞닥트렸을때 (문제 조건에서 M,N) 이분 탐색을 떠올리는게 좋은 것 같습니다.
            c += 1       # 저도 잘 모르지만... 이분 탐색 한 번 찾아보시는 것을 추천 드립니다.
    a -= 1
print(a + 1)      
