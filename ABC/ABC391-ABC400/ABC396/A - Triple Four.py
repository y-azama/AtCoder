"""
Created by Y.Azama 2025-03-09
Ref: https://atcoder.jp/contests/abc396/tasks/abc396_a
"""
N = int(input())
A = input().split()
ans = 'No'
for i in range(N-2):
  if A[i] == A[i+1] == A[i+2]:
    ans = 'Yes'
    break
print(ans)