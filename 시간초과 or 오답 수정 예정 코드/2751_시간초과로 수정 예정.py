N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()             #  그냥 sort 해도 시간초과가 나서.. 공부해서 돌아오겠습니다(ㅠㅠ)

for k in num:
    print(k)
    
    # 버블 sort 하면 시간초과 날거여..
    # 그냥 sort 함수 쓰거나 그게 싫은거면 quick sort , merge sort를 구현할 수 있게 공부해야하도록..
