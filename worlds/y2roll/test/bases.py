from test.bases import WorldTestBase
from worlds.y2roll import Y2ROLLWorld


class Y2ROLLTestBase(WorldTestBase):
    game = "Y2ROLL"
    world: Y2ROLLWorld
