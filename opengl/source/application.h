#pragma once

#include "config.h"
#include "window.h"
#include "state/state.h"

class Application {
  public:
    Application(const Config &config);
    void runLoop();

  private:
    Window mWindow;

    // todo: convert to vector
    State mState;
};