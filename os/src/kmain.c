#include "framebuffer.c"
#include "io.h"


int main (void)
{
  fb_clear();

  //fb_spam_a();
  char *string = "Welcome to the OS";
  char *A = "AA";
  char *B = "BB";
  char *C = "CC";
  char *D = "DD";
  char *E = "EE";
  char *F = "FF";
  char *G = "GG";
  char *H = "HH";
  char *I = "II";
  char *J = "JJ";
  char *K = "KK";
  char *L = "LL";
  char *M = "MM";
  char *N = "NN";
  char *O = "OO";

  fb_move_cursor(80);
  fb_write(string, 17);
  fb_move_cursor(160);
  fb_write(string, 17);


  fb_move_cursor(320);
  fb_write(A, 2);
  fb_move_cursor(400);
  fb_write(B, 2);
  fb_move_cursor(480);
  fb_write(C, 2);
  fb_move_cursor(560);
  fb_write(D, 2);
  fb_move_cursor(640);
  fb_write(E, 2);
  fb_move_cursor(720);
  fb_write(F, 2);
  fb_move_cursor(800);
  fb_write(G, 2);
  fb_move_cursor(880);
  fb_write(H, 2);
  fb_move_cursor(960);
  fb_write(I, 2);
  fb_move_cursor(1040);
  fb_write(J, 2);
  fb_move_cursor(1120);
  fb_write(K, 2);
  fb_move_cursor(1200);
  fb_write(L, 2);
  fb_move_cursor(1280);
  fb_write(M, 2);
  fb_move_cursor(1360);
  fb_write(N, 2);
  fb_move_cursor(1440);
  fb_write(O, 2);
  fb_move_cursor(1520);
  fb_write(A, 2);
  fb_move_cursor(1600);
  fb_write(B, 2);
  fb_move_cursor(1680);
  fb_write(C, 2);
  fb_move_cursor(1760);
  fb_write(D, 2);
  fb_move_cursor(1840);
  fb_write(E, 2);
  fb_move_cursor(1920);
  fb_write(F, 2);




  fb_scroll();
  fb_scroll();
  return 0;
}
