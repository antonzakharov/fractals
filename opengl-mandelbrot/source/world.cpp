#include "world.h"

#include "config.h"

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

World::World(const Config &config)
: shader("../source/shader/basic.vert", "../source/shader/mandel.frag"),
  mConfig(config) {
  float tempVertices[] = {
    -1.0f, -1.0f, 0.0f,
    -1.0f,  1.0f, 0.0f,
     1.0f,  1.0f, 0.0f,
     1.0f,  1.0f, 0.0f,
     1.0f, -1.0f, 0.0f,
    -1.0f, -1.0f, 0.0f
  };
  vertices = tempVertices;

  glGenVertexArrays(1, &VAO);
  glBindVertexArray(VAO);

  glGenBuffers(1, &VBO);
  glBindBuffer(GL_ARRAY_BUFFER, VBO);

  glBufferData(GL_ARRAY_BUFFER, sizeof(tempVertices), vertices, GL_STATIC_DRAW);

  glEnableVertexAttribArray(0);
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void *) 0);
  shader.use();
}

void World::render(const glm::mat4 proj, const glm::mat4 view, glm::vec2 cursorPos, float zoom) {
  shader.setVec2("mouse", cursorPos);
  shader.setFloat("time", glfwGetTime());
  shader.setFloat("zoom", zoom);
  shader.setInt("MAX_ITER", 100);

  glBindVertexArray(VAO);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}