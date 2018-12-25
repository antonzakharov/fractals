#pragma once

#include "../config.h"
#include "../world.h"
#include "../player.h"

#include <GLFW/glfw3.h>

// todo: make multiple states

class State {
  public:
    State(const Config &config, GLFWwindow *window);
    void handleInput();
    void update();
    void render();

  private:
    GLFWwindow *window;
    World mWorld;
    Player mPlayer;
};