import scene.constants
import scene.draw_commands

import tkinter


class Instance:
    def __init__(
        self
        , draw_command: scene.draw_commands.Draw_Command
        , canvas: tkinter.Canvas
    ):
        self.draw_command = draw_command
        self._canvas = canvas

        if isinstance(self.draw_command, scene.draw_commands.Particle_Draw_Command):
            self.id = self._canvas.create_oval(
                0.0, 0.0, 1.0, 1.0,
                fill = self.draw_command.color,
                width = 0.0
            )
        elif isinstance(self.draw_command, scene.draw_commands.Boundary_Draw_Command):
            self.id = self._canvas.create_line(
                0.0, 0.0, 1.0, 1.0,
                fill = self.draw_command.color
            )
        else:
            self.id = None

class Pass:
    def __init__(self, canvas: tkinter.Canvas):
        self._canvas = canvas
        self.instance_queue = []

    def enqueue_draw_command(self, draw_command: scene.draw_commands.Draw_Command) -> None:
        self.instance_queue.append(Instance(draw_command, self._canvas))

    def update(self) -> None:
        for instance in self.instance_queue:
            instance.draw_command.draw()

    def render(self) -> None:
        for instance in self.instance_queue:
            self._canvas.coords(
                instance.id,
                [
                    instance.draw_command.bounding_box.x1 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.y1 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.x2 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.y2 * scene.constants.SCALE,
                ]
            )

