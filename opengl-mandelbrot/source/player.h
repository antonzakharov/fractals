#pragma once

#include "config.h"

#include <GLFW/glfw3.h>
#include <glm/glm.hpp>

enum Direction {
  FORWARD,
  BACKWARD,
  LEFT,
  RIGHT
};

class Player {
  public:
    Player(const Config &config);
    glm::mat4 getViewMatrix();
    glm::mat4 getProjectionMatrix();
    glm::vec2 getPos();
    float getZoom();

    void handleMouse(GLFWwindow *window);
    void stopPressing();
    void handleKeyboard(Direction direction);

  private:
    float zoom = 0.0f;
    bool pressing;

    glm::vec2 center;
    glm::vec2 tempOffset;
    glm::vec2 clickLoc;

    glm::vec3 position;
    glm::vec3 target;

    Config mConfig;
};