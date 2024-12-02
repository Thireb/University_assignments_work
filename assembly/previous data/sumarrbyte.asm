[org 0x100]

arr: db  5,7,2,1,0
mov bl, 0
mov al, 0

sum: db 0

main:	add al, [arr + bx]
		add bl, 1
		cmp bl, 5
		jne main

mov [sum], al
	
mov ax, 0x4c00
int 0x21
