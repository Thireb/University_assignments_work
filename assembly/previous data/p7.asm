[org 0x100]
 
mov si, num1 
mov cx, 10
mov ax, 0

l1:	add ax,[si]
	add si,2       
	sub cx,1   
 	jnz l1

 mov [total], ax





mov ax, 0x4c00
int 0x21

num1: dw 5,10,15,20,25,5,10,15,20,25
total: dw 0