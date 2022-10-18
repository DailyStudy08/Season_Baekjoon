def solution(msg):
    answer = []
    word_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
                 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
                 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
                 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    print(msg[:-1])
    idx = 0
    while idx < len(msg):
        temp_idx = idx + 1
        n = msg[idx]
        temp = n
        if temp_idx < len(msg):
            temp += msg[temp_idx]
        while temp in word_dict:
            temp_idx += 1
            if temp_idx < len(msg):
                temp += msg[temp_idx]
            else:
                temp += '0'
        if temp_idx - 1 > idx:
            n = temp[:-1]
        answer.append(word_dict[n])
        word_dict[temp] = len(word_dict) + 1
        idx += temp_idx - idx
    return answer

print(solution(input()))