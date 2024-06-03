#include "io.h"

/* Setup Variables */

#define FRAMEBUFFER_BASE_ADDRESS 0x000B8000
#define FRAMEBUFFER_LENGTH 80 * 25 /* bit of one member times columns times rows */
char *fb = (char *) FRAMEBUFFER_BASE_ADDRESS;


#define FB_COLOR_BLACK 0
#define FB_COLOR_BLUE 1
#define FB_COLOR_GREEN 2
#define FB_COLOR_CYAN 3 #define FB_COLOR_RED 4
#define FB_COLOR_MAGENTA 5
#define FB_COLOR_BROWN 6
#define FB_COLOR_LIGHT_GREY 7
#define FB_COLOR_DARK_GREY 8
#define FB_COLOR_LIGHT_BLUE 9
#define FB_COLOR_LIGHT_GREEN 10
#define FB_COLOR_LIGHT_CYAN 11
#define FB_COLOR_LIGHT_RED 12
#define FB_COLOR_LIGHT_MAGENTA 13
#define FB_COLOR_LIGHT_BROWN 14
#define FB_COLOR_WHITE 15


/* Setup Cursor & writing state */

unsigned int writing_state = 160;
unsigned int cursor_state = 80;

/* define I/O Ports */
#define FB_COMMAND_PORT   0x3D4
#define FB_DATA_PORT      0x3D5

/* define I/O port commands (magic numbers that you send the lower/upper bits */
#define FB_HIGH_BYTE_COMMAND    14
#define FB_LOW_BYTE_COMMAND     15




void fb_clear(void);
void fb_clear_line(int pos);
void fb_write_cell(unsigned i, char c, unsigned char fg, unsigned char bg);
void fb_move_cursor(unsigned short pos);
int fb_write(char *buf, unsigned int len);


/** fb_move_cursor:
 * Moves the cursor the a position i
 *
 * @ param pos: the new position of the cursor
 */


void fb_move_cursor(unsigned short pos)
{
  outb(FB_COMMAND_PORT, FB_HIGH_BYTE_COMMAND);
  outb(FB_DATA_PORT, ((pos >> 8) & 0x00FF));
  outb(FB_COMMAND_PORT, FB_LOW_BYTE_COMMAND);
  outb(FB_DATA_PORT, (pos & 0x00FF));
}


/* clears the framebuffer */

void fb_clear(void)
{
  for (int i = 0; i < FRAMEBUFFER_LENGTH; i++)
  {
    fb_write_cell(i*2, ' ', 0, 0);
  }
}


/* clears the current line (next 80 characters for now)*/

void fb_clear_line(int pos)
{
  for (int i = 0; i < 80; i++)
  {
    fb_write_cell(pos + i*2, ' ', 0, 0);
  }
}


/** fb_write_cell:
 * Writes a character with the given foreground a background to position i in the framebuffer
 *
 * @ param i    The location in the framebuffer
    * would be: i = row * 80 + column
 * @ param c    The character
 * @ param fg   The foreground color
 * @ param bg   The background color
 */

void fb_write_cell(unsigned int i, char c, unsigned char fg, unsigned char bg)
{
  fb[i] = c;
  fb[i + 1] = ((fg & 0x0F) << 4 | (bg & 0x0F));
}



/** fb_write:
 * Writes the buffer "buf" of length "len" to the screen
 *
 * @ param *buf: buffer to be written
 * @ param len: length of the buffer
 *
 * TO IMPLEMENT: fb_write automatically scrolls
 */

int fb_write(char *buf, unsigned int len)
{
  for (unsigned int i = 0; i < len; i++)
    {
      fb_write_cell((writing_state+i*2), buf[i], 0, 15);
    }
  writing_state+=len*2;
  cursor_state+=len;
  fb_move_cursor(cursor_state);

  return 0;
}
