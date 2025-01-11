"""
Created by Y.Azama 2024-12-21
Ref: https://atcoder.jp/contests/abc385/tasks/abc385_b
"""
H, W, X ,Y = map(int, input().split())
M = [list(input()) for _ in range(H)]
T = list(input())
ans = set()
X = X-1
Y = Y-1
for t in T:
  if t == 'U':
    if 0 <= X-1 < H and M[X-1][Y] != '#':
      X = X-1
      if M[X][Y] == "@":
        ans.add((X,Y))
  if t == 'D':
    if 0 <= X-1 < H and M[X+1][Y] != '#':
      X = X+1
      if M[X][Y] == "@":
        ans.add((X,Y))
  if t == 'L':
    if 0 <= Y-1 < W and M[X][Y-1] != '#':
      Y = Y-1
      if M[X][Y] == "@":
        ans.add((X,Y))
  if t == 'R':
    if 0 <= Y+1 < W and M[X][Y+1] != '#':
      Y = Y+1
      if M[X][Y] == "@":
        ans.add((X,Y))
print(X+1, Y+1, len(ans))