'''
그리디 알고리즘
#1
N, K = map(int, input().split())
cnt = 0

while N != 1:
    if N % K == 0:
        N = N / K
        cnt += 1

    else:
        N = N - 1
        cnt += 1

print(cnt)

#2
S = input()
b = 0
for i in range(len(S)-1):
    a = int(S[i])
    if a == 0:
        b += int(S[i+1])
    else:
        b *= int(S[i+1])

print(b)

#3
N = int(input())
num = list(map(int, input().split()))
num.sort(reverse = True)
ind, cnt = 0, 0

while ind < len(num):
    a = num[ind]
    cnt += 1
    ind += a

print(cnt)
'''

'''
#1
x, y = 1, 1

N = int(input())
din = list(map(str, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dr = ['L', 'R', 'U', 'D']

for i in din:
    for j in range(len(dr)):
        if i == dr[j] and dx[j] + x > 0 and dy[j] + y > 0 and dx[j] + x < N and dy[j] + y < N:
            x += dx[j]
            y += dy[j]
        else:
            continue

print(f"{x} {y}")

#2
N = int(input())

cnt = 0
for i in range(N+1):
    for j in range(60):
        for m in range(60):
            clock = str(i) + str(j) + str(m)
            if '3' in clock:
                cnt += 1

print(cnt)

#3

pos = input()
did = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = int(pos[1])
y = pos[0]

for k, v in did.items():
    if k == y:
        y = v

cnt = 0

dm = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in dm:
    if x + i[0] < 1 or x + i[0] > 8 or y + i[1] < 1 or y + i[1] > 8:
        continue
    else:
        cnt += 1

print(cnt)
'''
#4

S = list(input())
a = []
b = 0

for i in S:
    if i.isalpha():
        a.append(i)
    else:
        b += int(i)

a.sort()
a.append(str(b))
print(''.join(a))