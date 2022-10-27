# -*- coding: utf-8 -*-
# 警告： 注意執行本程序前機台必須先做回原點動作，以免過行程
# WARNING : Must go to machine home position before run this program

import time
import serial

com = serial.Serial('COM12', 38400)
com.write(b'PPS0=9600\r\n')
time.sleep(0.5)
com.write(b'PPS1=9600\r\n')
time.sleep(0.5)
com.write(b'PPS2=9600\r\n')
time.sleep(0.5)
num = 200
while(num > 0):
    print(num)
    com.write(b'MVP0=-18000\r\n')
    time.sleep(3)
    print('.')
    com.write(b"MVP0=18000\r\n")
    time.sleep(3)
    print('.')
    com.write(b"MVP1=-20000\r\n")
    time.sleep(4)
    print('.')
    com.write(b"MVP1=20000\r\n")
    time.sleep(4)
    print('.')
    com.write(b"MVP2=-20000\r\n")
    time.sleep(3)
    print('.')
    com.write(b"MVP2=20000\r\n")
    time.sleep(3)
    num = num - 1

com.close()
print("done.\r\n")
