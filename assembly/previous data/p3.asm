[org 0x100]

mov ax, 0008  ;replace xyz with last 4 digits of your roll number. 
mov dx, 42
xor ah, dl
dec ax
inc ax
xor ah, dl

mov ax,0x4c00
int 0x21

