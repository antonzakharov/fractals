#pragma once

#include "config.h"

#include <GLFW/glfw3.h>

class Window {
  public:
    Window(const Config &config);
    GLFWwindow *get();

    bool shouldClose();
    void clear();
    void swapBuffer();
    void pollEvents();
  private:
    GLFWwindow *window;
};