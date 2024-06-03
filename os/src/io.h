#ifndef INCLUDE_IO_H
#define INCLUDE_IO_H

/** outb:
 *    Sends a byte to an I/O Port. (Defined in io.s)
 *
 *    @ param port: The I/O Port Address
 *    @ param data: The Byte to send
 */

void outb(unsigned short port, unsigned char data);

#endif /* INCLUDE_IO_H */
