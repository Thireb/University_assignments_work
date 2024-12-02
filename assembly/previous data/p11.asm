;Register + offset Addressing
[org 0x100]
 
mov dx, 0
mov cx, 10
mov ax, 20; number to find
mov bx, 0

l1:	cmp ax,[num1+bx]
	je l2
	add bx, 2
	sub cx,1
	jnz l1
	
l2: 	
	mov dx,1
	;mov dx, 0


;mov dx, 1


mov ax, 0x4c00
int 0x21
 
num1: dw 5,10,15,20,25,5,10,15,20,25  ;[11d +i*2]
;: dw 10