"""
.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.
Authors:                                                                    *
    Fenna Houtsma, Christopher Buch Madsen, Guido Vaessen                   *
                                                                            *
Date:                                                                       *
    January 2020                                                            *
*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*~.~*
"""

from drawing2 import DrawCrystal
from hexagonal_grid import CrystalLattice
import pyglet

class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(600, 600)
        self.CL = CrystalLattice(30, gamma=0.01, alpha=0.1, beta=0.5)
        self.drawing = DrawCrystal(self.CL, self.get_size()[0], hexagon_side_length=5)
        pyglet.clock.schedule_interval(self.update, 1.0/24)

    def on_draw(self):
        self.clear()
        self.drawing.draw()

    def update(self, dt):
        self.CL.diffusion()

if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
