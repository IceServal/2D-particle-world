import util.shapes
import resource.particles
import resource.boundaries


class Draw_Command:
    def __init__(self, color: str):
        self.color = color

        self.bounding_box = None

    def draw(self):
        pass

class Particle_Draw_Command(Draw_Command):
    def __init__(self, particle: resource.particles.Particle):
        super().__init__(particle.color)

        self._particle = particle

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
        self.color = self._particle.color

class Boundary_Draw_Command(Draw_Command):
    def __init__(self, boundary: resource.boundaries.Boundary):
        super().__init__(boundary.color)

        self._boundary = boundary

    def draw(self) -> None:
        self.bounding_box = util.shapes.Rectangle(self._boundary.point1, self._boundary.point2)
        self.color = self._boundary.color

