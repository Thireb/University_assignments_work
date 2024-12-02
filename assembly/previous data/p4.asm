
[org 0x100]

mov al, [num1]
add dl, al
mov al, [num1+1]
add dl, al


mov al, [num2]
add dl, al
mov al, [num2+1]
add dl, al

mov ax, 0x4c00
int 0x21

num1: dw 0x10AB
num2: dw 0x23CD