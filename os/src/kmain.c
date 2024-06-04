#include "framebuffer.c"
#include "io.h"


int main (void)
{
  fb_clear();

  //fb_spam_a();
  char *string = "Welcome to the OS";
  char *C = "CC";

  //fb_scroll();
  //fb_write_cell(0, 'A', 15, 0);
  //fb_write_cell(80, 'B', 15, 0);
  //fb_write_cell(24*80, 'B', 15, 0);

  for (int i = 0; i < 21; i++)
  {
    fb_move_cursor((24-i)*80);
    fb_write(C, 2);
  }
  //fb_scroll();
  fb_move_cursor(80);
  fb_write(string, 17);
  fb_move_cursor(160);
  fb_write(string, 17);

  fb_scroll();
  fb_scroll();
  return 0;
}
