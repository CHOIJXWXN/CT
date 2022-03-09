n = int(input())

# 스위치 상태
switch_status = list(map(int, input().split()))

# 학생 수
s = int(input())

# 학생들의 정보를 받을 리스트 초기화
info_student = []

# 학생 수만큼 학생들의 정보를 리스트로 받음
for _ in range(s):
    info = list(map(int, input().split()))
    info_student.append(info)

for i in info_student:
    # 남학생일 때
    if i[0] == 1:
        # 카드 순서 j
        for j in range(1, n+1):
            # 카드 순서가 남학생이 받은 숫자의 배수이면
            if j % i[1] == 0:
                # 0을 1로, 1을 0으로
                if switch_status[j-1] == 0:
                    switch_status[j-1] = 1
                else:
                    switch_status[j-1] = 0
    # 여학생일 때    
    elif i[0] == 2:
        # 여학생이 받은 숫자가 끝값일경우
        # 끝값만 바꾸고 다음 학생으로
        if i[1] == n or i[1] == 1:
            if switch_status[i[1]-1] == 0:
                switch_status[i[1]-1] = 1
            else:
                switch_status[i[1]-1] = 0
            continue
         
        # 일단 여학생이 받은 숫자의 스위치 바꿈
        if switch_status[i[1]-1] == 0:
            switch_status[i[1]-1] = 1
        else:
            switch_status[i[1]-1] = 0
  
        k = 1
        # 여학생이 받은 숫자에 해당하는 스위치 앞뒤로 같은 값인지 계산하기 위해
        # 반복문을 돌리면서 점점 범위를 넓혀갈텐데
        # 범위가 0보다 아래의 숫자까지 확장되거나
        # 범위가 n보다 큰 숫자까지 확장될 경우
        while i[1]-1 - k >= 0 and i[1]-1 + k < n:
            if switch_status[i[1]-1 - k] == switch_status[i[1]-1 + k]:
                if switch_status[i[1]-1 - k] == 0:
                    switch_status[i[1]-1 - k] = 1
                else:
                    switch_status[i[1]-1 - k] = 0

                if switch_status[i[1]-1 + k] == 0:
                    switch_status[i[1]-1 + k] = 1
                else:
                    switch_status[i[1]-1 + k] = 0 
                
                k += 1
            else:
                k += 1

for i in range(0, len(switch_status), 20):
    print(*switch_status[i:i+20])