"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc201/tasks/abc201_c
"""
S = input()
N = 10 ** 4
tmp = ''
ans = 0
not_flg = False
for i in range(N):
  tmp = str(i).zfill(4)
  not_flg = False

  for j in range(10):
    if S[j] == 'o' and str(j) not in tmp:
      not_flg = True
      break
    elif S[j] == 'x' and str(j) in tmp:
      not_flg = True
      break

  if not_flg == False:
    ans += 1

print(ans)