[org 0x100]

jmp start

arr: dw 5,7,2,1,0
flag: db 0

start:	
		mov bx, 0
		mov byte [flag], 0
		
innerloop:
			mov ax, [arr+bx]
			cmp ax, [arr+bx+2]
			jbe noswap
			mov dx, [arr+bx+2]
			mov [arr+bx+2], ax
			mov [arr+bx], dx
			mov byte [flag], 1
			
noswap: 
		add bx, 2
		cmp bx, 8
		jne innerloop
		cmp byte[flag], 1
		je start
		
mov ax, 0x4c00
int 0x21
