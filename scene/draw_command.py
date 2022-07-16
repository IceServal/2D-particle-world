import util.shapes
import resource.particles

class Draw_Command:
    def __init__(self, particle: resource.particles.Particle):
        self._particle = particle

        self.bounding_box = None
        self.fill_color = None

    def draw(self) -> None:
        left_up = util.shapes.Point(
            self._particle.center.x - self._particle.radius,
            self._particle.center.y - self._particle.radius
        )
        right_bottom = util.shapes.Point(
            self._particle.center.x + self._particle.radius,
            self._particle.center.y + self._particle.radius
        )
        self.bounding_box = util.shapes.Rectangle(left_up, right_bottom)
        self.fill_color = self._particle.color

