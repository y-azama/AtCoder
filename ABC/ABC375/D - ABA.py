"""
Created by Y.Azama 2024-10-26
Ref: https://atcoder.jp/contests/abc375/tasks/abc375_d
"""
S = input()
ans = 0
cnt = [0] * 26
idx_sums = [0] * 26

for i in range(len(S)):
  ch = ord(S[i]) - 65
  ans += cnt[ch] * i - idx_sums[ch] - cnt[ch]
  cnt[ch] += 1
  idx_sums[ch] += i
print(ans)