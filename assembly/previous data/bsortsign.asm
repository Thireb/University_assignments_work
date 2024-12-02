[org 0x100]

jmp start

arr: db  5,7,2, -1,0
flag: db 0

start:	
		mov  bx, 0
		mov byte [flag], 0
		
innerloop:
			mov al, [arr+bx]
			cmp al, [arr+bx+1]
			jle noswap
			mov dl, [arr+bx+1]
			mov [arr+bx+1], al
			mov [arr+bx], dl
			mov byte [flag], 1
			
noswap: 
		add bx, 1
		cmp bx, 4
		jne innerloop
		cmp byte[flag], 1
		je start
		
mov ax, 0x4c00
int 0x21
