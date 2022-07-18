# Getting input from the Stdin
firstLine = str(input()).split()

nLength = int(firstLine[0])
qLength = int(firstLine[1])

n = str(input()).split()

q = []

for i in range(qLength):
    q.append(input())

# solution:
for x_i in q:
    answer_i = 0
    for a_i in n:
        if int(x_i) > int(a_i):
            answer_i += 1
    print(answer_i)