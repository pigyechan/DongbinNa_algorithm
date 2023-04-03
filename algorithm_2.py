'''
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
'''
