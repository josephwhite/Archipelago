import unittest

from worlds.y2roll.locations import get_y2roll_gem_locations
from worlds.y2roll.test.bases import Y2ROLLTestBase


class TestY2ROLLData(Y2ROLLTestBase):
    def test_gem_locations(self) -> None:
        possible_locations = self.world.location_names
        locs = get_y2roll_gem_locations()
        for loc in locs:
            with self.subTest("Location created", location=loc):
                self.assertIn(loc, possible_locations)
