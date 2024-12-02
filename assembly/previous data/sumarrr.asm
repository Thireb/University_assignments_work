[org 0x100]


arr: dw  5,7,2,1,0
mov bx, 0
mov ax, 0
sum: dw 0
start:	
		
		add ax, [arr + bx]
		add bx, 2
		cmp bx, 10
		jne start

mov [sum], ax		
mov ax, 0x4c00
int 0x21
