import collections
import math
import random
from typing import Optional

import numpy as np


SystemTuple = collections.namedtuple('SystemTuple', ['suns', 'planets', 'moons', 'astroids', 'comets'])
BodyTuple = collections.namedtuple('BodyTuple', ['x', 'y', 'x_speed', 'y_speed', 'mass', 'radius', 'color'])


FULL_CIRCLE = 2 * math.pi
MAXIMUM_TRANSLATION = 10430107865214.05
STAR_COLORS = [
    (0, 33, 75),
    (2, 55, 123),
    (246, 128, 37),
    (250, 152, 41),
    (255, 210, 5),
    (238, 22, 82),
]


def generate_system() -> Optional[SystemTuple]:
    origin = (random.uniform(0, FULL_CIRCLE), random.uniform(0, MAXIMUM_TRANSLATION))
    origin = np.array([math.cos(origin[0]), math.sin(origin[0])], np.float64) * origin[1]

    suns = []
    rand = random.random()
    if rand > 0.70:
        return None
    elif rand < 0.10:
        pass
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


def create_sun(position=(0, 0)) -> BodyTuple:
    return BodyTuple(position[0], position[1],
                     0, 0,
                     random.uniform(1.989e30, 2.188e31),
                     random.uniform(6.9634e8, 6.171e11),
                     random.choice(STAR_COLORS)
    )


if __name__ == '__main__':
    print(generate_system())
