S = "abaab"
N = len(S)
LPS = [0] * N
LPS[0] = 0

for i in range(1, N):

    X = LPS[i-1]

    while S[i] != S[X]:
        if X == 0:
            X = -1
            break
        X = LPS[X-1]

    LPS[i] = X + 1

print(LPS)
