#include "framebuffer.c"
#include "io.h"


int main (void)
{
  //fb_clear();

  fb_spam_a();
  //char *string = "Welcome to the OS";

  fb_scroll();
  fb_write_cell(0, 'A', 15, 0);

  fb_scroll();
  //fb_move_cursor(24*80);
  //fb_write(string, 17);

  //fb_scroll();
  return 0;
}
