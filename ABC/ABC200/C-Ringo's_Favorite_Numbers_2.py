"""
Created by Y.Azama 2024-07-20
Ref: https://atcoder.jp/contests/abc200/tasks/abc200_c

単純に全探索を行うとO(N^2)となりTLE
数え上げに工夫が必要
⇒ 考え方は解説と同様となっているため、下記コードの詳細については解説を参照
　 解説ではC++にて実装
"""
N = int(input())
A = [int(n) for n in input().split()]
r = [0] * 200
for n in A:
  r[n % 200] += 1

ans = 0
for i in r:
  ans += i * (i - 1) // 2
print(ans)