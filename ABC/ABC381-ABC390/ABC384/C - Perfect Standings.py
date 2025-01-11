"""
Created by Y.Azama 2024-12-14
Ref: https://atcoder.jp/contests/abc384/tasks/abc384_c
"""
V = [int(n) for n in input().split()]
dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
P = ['ABCDE','BCDE','ACDE','ABDE','ABCE','ABCD','CDE','BDE','ADE','BCE','ACE','BCD','ABE','ACD','ABD','ABC','DE','CE','BE','CD','AE','BD','AD','BC','AC','AB','E','D','C','B','A']

ans = []
for p in P:
  S = list(p)
  v = 0
  for s in S:
    v += V[dic[s]]
  ans.append([p, v])
ans = sorted(ans, key=lambda x: x[0])
sorted_ans = sorted(ans, key=lambda x: x[1], reverse=True)
for k in sorted_ans:
  print(k[0])