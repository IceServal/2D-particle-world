import resource.constants
import util.shapes


class Particle(util.shapes.Circle):
    ''' particle is a kind of circle which has basically 2D physical attributes '''

    def __init__(
        self
        , center: util.shapes.Point
        , radius: float
        , mass: float
        , velocity: util.shapes.Vector
        , color: str
    ):
        super().__init__(center, radius)

        self.mass = mass
        self.velocity = velocity
        self.color = color

    def influence(self, other) -> util.shapes.Vector:
        force = util.shapes.Vector(0.0, 0.0)

        contact_distance = other.radius + self.radius

        delta_position = util.shapes.Vector(
            other.center.x - self.center.x,
            other.center.y - self.center.y
        )
        if delta_position.x == 0.0 and delta_position.y == 0.0:
            delta_position.y = 0.0001 * contact_distance
        distance = delta_position.modulus()

        cos_theta = delta_position.x / distance
        sin_theta = delta_position.y / distance

        if distance < contact_distance:
            k = 1.0 - (distance / contact_distance)
            f_min = resource.constants.PUSH_FORCE_MIN
            f_max = resource.constants.PUSH_FORCE_MAX
            force_modulus = f_min + (k * (f_max - f_min))
            force.x = cos_theta * force_modulus
            force.y = sin_theta * force_modulus

        return force

