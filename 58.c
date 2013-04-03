#include <stdio.h>
#include <stdlib.h>

int isPrime(int x) {
  if (x < 2)
    return 0;
  for (int i = 2; i * i <= x; i++) {
    if (x % i == 0) {
      return 0;
    }
  }
  return 1;
}

int main(void) {
  int step = 2;
  int x = 1;
  int cnt = 0;
  int i = 0;

  while (1) {
    i += 1;
    for (int i = 0; i < 4; i++) {
      x += step;
      cnt += isPrime(x);
    }
    step += 2;
    if (cnt * 10 < 4 * i + 1) {
      printf("%d %d %d\n", cnt, 4 * i + 1, i * 2 + 1);
      return 0;
    }
  }
  return 1;
}
