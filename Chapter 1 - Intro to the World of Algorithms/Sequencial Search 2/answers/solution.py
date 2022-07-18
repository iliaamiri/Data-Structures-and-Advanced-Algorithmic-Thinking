MAXN = 1000010

n, q = map(int, input().split())
a = list(map(int, input().split()))

cnt = [0] * MAXN

for x in a:
    cnt[x] += 1

#cnt[x] is number of occurness of x in a

dp = [0]

for x in range(MAXN):
    dp.append(dp[-1] + cnt[x])

#dp[x] is answer of problem for d_i = x

for i in range(q):

    d = int(input())
    print(dp[d])

# total number of operations is MAXN + q + n