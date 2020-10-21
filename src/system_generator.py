import collections
import math
import random
from typing import Optional
import colorsys

import numpy as np


SystemTuple = collections.namedtuple('SystemTuple', ['suns', 'planets', 'moons', 'astroids', 'comets'])
BodyTuple = collections.namedtuple('BodyTuple', ['x', 'y', 'x_speed', 'y_speed', 'mass', 'radius', 'color'])


FULL_CIRCLE = 2 * math.pi
MAXIMUM_TRANSLATION = 10430107865214.05


def generate_system() -> Optional[SystemTuple]:
    origin = (random.uniform(0, FULL_CIRCLE), random.uniform(0, MAXIMUM_TRANSLATION))
    origin = np.array([math.cos(origin[0]), math.sin(origin[0])], np.float64) * origin[1]

    suns = []
    rand = random.random()
    if rand > 0.70:
        return None
    elif rand < 0.90:
        suns.extend(create_binary_suns(origin))
    else:
        suns.append(create_sun(origin))
        # suns.append(BodyTuple(origin[0], origin[1], 0, 0, random.uniform(1.989e30, 2.188e31), random.uniform()))

    return SystemTuple(
        suns,
        None,
        None,
        None,
        None,
    )


def random_sun_mass():
    return random.uniform(1.989e30, 2.188e31)


def random_sun_color():
    blue_color = colorsys.rgb_to_hsv(*(np.array((32, 32, 117)) / 255))
    red_color = colorsys.rgb_to_hsv(*(np.array((153, 63, 50)) / 255))
    range = random.uniform(-1, 1)
    if range > 0:
        base_color = list(blue_color)
    else:
        base_color = list(red_color)
    base_color[1] *= range
    return tuple(np.array(colorsys.hsv_to_rgb(*base_color)) * 255)


def create_sun(position=(0, 0), **extra) -> BodyTuple:
    result = BodyTuple(position[0], position[1],
                       0, 0,
                       random_sun_mass(),
                       random.uniform(6.9634e8, 6.171e11),
                       random_sun_color()
    )
    return result._replace(**extra)


def create_binary_suns(origin):
    """This function was created based on https://imagine.gsfc.nasa.gov/features/yba/CygX1_mass/binary/equation_derive.html"""
    separation = random.uniform(3481700000, 8356080000)
    mass1 = random_sun_mass()
    mass2 = random_sun_mass()
    separation2 = (mass1 / (mass1 + mass2)) * separation
    separation1 = separation - separation2
    velocity1 = random.uniform(300, 3000)
    velocity2 = (mass1 / mass2) * velocity1

    orbit_direction = random.choice([-1, 1])
    velocity1 *= orbit_direction
    velocity2 *= orbit_direction

    return [
        create_sun((origin[0] - separation1, origin[1]), y_speed=velocity1, mass=mass1),
        create_sun((origin[1] + separation2, origin[1]), y_speed=-velocity2, mass=mass2)
    ]


if __name__ == '__main__':
    print(generate_system())
