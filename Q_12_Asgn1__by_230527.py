MOD = 10**9 + 7
P = [0] * 101
P[0] = 1
for k in range(1, 101):
    for i in range(k):
        P[k] = (P[k] + P[i] * P[k-1-i]) % MOD

# Print all P_n from n=1 to n=100
for n in range(1, 101):
    print(f"P_{n} = {P[n]}")