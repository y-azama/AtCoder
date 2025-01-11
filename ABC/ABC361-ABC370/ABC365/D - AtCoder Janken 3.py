"""
Created by Y.Azama 2024-10-28
Ref: https://atcoder.jp/contests/abc365/tasks/abc365_d
"""
N = int(input())
s = input()
R = 0
S = 1
P = 2
dp = [[0,0,0] for _ in range(N+1)]

for i in range(N):
  if s[i] == 'R':
    dp[i+1][R] = max(dp[i][S], dp[i][P])
    dp[i+1][P] = max(dp[i][R], dp[i][S]) + 1
  elif s[i] == 'S':
    dp[i+1][R] = max(dp[i][S], dp[i][P]) + 1
    dp[i+1][S] = max(dp[i][R], dp[i][P])
  elif s[i] == 'P':
    dp[i+1][P] = max(dp[i][R], dp[i][S])
    dp[i+1][S] = max(dp[i][R], dp[i][P]) + 1
print(max(dp[-1]))