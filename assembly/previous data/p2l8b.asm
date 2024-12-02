[org 0x100]

mov si, num
mov cx, 4
mov di, 0
mov dl, 0

z:	add dl, [si]
	add si, 1
	sub cx, 1
	jnz z


mov ax, 0x4c00
int 0x21

num: db 2,5,7,9