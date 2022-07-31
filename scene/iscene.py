import scene.ipass
import scene.constants
import scene.draw_commands
import resource.world

import time
import tkinter

class Scene:
    def __init__(self, width: int, height: int, world: resource.world.World):
        self.width  = width * scene.constants.SCALE
        self.height = height * scene.constants.SCALE

        self.world = world

        self.board = tkinter.Tk()
        self.board.title('2D particle world')

        self.canvas = tkinter.Canvas(
            self.board,
            width=self.width,
            height=self.height,
            bg=world.color
        )
        self.canvas.pack()

        self.ipass = scene.ipass.Pass(self.canvas)

    def pack_world(self) -> None:
        for particle in self.world.inspect_particles():
            self.ipass.enqueue_draw_command(scene.draw_commands.Particle_Draw_Command(particle))

        for boundary in self.world.boundaries:
            self.ipass.enqueue_draw_command(scene.draw_commands.Boundary_Draw_Command(boundary))

    def mainloop(self) -> None:
        base_time = time.time() - scene.constants.DELTA_TIME
        while True:
            self.ipass.update()
            self.ipass.render()

            self.canvas.update_idletasks()
            self.canvas.update()

            current_time = time.time()
            delta_time = current_time - base_time
            if delta_time > scene.constants.DELTA_TIME:
                base_time = current_time
                self.world.resolve(scene.constants.DELTA_TIME)

