#include <stdio.h>

int num_divisors(int n) {
  int r = 0;
  int i;
  for (i = 1; i <= n; i++)
    if (n % i == 0)
      r++;
  return r;
}

int main(void) {
  int n = 500;
  int x;
  int i = 10000;
  while (num_divisors(x) < n) {
    i += 1;
    x = i * (i+1) / 2;
    if (i % 100 == 0)
      printf("%d %d\n", i, x);
  }
  printf("%d\n", x);
  return 0;
}
