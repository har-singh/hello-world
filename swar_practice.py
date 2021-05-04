#!/usr/bin/python3

#-----HS 14May19-----

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

#------------------------------------------

def reaz8():
  for i in range(len(base)):
    print(base[i], end=' ')
    print(base[i+2], end=' ')
    print()
    if (i+2 == 7):
      break
  #
  for i in range(len(base)):
    index = -i-1
    print(base[index], end=' ')
    print(base[index-2], end=' ')
    print()
    if (i+2 == 7):
      break

#------------------------------------------

def reaz9():
  for i in range(len(base)):
    print(base[i], end=' ')
    print(base[i+1], end=' ')
    print(base[i], end=' ')
    print(base[i+1], end=' ')
    print(base[i+2], end=' ')
    print()
    if (i+2 == 7):
      break
  #
  for i in range(len(base)):
    index = -i-1
    print(base[index], end=' ')
    print(base[index-1], end=' ')
    print(base[index], end=' ')
    print(base[index-1], end=' ')
    print(base[index-2], end=' ')
    print()
    if (i+2 == 7):
      break

#------------------------------------------

def reaz10():
  for i in range(len(base)):
    print(base[i], end=' ')
    print(base[i+2], end=' ')
    print(base[i+1], end=' ')
    print(base[i], end=' ')
    print()
    if (i+2 == 7):
      print(base[i+2])
      break
  #
  for i in range(len(base)):
    index = -i-1
    print(base[index], end=' ')
    print(base[index-2], end=' ')
    print(base[index-1], end=' ')
    print(base[index], end=' ')
    print()
    if (i+2 == 7):
      print(base[i+2])
      break

#------------------------------------------

def reaz11():
  for i in range(len(base)):
    print(base[0], end=' ')
    print(base[i+1], end=' ')
    print()
    if (i+1 == 7):
      break
  #
  for i in range(len(base)):
    index = -i-1
    print(base[7], end=' ')
    print(base[index-1], end=' ')
    print()
    if (i+1 == 7):
      break

#------------------------------------------

def reaz12():
  for i in range(len(base)):
    for j in range(2):
      print(base[i], end=' ')
      print(base[i+1], end=' ')
      print(base[i+2], end=' ')
    print(base[i], end=' ')
    print(base[i+2], end=' ')
    print()
    if (i+2 == 7):
      break
  #
  for i in range(len(base)):
    index = -i - 1
    for j in range(2):
      print(base[index], end=' ')
      print(base[index-1], end=' ')
      print(base[index-2], end=' ')
    print(base[index], end=' ')
    print(base[index-2], end=' ')
    print()
    if (i+2 == 7):
      break

#------------------------------------------


if __name__ == "__main__":
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧")
  reaz1()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੨")
  reaz2()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੩-੭")
  reaz_regular()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੮")
  reaz8()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੯")
  reaz9()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧੦")
  reaz10()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧੧")
  reaz11()
#
  print("ਸਰਗਮ ਰਿਆਜ਼ ੧੨")
  reaz12()
#
