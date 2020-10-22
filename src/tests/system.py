from pygravity.twod import GravityContainer, Vector2
from pygravity.twod.util import Body, BodyWithMetadata

from system_generator import generate_system, BodyTuple
from planet_name_gen import generate_planet_name


container = GravityContainer()

system = generate_system()
# print(system)


if system is not None:
    from pygravity.twod.pygame_simulation import Body as SimBody, start_simulation, bodies, Settings

    suns = []
    sun_sims = []
    for sun_tuple in system.suns:
        sun = BodyWithMetadata(Body(container, Vector2(sun_tuple.x, sun_tuple.y), sun_tuple.mass),
                            generate_planet_name(), sun_tuple.radius, sun_tuple.color)
        print(sun)
        suns.append(sun)
        sun_sim = SimBody.from_metadata(sun)
        sun_sim.physics.add_velocity(sun_tuple.x_speed, sun_tuple.y_speed)
        sun_sims.append(sun_sim)
        bodies.append(sun_sim)


    # Settings.focus = sun_sims[0]
    Settings.time_scale *= 10
    start_simulation()
