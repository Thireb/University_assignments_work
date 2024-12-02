
[org 0x100]
 

mov cx, 5
mov ax, 0

l1: mov ax, cx
	sub cx,1
	jnz l1


mov ax, 0x4c00
int 0x21
 
num1: dw 5,10,15,20,25,5,10,15,20,25  ;[11d +i*2]
total: dw 0