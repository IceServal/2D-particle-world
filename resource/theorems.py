import resource.particles
import util.shapes


def momentum_theorem(
    particle1: resource.particles.Particle,
    particle2: resource.particles.Particle
) -> None:
    p1 = particle1
    p2 = particle2

    delta_position = util.shapes.Vector(
        p2.center.x - p1.center.x,
        p2.center.y - p1.center.y
    )
    delta_velocity = util.shapes.Vector(
        p2.velocity.x - p1.velocity.x,
        p2.velocity.y - p1.velocity.y
    )
    if True \
        and ((delta_position.x * delta_velocity.x) >= 0) \
        and ((delta_position.y * delta_velocity.y) >= 0) \
    :
        return

    distance = delta_position.modulus()
    if distance > (p1.radius + p2.radius):
        return
    if distance == 0.0:
        return
    # need fix bug condition

    sin_theta = delta_position.y / distance
    cos_theta = delta_position.x / distance

    p1_normal_velocity  =   p1.velocity.x * cos_theta \
                          + p1.velocity.y * sin_theta
    p1_tangent_velocity =   p1.velocity.x * sin_theta \
                          + p1.velocity.y * cos_theta
    p2_normal_velocity  =   p2.velocity.x * cos_theta \
                          + p2.velocity.y * sin_theta
    p2_tangent_velocity =   p2.velocity.x * sin_theta \
                          + p2.velocity.y * cos_theta

    p1_momentum = p1.mass * p1_normal_velocity
    p2_momentum = p2.mass * p2_normal_velocity
    denom = p1.mass + p2.mass
    p1_nom = (p1.mass - p2.mass) * p1_normal_velocity + 2 * p2_momentum
    p2_nom = (p2.mass - p1.mass) * p2_normal_velocity + 2 * p1_momentum
    p1_normal_velocity = p1_nom / denom
    p2_normal_velocity = p2_nom / denom

    p1.velocity.x =   p1_normal_velocity  * cos_theta \
                    + p1_tangent_velocity * sin_theta
    p1.velocity.y =   p1_normal_velocity  * sin_theta \
                    + p1_tangent_velocity * cos_theta
    p2.velocity.x =   p2_normal_velocity  * cos_theta \
                    + p2_tangent_velocity * sin_theta
    p2.velocity.y =   p2_normal_velocity  * sin_theta \
                    + p2_tangent_velocity * cos_theta

