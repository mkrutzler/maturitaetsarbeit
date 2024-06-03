; Basically sets up the magic number for grub

global loader ; the entry symbol for ELF
extern main

MAGIC_NUMBER equ 0x1BADB002
FLAGS equ 0x0
CHECKSUM equ -MAGIC_NUMBER
KERNEL_STACK_SIZE equ 4096

section .bss
align 4
kernel_stack:
  resb KERNEL_STACK_SIZE


section .text
align 4
  dd MAGIC_NUMBER
  dd FLAGS
  dd CHECKSUM


loader:
  mov esp, kernel_stack + KERNEL_STACK_SIZE
  call main

  mov ebx, 0xBABABABA


.loop:
  jmp .loop

