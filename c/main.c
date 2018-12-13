#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"
#include <complex.h>
#include <stdio.h>
#include <math.h>

// Resolution across 1 row/column
const int RESOLUTION = 10000;
const int PIXELS = RESOLUTION * RESOLUTION;
// Width across center
const float WIDTH = 4;
const double complex CENTER = 0;
const int  MAX_ITER = 20;

static inline char mandelbrot(double complex *c) {
  double complex z = 0.0;
  for (int j = 0; j < MAX_ITER; j++) {
    if (cabs(z) > 2.0) {
      return (int)(((float)j / MAX_ITER) * 255);
    }

    // Increment
    z = z*z + *c;
  }
  return (char)255;
}

int main() {
  char *data;
  data = (char *)malloc(PIXELS * sizeof(char));
  for (int i = 0; i < PIXELS; i++) {
    // convert position in array to complex
    double complex c = ((float)(i % RESOLUTION) / RESOLUTION)
      * WIDTH - WIDTH / 2 + creal(CENTER)
      + ((floor(i / RESOLUTION) / RESOLUTION)
      * WIDTH - WIDTH / 2 + cimag(CENTER)) * -I;

    data[i] = mandelbrot(&c);
  }
  stbi_write_png("test.png", RESOLUTION, RESOLUTION, 1, data, 
      RESOLUTION * sizeof(char));
  return 0;
}
