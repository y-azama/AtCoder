"""
Created by Y.Azama 2024-10-19
Ref: https://atcoder.jp/contests/abc376/tasks/abc376_b
"""
N = int(input())
A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
B.append(0)
cnt = 0
ans = 0
#print(*A)
#print(*B)
for i, a in enumerate(A):
  #print(a, B[i-cnt])
  if a <= B[i-cnt]: continue
  cnt += 1
  ans = a
  if cnt > 1: break

if cnt == 0:
  print(A[-1])
elif cnt > 1:
  print(-1)
else:
  print(ans)
