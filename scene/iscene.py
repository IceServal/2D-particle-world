import time
import tkinter

import scene.ipass
import scene.constants
import scene.draw_command
import resource.world

class Scene:
    def __init__(self, width: int, height: int, world: resource.world.World):
        self._width  = width * scene.constants.SCALE
        self._height = height * scene.constants.SCALE

        self._board = tkinter.Tk()
        self._board.title('2D particle world')

        self._canvas = tkinter.Canvas(self._board, width=self._width, height=self._height, bg='ivory')
        self._canvas.pack()
        
        self.ipass = scene.ipass.Pass()

        self.world = world

    def pack_world(self) -> None:
        for particle in self.world.inspect():
            self.ipass.enqueue_draw_command(scene.draw_command.Draw_Command(particle))

    def mainloop(self) -> None:
        base_time = time.time() - scene.constants.DELTA_TIME
        while True:
            self.ipass.update()
            self.ipass.render(self._canvas)

            self._canvas.update_idletasks()
            self._canvas.update()

            current_time = time.time()
            delta_time = current_time - base_time
            if delta_time > scene.constants.DELTA_TIME:
                base_time = current_time
                self.world.resolve(scene.constants.DELTA_TIME)

