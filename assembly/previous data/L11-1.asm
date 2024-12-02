
[org 0x100]

mov ax, 62

cmp ax, 92
je l1
cmp ax, 82
je l2
cmp ax, 72
je l3
cmp ax, 62
je l4

l1: mov bx, 40
	jmp fin
l2: mov bx, 30
	jmp fin
l3: mov bx, 20
	jmp fin
l4: mov bx, 10
	jmp fin

fin: 
	mov ax, 0x4c00
	int 0x21

