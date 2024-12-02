;Register + offset Addressing
[org 0x100]
 
mov bx, 0
mov cx, 10
mov ax, 0

l1:	add ax,[num1+bx]
	add bx,2       
	sub cx,1   
 	jae l1    ; jump if destination is not zero jnz/

 mov [total], ax


mov ax, 0x4c00
int 0x21
 
num1: dw 5,10,15,20,25,5,10,15,20,25  ;[11d +i*2]
total: dw 0