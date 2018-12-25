#include "world.h"

#include "config.h"

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <iostream>

World::World(const Config &config)
: basic("../source/shader/basic.vert", "../source/shader/basic.frag"),
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
  basic.use();
}

void World::render(const glm::mat4 proj, const glm::mat4 view, glm::vec2 cursorPos) {
  basic.setVec2("mouse", cursorPos);
  basic.setFloat("time", glfwGetTime());

  glBindVertexArray(VAO);
  glDrawArrays(GL_TRIANGLES, 0, 6);
}