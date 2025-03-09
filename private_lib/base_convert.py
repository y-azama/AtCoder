"""
基数変換
"""
# 10 -> n
def base_n(num, base):
  pow = 0
  while num >= base**pow:
    pow += 1
  ans = []
  while pow > 0:
    pow -= 1
    ans.append(num//(base**pow))
    num -= ans[-1]*(base**pow)
  
  return int(''.join(map(str,ans)))

# n -> 10
def base_10(num, base):
  S = str(num)
  ans = 0
  pow = 1
  for i, s in enumerate(S[::-1]):
    ans += int(s)*pow
    pow *= base
  return ans
