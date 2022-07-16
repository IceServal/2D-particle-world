import util.ops
import util.shapes
import util.constants
import scene.iscene
import resource.world
import resource.particles


# Global Variables
WORLD_WIDTH  = 8
WORLD_HEIGHT = 8
PARTICLE_NUMBER = 5


if __name__ == '__main__':
    world = resource.world.World()
    for i in range(PARTICLE_NUMBER):
        center = util.shapes.Point(1.0 + ((6.0 / (PARTICLE_NUMBER - 1)) * i), 6.0)
        radius = 0.2
        mass = util.constants.PI * util.ops.pow2(radius) * 2.0
        color = "blue"
        velocity = util.shapes.Vector(-2.0 + ((4.0 / (PARTICLE_NUMBER - 1)) * i), i * 2.0)
        particle = resource.particles.Particle(center, radius, mass, color, velocity)
        world.add_particle(particle)

    main_scene = scene.iscene.Scene(WORLD_WIDTH, WORLD_HEIGHT, world)
    main_scene.pack_world()
    main_scene.mainloop()

