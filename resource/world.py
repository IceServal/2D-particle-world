import resource.constants
import resource.particles
import util.shapes


class In_World_Particle:
    def __init__(self, particle: resource.particles.Particle):
        self.particle = particle
        self.force_queue = []

    def add_force(self, force: util.shapes.Vector) -> None:
        self.force_queue.append(force)

    def region_constrain(self) -> None:
        # need add wall resource
        # need add bit condition
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

    def force_analyze(self, delta_time: float) -> None:
        resultant_force = util.shapes.Vector(0.0, 0.0)
        for force in self.force_queue:
            resultant_force.shift(force.x, force.y)

        acceleration = util.shapes.Vector(
            resultant_force.x / self.particle.mass,
            resultant_force.y / self.particle.mass
        )
        acceleration.shift(0.0, resource.constants.GRAVITY)

        self.particle.velocity.shift(acceleration.x * delta_time, acceleration.y * delta_time)
        self.force_queue.clear()

    def shift(self, delta_time: float) -> None:
        delta_position   = util.shapes.Vector(0.0, 0.0)
        delta_position.x = self.particle.velocity.x * delta_time
        delta_position.y = self.particle.velocity.y * delta_time

        self.particle.shift(delta_position.x, delta_position.y)

class World:
    def __init__(self):
        self.in_world_particle_queue = []

    def add_particle(self, particle: resource.particles.Particle) -> None:
        self.in_world_particle_queue.append(In_World_Particle(particle))

    def inspect(self) -> resource.particles.Particle:
        for iw_particle in self.in_world_particle_queue:
            yield iw_particle.particle

    def resolve(self, delta_time: float) -> None:
        for iwp1 in self.in_world_particle_queue:
            for iwp2 in self.in_world_particle_queue:
                if iwp1 is iwp2:
                    continue

                iwp1.force_queue.append(iwp2.particle.interact(iwp1.particle))
                iwp2.force_queue.append(iwp1.particle.interact(iwp2.particle))

        for iw_particle in self.in_world_particle_queue:
            iw_particle.shift(delta_time)
            iw_particle.force_analyze(delta_time)
            iw_particle.region_constrain()

