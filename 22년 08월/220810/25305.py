N, k = map(int, input().split())
score = list(sorted(map(int, input().split())))
print(score[-k])