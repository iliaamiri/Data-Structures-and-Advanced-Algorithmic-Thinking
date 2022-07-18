n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    t = int(input())
    ans = 0
    for x in a: # calculating number of sad people in n opeartions
        if t > x:
            ans += 1
    print(ans)

# total number of operations is n * q