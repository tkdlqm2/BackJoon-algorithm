# 그리드
# 컨셉 1 : 문제 조건에 맞춰서 최대 만들 수 있는 팀을 만든다.
# 컨셉 2 : 최대로 만든 팀에서 인턴을 보낼 때 쪼게지는 팀의 갯수를 구한다


# param1 : 인턴 수
# return : 인턴 수에 따라 없앨 팀의 수를 리턴

def intercrew(n):
    if n%3 == 0:
        return int(n/3)
    else:
        if int(n/3) == 0:
            return 1
        else:
            return int(n/3) + 1


# param1 : 여자
# param2 : 남자
# param3 : 인턴 수
# return : 문제의 정답

def makeTeam(w,m,n):
    if m*2 == w:
        return m - intercrew(n)

    elif m*2 < w:
        if n - (w - (2*m)) < 0: # 여자 인원으로 인턴보내는게 충당이 되면
            return m
        else: # 팀 삭감
            remainer = n - (w - (2 * m)) # 남은 여자 인원으로 충당
            return m - intercrew(remainer)

    else:
        if n - (m - int(w/2)) < 0: # 남자 인원으로 인턴 충당 가능
            return int(w/2)
        else:
            remainer = n - ((m - int(w/2)) + w%2) # 팀을 이루고 남은 여자 인원 고려
            return int(w/2) - intercrew(remainer)


N,M,K = input().split()
N,M,K = int(N),int(M),int(K)

print(int(makeTeam(N,M,K)))
