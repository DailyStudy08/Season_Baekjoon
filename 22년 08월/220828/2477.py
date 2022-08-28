K = int(input())
a = []
b = []
for _ in range(6):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

row = 0
col = 0
row_idx = 0
col_idx = 0
for i in range(6):
    if a[i] in [1, 2]:  
        if b[i] > col:
            col = b[i]
            col_idx = i
    else:
        if b[i] > row:
            row = b[i]
            row_idx = i

result = 0
if (col_idx == 0 and row_idx == 5) or (col_idx == 5 and row_idx == 0):
    result = col * row - b[2] * b[3]
elif col_idx < row_idx:
    result = col * row - b[col_idx-2] * b[col_idx-3]
else:
    result = col * row - b[row_idx-2] * b[row_idx-3]

print(result * K)