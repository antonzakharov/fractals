#include <iostream>

#include "config.h"
#include "application.h"

int main()
{
  Config config;
  Application app(config);

  app.runLoop();

  return 0;
}