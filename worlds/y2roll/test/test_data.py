from worlds.y2roll.locations import get_y2roll_gem_locations
from worlds.y2roll.test.bases import Y2ROLLTestBase

from .. import options


class TestY2ROLLData(Y2ROLLTestBase):
    options = {
        "include_gems": options.IncludeGems.option_true
    }
    def test_gem_locations(self) -> None:
        possible_locations = [location.name for location in self.world.get_locations()]
        gems = get_y2roll_gem_locations()
        for loc in gems:
            with self.subTest("Location created", location=loc):
                self.assertIn(loc, possible_locations)
