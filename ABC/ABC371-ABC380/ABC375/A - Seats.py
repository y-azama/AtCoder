"""
Created by Y.Azama 2024-10-12
Ref: https://atcoder.jp/contests/abc375/tasks/abc375_a
"""
N = int(input())
S = input()
ans = 0
for i in range(0,N-2,1):
  if S[i] == S[i+2] == '#' and S[i+1] == '.': ans += 1
print(ans)