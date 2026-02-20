from test.bases import WorldTestBase

from .. import NodebusterWorld

class NodebusterTestBase(WorldTestBase):
    game = "Nodebuster"
    world: NodebusterWorld
