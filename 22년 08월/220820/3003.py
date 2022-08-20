chess_piece = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
for i in range(len(chess_piece)):
    chess_piece[i] -= piece[i]
print(*chess_piece)