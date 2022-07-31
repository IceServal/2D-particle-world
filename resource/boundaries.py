import resource.particles
import util.shapes


class Boundary:
    def __init__(self, color: str):
        self.color = color

    def influence(self, other: resource.particles.Particle) -> None:
        pass

class One_Way_Slab(util.shapes.Line, Boundary):
    def __init__(
        self
        , line_point1: util.shapes.Point
        , line_point2: util.shapes.Point
        , region_point: util.shapes.Point
        , color: str
    ):
        util.shapes.Line.__init__(self, line_point1, line_point2)
        Boundary.__init__(self, color)

        self.region_point = region_point

    def influence(self, particle: resource.particles.Particle) -> None:
        if  False \
            or (self.particle.center.x + self.particle.radius > 8.0 and self.particle.velocity.x > 0.0) \
            or (self.particle.center.x - self.particle.radius < 0.0 and self.particle.velocity.x < 0.0) \
        :
            self.particle.velocity.x = -self.particle.velocity.x
        if False \
            or (self.particle.center.y + self.particle.radius > 8.0 and self.particle.velocity.y > 0.0) \
            or (self.particle.center.y - self.particle.radius < 0.0 and self.particle.velocity.y < 0.0) \
        :
            self.particle.velocity.y = -self.particle.velocity.y
        pass

class Zero_Way_Slab(util.shapes.Line, Boundary):
    def __init__(
        self
        , line_point1: util.shapes.Point
        , line_point2: util.shapes.Point
        , color: str
    ):
        util.shapes.Line.__init__(self, line_point1, line_point2)
        Boundary.__init__(self, color)

    def influence(self, particle: resource.particles.Particle) -> None:
        pass

