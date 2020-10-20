from pygravity.twod import GravityContainer, Vector2
from pygravity.twod.util import Body, BodyWithMetadata

from system_generator import generate_system, BodyTuple
from planet_name_gen import generate_planet_name


container = GravityContainer()

system = generate_system()
# print(system)


if system is not None and system.suns:
    sun_tuple: BodyTuple = system.suns[0]
    sun = BodyWithMetadata(Body(container, Vector2(sun_tuple.x, sun_tuple.y), sun_tuple.mass),
                           generate_planet_name(), sun_tuple.radius, sun_tuple.color)
    print(sun)

    from pygravity.twod.pygame_simulation import Body as SimBody, start_simulation, bodies, Settings
    sun_sim = SimBody.from_metadata(sun)
    bodies.append(sun_sim)
    Settings.focus = sun_sim
    start_simulation()
