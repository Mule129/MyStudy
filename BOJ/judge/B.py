n, m, k = map(int, input().split())
b_computer = list(map(int, input().split()))

for i in range(m):
    log = list(map(int, input().split()))

# 들어온 로그의 시작시간은 특정 컴퓨터가 감염이 된 시점이다. -> 이게 힌트인듯?
# a->b와 같이 한번에 한대의 컴퓨터와만 주고받을 수만 있다.
#   감염이 순차적으로 하나씩 일어남을 알 수 있다.
# 감염이 된 컴퓨터를 추적하기 위해서는, k개의 감염된 컴퓨터와 주고받은 기록이 있어야 한다.
# n번 컴퓨터가 감염됐을 것을 가정하고 문제를 풀면 어떨까?
# 감염요인을 지워나가는 방식?