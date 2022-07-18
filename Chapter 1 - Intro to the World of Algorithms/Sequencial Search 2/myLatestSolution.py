# Getting input from the Stdin
firstLine = str(input()).split()

nLength = int(firstLine[0])
qLength = int(firstLine[1])

n = str(input()).split()

q = []

for i in range(qLength):
    q.append(input())

# solution:
maximumNumberInN = int(max(n))

M = [0] * maximumNumberInN

for n_i in n:
    n_i = int(n_i)
    M[n_i - 1] += 1

#print(M)

Kir = [0] * maximumNumberInN
for k_i in range(0, maximumNumberInN):
    k_i = int(k_i)
    indexKireGhabli = k_i - 1
    if indexKireGhabli == -1:
        indexKireGhabli = 0
    
    Kir[k_i] = Kir[indexKireGhabli] + M[k_i]

# print(Kir)


for x_i in q:
    x_i = int(x_i)
    if x_i > maximumNumberInN:
        print(nLength)
    else:
        if x_i - 2 < 0:
            print(0)
        else:
            print(Kir[x_i - 2])