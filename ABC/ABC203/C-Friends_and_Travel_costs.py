"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc203/tasks/abc203_c
"""
N, K = map(int, input().split())
friends = []
a, b = 0, 0
for _ in range(N):
  a, b = map(int, input().split())
  friends.append([a, b])
  
friends = sorted(friends, key=lambda x: x[0])
# 現在位置から次の友達の場所まで移動できるかどうかを判定
money = K
position = 0
f_num = 0
for i, j in friends:
  if money - (i - position) < 0:
    break
  money = money - (i - position) + j
  position = i

position += money
print(position)
