def solution(m, musicinfos):
    answer = ''
    music_title = []
    liric = []
    for i in range(len(musicinfos)):
        start, end, title, lir = musicinfos[i].split(',')
        start_clock, start_min = map(int, start.split(':'))
        end_clock, end_min = map(int, end.split(':'))
        min = (end_clock - start_clock) * 60 + end_min - start_min
        i = 0
        while i < min:
            lir += lir[i]
            if lir[i] == '#':
                min += 1
            i += 1
        music_title.append(title)
        liric.append(lir)
    print(music_title)
    print(liric)

    return answer