[org 0x100]


mov dl, num

add dl, [num + 1]
add dl, [num + 2]
add dl, [num + 3]
	


mov ax, 0x4c00
int 0x21

num: db 5,9,7,4