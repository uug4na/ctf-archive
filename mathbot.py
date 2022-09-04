from pwn import *
import os

host = "64.227.11.108"
port = 5000

c = remote(host, port)
count = 0

while 1:
    count = count + 1
    print(count)
    num = c.recvuntil(b"= ")
    if b"exec" in num:
        if count == 70:
          c.interactive()
        num = num.replace(b" ", b"")
        print(num)
        sliced = str(num[95:])
        print(sliced)
        bodlogo = sliced[-9:]
        print(bodlogo)
        answer = str(eval(bodlogo[:-2]))
        print(answer)
        c.sendline(answer)
        print("YAWCHIHLAASHDE")
    num = num.replace(b" ", b"")
    print(num.decode())
    if b"unknown" in num and b"=" in num:
        bodlogo = num[-9:]
        print(bodlogo)
        answer = str(eval(bodlogo[:-1]))
        print(answer)
        c.sendline(answer)
        print("FIRST DONE:)")
    else:
        answer = str(eval(num[:-1]))
        print(answer)
        c.sendline(answer)
