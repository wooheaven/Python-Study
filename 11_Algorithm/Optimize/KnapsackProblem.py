# 물건 N 개, 배낭 총무게 K kg
print(f'물건의 갯수 N 과 배낭의 총무게 K kg을 입력하세요.')
n, k = map(int, input().split()) # 4 7 입력
print(f'물건 n 개 = {n}')
print(f'배낭 총무게 K kg = {k}')

# index 0 은 없는 물건으로 보고, 가치가 0인 것으로 정의한다.
# 즉 0번(없는) 물건은 데이터상 존재하지만 가치는 0으로 정의한다.
lst=[[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]
# 물건 n 개의, 번호별 가치
for i in range(1, n+1):
    print(f'{i}번째 물건의 무게는 {lst[i][0]} 가치는 {lst[i][1]} 입니다.')
    # lst.append(list(map(int, input().split())))
    print(lst[i])
print(lst)

# dp 초기화
dp = [[None]*(k+1) for _ in range(n+1)]
print(dp)

# 0번(없는) 물건으로 최대 가치가 0(없는) 경우
for j in range(0, k+1):
    dp[0][j] = 0
print(dp)

# 배냥의 용량이 0 kg으로 최대 가치가 0(없는)인 경우
for i in range(1, n+1):
    dp[i][0] = 0
print(dp)

for i in range(1, n+1):              # i번째 물건
    for j in range(1, k+1):          # 배낭의 적재가능 최대 무게가 j
        weight = lst[i][0]           # i번째 물건의 무게
        value = lst[i][1]            # i번째 물건의 가치
        if j < weight:               # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
            print(dp)
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            print(dp)
print(dp[n][k])