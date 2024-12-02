;Register + offset Addressing
[org 0x100]
 
mov dx, 0
mov cl, 5; count
mov ax, 0010; number to find
mov si, 0

l1:	cmp ax,[num1+si]
	je l2
	add si, 1
	sub cl,1
	jnz l1
	
l2: 	
	mov dx,1
	;mov dx, 0


;mov dx, 1


mov ax, 0x4c00
int 0x21
 
num1: db 5,10,15,20,25  ;[11d +i*2]
;: dw 10