
[org 0x100]

mov cx, 5    ; move 5 to ax
mov dx, 10   ; move 10 to bx
add cx, dx   ; add bx to ax
mov dx, 15
add cx, dx

mov ax, 0x4c00
int 0x21
