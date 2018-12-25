#include "player.h"

#include "config.h"

#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

#include <iostream>

namespace {

}

Player::Player(const Config &config) 
: mConfig(config) {
  // todo: set init values in better way (or something)
  position = glm::vec3(0.0, 0.0, 0.0);
  target = glm::vec3(0.0, 0.0, -1.0);

  center = glm::vec2(0.0, 0.0);
}

glm::mat4 Player::getViewMatrix() {
  return glm::lookAt(position, position + target, glm::vec3(0.0, 1.0, 0.0));
}

glm::mat4 Player::getProjectionMatrix() {
  return glm::perspective(glm::radians(mConfig.FOV), (float)mConfig.WIDTH / (float)mConfig.HEIGHT, 0.1f, 100.0f);
}

glm::vec2 Player::getPos() {
  return center + tempOffset;
}

void Player::handleMouse(GLFWwindow *window) {
  double tempX, tempY;
  glfwGetCursorPos(window, &tempX, &tempY);

  glm::vec2 cursorLoc(-tempX / mConfig.WIDTH , tempY / mConfig.HEIGHT);

  if (!pressing) {
    clickLoc = cursorLoc;
    pressing = true;
  }

  tempOffset = cursorLoc - clickLoc;
}

void Player::stopPressing() {
  pressing = false;
  center += tempOffset;
  tempOffset = glm::vec2(0.0, 0.0);
}

void Player::handleKeyboard(Direction direction) {

}