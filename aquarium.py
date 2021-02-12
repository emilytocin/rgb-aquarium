#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics_test
import time

class Position(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Entity(object):
  def __init__(self, pos, aquarium):
    self.pos = pos
    self.aquarium = aquarium

class Aquarium(SampleBase):
  def __init__(self, *args, **kwargs):
    super(Aquarium, self).__init__(*args, **kwargs)
    self.entities = []
    self.spawn_seed()

  def spawn_seed(self):
    # Need to add logic here in subclasses to spawn initial entities.
    pass

  def addEntity(self, entity):
    self.entities.append(entity)

  def show(self):
    # Clear the matrix.

    self.matrix.Fill(0, 0, 0)
    for entity in self.entities:
      entity.show()

  def run(self):
    # Simulate the Aquarium. For each entity in the aquarium, make a step.
    # After all steps, draw the screen.

    for entity in self.entities:
      entity.step()
    self.show()


# Main function
if __name__ == "__main__":
  Acquarium = Acquarium()
  if (not Acquarium.process()):
    graphics_test.print_help()