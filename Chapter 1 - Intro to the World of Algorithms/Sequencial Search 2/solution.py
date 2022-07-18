firstLine = input().split()

# n is the length of A
n = int(firstLine[0])
# q is the length of X
q = int(firstLine[1])

secondLine = input().split()

# A is the first list a[i]
A = []
for i in range(0, n):
    A.append(int(secondLine[i]))

# X is the second list x[i]
X = []
for i in range(0, q):
    X.append(int(input()))


maximumNum = max(A)

M = []
K = []

for i in range(0, maximumNum):
    M.append(int(0))
    K.append(int(0))

for i in A:
    M[i - 1] += 1

for i in range(0, maximumNum):
    previousIndexInK = i - 1
    if previousIndexInK == -1:
        previousIndexInK == 0
    K[i] = K[i - 1] + M[i]

answers = []

for x in X:
    if x > maximumNum:
        answers.append(n)
    elif x - 2 == -1:
        answers.append(0)
    else:
        answers.append(K[x - 2])

for i in answers:
    print(i)