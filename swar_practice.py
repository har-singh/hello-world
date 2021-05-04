# HS 03May21

import time

base = ['ਸਾ', 'ਰੇ', 'ਗਾ', 'ਮਾ', 'ਪਾ', 'ਧਾ', 'ਨੀ', 'ਸਾ']

def reaz1():
  # 1-2-3-4
  for i in range(len(base)):
    print(base[i], end=' ')
  print()
  #
  for i in range(len(base)):
    print(base[-(i)-1], end=' ')

#------------------------------------------

def reaz2():
  # 1-2-1
  for i in range(len(base)):
    print(base[i], end=' ')
    print(base[i+1], end=' ')
    print(base[i], end=' ')
    print()
    if (i == 6):
      print(base[i+1], end=' ')
      print()
      break
  #
  for i in range(len(base)):
    print(base[abs(i-7)], end=' ')
    print(base[abs(i-6)], end=' ')
    print(base[abs(i-7)], end=' ')
    print()
    if (i == 6):
      print(base[i+1], end=' ')
      print()
      break

#------------------------------------------

def reaz_func(length=3):
  for i in range(len(base)):
    for j in range(length):
      index = i + j
      print(base[index], end=' ')
    print()
    if (i+j == 7):
      break
#
  for i in range(len(base)):
    for j in range(length):
      index = -(i + j) - 1 # negative index for inverse scale
      print(base[index], end=' ')
    print()
    if (i+j == 7):
      break

def reaz_regular():
  for i in range(3,8):
    reaz_func(i)
    time.sleep(1)
    print()
