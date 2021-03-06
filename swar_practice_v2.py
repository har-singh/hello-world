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
      break
  print()

def render_pattern_reverse(pattern):
  for i in range(len(base)):
    for j in range(len(pattern)):
      index = i + pattern[j] - 1
      reverse_index = -(index + 1)
#      print(reverse_index, end='')
      print(base[reverse_index], end='')
    print()
    if max(pattern) + i >= len(base):
      break
  print()

def reaz_func(length=3):
  #default is 1-2-3
  pattern_list = []
  for i in range(length):
    pattern_list.append(i+1)
  return(pattern_list)



if __name__ == "__main__":
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧")
  render_pattern([1])
  render_pattern_reverse([1])
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੨")
  render_pattern([1, 2, 1])   # ਸਾਰੇਸਾ 1-2-1
  render_pattern_reverse([1, 2, 1])
#
  for i in range(3,8):
    print(f'ਸਰਗਮ ਰਿਆਜ਼  {i}')
    render_pattern(reaz_func(i))   # ਸਾਰੇਗਾ 1-2-3
    render_pattern_reverse(reaz_func(i))   # ਸਾਰੇਗਾ 1-2-3
    time.sleep(1)
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੮")
  render_pattern([1, 3])      # ਸਾਰੇ 1-3
  render_pattern_reverse([1, 3])
