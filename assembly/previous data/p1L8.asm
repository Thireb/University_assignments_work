
[org 0x100]

mov word [0x0106], 0xABCD    ; move 5 to ax
mov bx, 10   ; move 10 to bx
add ax, bx   ; add bx to ax
mov bx, 15
add ax, bx

mov ax, 0x4c00
int 0x21
