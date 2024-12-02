[org 0x100]

jmp here
array: dw 4,6,8,6,3


switch:
        mov si, [array+bx+2]
		mov ax, [si]
        ret


comparearray:     
                cmp si,[array+bx+2]
                jnbe switch
                add bx, 2
                sub cx, 1
                jae comparearray
                ret

here:    mov bx, 0
         mov cx, 5
         mov si, [array+bx]
         call comparearray

mov ax, 0x4c00
int 0x21