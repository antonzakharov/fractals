#pragma once

#include "player.h"
#include "config.h"
#include "shader/shader.h"

#include <glad/glad.h>
#include <glm/glm.hpp>

class World {
  public:
    World(const Config &config);
    void render(const glm::mat4 proj, const glm::mat4 view, glm::vec2 cursorPos);

  private:
    GLuint VAO, VBO;
    Shader basic;
    Config mConfig;

    // temporary
    float *vertices;
    float *indices;
};