"""
Created by Y.Azama 2024-11-02
Ref: https://atcoder.jp/contests/abc378/tasks/abc378_c
"""
N = int(input())
A = [int(n) for n in input().split()]

d = {}
#print(t)
B = []
for i in range(N):
  if A[i] in d:
    tmp = d[A[i]] + 1
  else:
    tmp = -1

  B.append(tmp)
  d[A[i]] = i

print(*B)