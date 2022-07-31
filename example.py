import util.ops
import util.shapes
import util.constants
import scene.iscene
import resource.world
import resource.particles
import resource.boundaries


# Global Variables
WORLD_WIDTH  = 8
WORLD_HEIGHT = 8
PARTICLE_NUMBER = 5


if __name__ == '__main__':
    world = resource.world.World("white")

    for i in range(PARTICLE_NUMBER):
        center = util.shapes.Point(1.0 + ((6.0 / (PARTICLE_NUMBER - 1)) * i), 6.0)
        radius = 0.2
        mass = util.constants.PI * util.ops.pow2(radius) * 2.0
        velocity = util.shapes.Vector(-2.0 + ((4.0 / (PARTICLE_NUMBER - 1)) * i), i * 2.0)
        color = 'blue'
        particle = resource.particles.Particle(center, radius, mass, velocity, color)

        world.add_particle(particle)

    line_left_point1 = util.shapes.Point(1.0, 0.0)
    line_left_point2 = util.shapes.Point(0.0, 8.0)
    world.add_boundary(
        resource.boundaries.One_Way_Slab(
            line_left_point1,
            line_left_point2,
            util.shapes.Point(4.0, 4.0),
            "black"
        )
    )

    line_right_point1 = util.shapes.Point(7.0, 0.0)
    line_right_point2 = util.shapes.Point(7.0, 8.0)
    world.add_boundary(
        resource.boundaries.One_Way_Slab(
            line_right_point1,
            line_right_point2,
            util.shapes.Point(4.0, 4.0),
            "black"
        )
    )

    line_top_point1 = util.shapes.Point(0.0, 1.0)
    lint_top_point2 = util.shapes.Point(8.0, 0.0)
    world.add_boundary(
        resource.boundaries.One_Way_Slab(
            line_top_point1,
            lint_top_point2,
            util.shapes.Point(4.0, 4.0),
            "black"
        )
    )

    line_bottom_point1 = util.shapes.Point(0.0, 7.0)
    line_bottom_point2 = util.shapes.Point(8.0, 7.0)
    world.add_boundary(
        resource.boundaries.One_Way_Slab(
            line_bottom_point1,
            line_bottom_point2,
            util.shapes.Point(4.0, 4.0),
            "black"
        )
    )

    main_scene = scene.iscene.Scene(WORLD_WIDTH, WORLD_HEIGHT, world)
    main_scene.pack_world()
    main_scene.mainloop()

