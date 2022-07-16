import tkinter

import scene.constants
import scene.draw_command


class Instance:
    def __init__(self, draw_command: scene.draw_command.Draw_Command):
        self.draw_command = draw_command
        self.id = None

class Pass:
    def __init__(self):
        self.instance_queue = []

    def enqueue_draw_command(self, draw_command: scene.draw_command.Draw_Command) -> None:
        self.instance_queue.append(Instance(draw_command))

    def update(self) -> None:
        for instance in self.instance_queue:
            instance.draw_command.draw()

    def render(self, canvas: tkinter.Canvas) -> None:
        for instance in self.instance_queue:
            if instance.id is None:
                instance.id = canvas.create_oval(
                    0.0, 0.0, 1.0, 1.0,
                    fill = instance.draw_command.fill_color,
                    width = 0.0
                )

            canvas.coords(
                instance.id,
                [
                    instance.draw_command.bounding_box.x1 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.y1 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.x2 * scene.constants.SCALE,
                    instance.draw_command.bounding_box.y2 * scene.constants.SCALE,
                ]
            )

