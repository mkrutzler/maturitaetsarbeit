global outb

; outb - send a byte to an I/O Port
  ; stack:  [esp + 8]: data byte
  ;         [esp + 4]: the I/O port
  ;         [esp    ]: return adr

outb:
  mov al, [esp + 8]
  mov dx, [esp + 4]
  out dx, al
  ret
