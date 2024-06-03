#include "framebuffer.c"
#include "io.h"


int main (void)
{
  fb_clear();

  char *string = "Welcome to the OS";

  fb_write(string, 17);
  return 0;
}
