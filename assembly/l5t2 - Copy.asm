
[org 0x100]

mov bx,0
mov al,0

loop:
	add al,[array+bx]
	cmp bx,4
	jz end
	add bx,1
	jmp loop


end:
mov [sum], al

mov ax, 0x4c00
int 0x21

array: db 1,2,3,4,5
sum: db 0
