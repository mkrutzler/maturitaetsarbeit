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

unsigned int cursor_state = 0;

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
void fb_scroll(void);


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
  cursor_state = pos;
}


/* clears the framebuffer */

void fb_clear(void)
{
  for (int i = 0; i < 24*80+1; i++)
  {
    fb_write_cell(i, ' ', 0, 0);
  }
}

/* fills buffer with "a", used for testing */
void fb_spam_a(void)
{
  for (int i = 0; i < 24*80; i++)
  {
    fb_write_cell(i, 'a', 15, 0);
  }
}

/* clears the current line (next 80 characters for now)*/

void fb_clear_line(int pos)
{
  for (int i = 0; i < 80; i++)
  {
    fb_write_cell(pos + i, ' ', 0, 0);
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
  i = i*2;
  fb[i] = c;
  fb[i + 1] = ((bg & 0x0F) << 4 | (fg & 0x0F));
}



/** fb_scroll:
 * Scrolls a line upwards
 *
 * no parameters needed
 */

void fb_scroll(void)
{
  for (unsigned int i = 0; i <= (25*80); i++)
  {
    //fb_write_cell((i+80), fb[i*2], 15, 0);
    fb[i] = fb[i+160];
    /* i: 160, because the fb has two parts: char & color => to move 80 cells you need to shift 160 chars */
  }
  fb_clear_line(24*80);
}




/** fb_write:
 * Writes the buffer "buf" of length "len" to the screen
 *
 * @ param *buf: buffer to be written
 * @ param len: length of the buffer
 */

int fb_write(char *buf, unsigned int len)
{
  for (unsigned int i = 0; i < len; i++)
    {
      fb_write_cell((cursor_state+i), buf[i], 15, 0);
    }
  cursor_state+=len;
  fb_move_cursor(cursor_state);

  return 0;
}