#!/usr/bin/python3
# https://note.nkmk.me/en/python-break-nested-loops/
# https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08

#-----HS 22May19-----

import time

base = ['ਸਾ', 'ਰੇ', 'ਗਾ', 'ਮਾ', 'ਪਾ', 'ਧਾ', 'ਨੀ', 'ਸਾ']

def render_pattern(pattern):
  for i in range(len(base)):
    for j in range(len(pattern)):
      index = i + pattern[j] - 1
      #print(index, end='')
      print(base[index], end='')
    print()
    if max(pattern) + i >= len(base):
      print('BREAK')
      break

def render_pattern_reverse(pattern):
  print(f'{pattern}')
  for i in range(len(base)):
    for j in range(len(pattern)):
      index = i + pattern[j] - 1
      reverse_index = -(index + 1)
#      print(reverse_index, end='')
      print(base[reverse_index], end='')
    print()
    if max(pattern) + i >= len(base):
      print('BREAK')
      break


if __name__ == "__main__":
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧")
  render_pattern([1])
  render_pattern_reverse([1])
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੨")
  render_pattern([1, 2, 1])   # ਸਾਰੇਸਾ 1-2-1
  render_pattern_reverse([1, 2, 1])
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੩-੭")
  render_pattern([1, 2, 3])   # ਸਾਰੇਗਾ 1-2-3
  render_pattern_reverse([1, 2, 3])   # ਸਾਰੇਗਾ 1-2-3
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੮")
  render_pattern([1, 3])      # ਸਾਰੇ 1-3
  render_pattern_reverse([1, 3])
