import random
from planet_name_gen import generate_planet_name
from system_generator import generate_system, SystemTuple, BodyTuple


class System:
    __slots__ = SystemTuple._fields

    def __init__(self, tuple: SystemTuple = None):
        if tuple is None:
            tuple = SystemTuple(*([] for _ in range(len(SystemTuple._fields))))
        for (i, attr) in enumerate(SystemTuple._fields):
            setattr(self, attr, tuple[i])


class Body:
    last_id = 0
    ids = []

    def __init__(self, tuple: BodyTuple = None):
        if tuple is None:
            tuple = BodyTuple(*([] for _ in range(len(BodyTuple._fields))))
        for (i, attr) in enumerate(BodyTuple._fields):
            setattr(self, attr, tuple[i])


class Planet(Body):
    pass


def generate_id(klass, highest=999999, char_count=7):
    while True:
        min_id = klass.last_id
        klass.last_id += 1
        char_count = max(char_count, len(str(min_id)))
        id = klass.__name__[0] + '+' \
            + str(random.randint(min_id, min_id + highest)).zfill(char_count)
        if id not in klass.ids:
            return id


if __name__ == '__main__':
    print(generate_id(Planet))
