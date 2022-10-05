def solution(m, musicinfos):
    answer = ''
    music_title = []
    liric = []
    minutes = []
    for i in range(len(musicinfos)):
        start, end, title, lir = musicinfos[i].split(',')
        start_clock, start_min = map(int, start.split(':'))
        end_clock, end_min = map(int, end.split(':'))
        min = (end_clock - start_clock) * 60 + end_min - start_min
        minutes.append(min)
        i = 0
        lirl = ''
        while i < min:
            lirl += lir[i % len(lir)]
            if (i + 1) % len(lir) < len(lir) and lir[(i + 1) % len(lir)] == '#':
                min += 1
            i += 1
        music_title.append(title)
        liric.append(lirl)
    print(music_title)
    print(liric)
    result = []
    for k in range(len(liric)):
        i = j = 0
        while j < len(m) and i < len(liric[k]):
            if liric[k][i] != m[j]:
                i = i - j
                j = -1
            i += 1
            j += 1
            if j == len(m):
                if i < len(liric[k]) and liric[k][i] == '#':
                    print(liric[k][i])
                    j = 0
                else:
                    result.append((k, minutes[k]))
    result_idx = 0
    result_min = 0
    if result:
        for el in result:
            if el[1] > result_min:
                result_min = el[1]
                result_idx = el[0]
        answer = music_title[result_idx]
    else:
        answer = '(None)'
    return answer