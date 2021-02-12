#!/usr/bin/env python
from aquarium import Aquarium, Entity, Position
import vectors
import random
from enum import Enum
from rgbmatrix import graphics, GraphicsTest
import time

Behavior = Enum('Behavior', 'wander flee chase')

class Dot(Entity):
  def __init__(self, *args, **kwargs):
    super(Dot, self).__init__(*args, **kwargs)
    
    self.color = graphics.Color(255, 0, 0)
    # Behavior mode should be set to a default.
    self.behavior = Behavior.wander
    self.direction = vectors.RandomDirectionNormal()
    self.tweakcounter = 0
    self.tweakdist = 50

  def step(self):
    def tweak_direction():
      self.tweakcounter -= 1
      if self.tweakcounter <= 0:
        self.direction = vectors.RandomDirectionNormal()
        self.tweakcounter = random.randrange(1,  self.tweakdist)
    
    def step_forward():
      self.pos += self.direction

    if self.behavior == Behavior.wander:
      tweak_direction()
      step_forward()
    
  def show(self):    
    # Draw me as a single dot for now.
    graphics.DrawLine(self.aquarium.matrix, self.pos.x, self.pos.y, self.pos.x, self.pos.y, self.color)

# Main function
if __name__ == "__main__":
  graphics_test = GraphicsTest()
  if (not graphics_test.process()):
    graphics_test.print_help()