[org 0x100]

mov cx, [num1]         
mov dx, [num2]   
add cx, dx   
mov dx, [num3]   ;mem to reg
add cx, dx
mov [num4],cx    ;reg to mem

mov ax, 0x4c00
int 0x21

num1: dw  5
num2: dw  10 
num3: dw  15
num4: dw  0
