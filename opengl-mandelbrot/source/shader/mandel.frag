#version 330 core

out vec4 FragColor;

in vec2 Position;

uniform vec2 mouse;
uniform float time;
uniform float zoom;
uniform int MAX_ITER;

float mandelbrot(vec2 c) {
  vec2 z = vec2(c);
  for (float i = 0.0; i < MAX_ITER; i++) {
    if (abs(dot(z, z)) > 4.0) {
      return (i / MAX_ITER);
    }
    z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c;
  }
  return 1.0;
}

void main() {
  float result = mandelbrot(Position / zoom + mouse);
  FragColor = vec4(result, result, result, 1.0);
}