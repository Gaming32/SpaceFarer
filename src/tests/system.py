from pygravity.twod import GravityContainer
from pygravity.twod.util import Body, BodyWithMetadata

from system_generator import generate_system


container = GravityContainer()

system = generate_system()
print(system)
