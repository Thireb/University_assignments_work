
[org 0x100]


mov ax, 8

cmp ax, 92
je l1
mov bx, 30

fin: 
	mov ax, 0x4c00
	int 0x21

l1: mov bx, 40
jmp fin