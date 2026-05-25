import unittest

from test.bases import WorldTestBase
from worlds.tony_hawks_pro_skater_1_2.enums import traplink_itemname_mapping, TonyHawksProSkater12APTrapTypes


class TonyHawksProSkater12TestBase(WorldTestBase):
    game = "Tony Hawk's Pro Skater 1 + 2"

    @unittest.skip("Local testing only")
    def test_traplink_mapping(self) -> None:
        """
        Test if all trap names accepted by traplink map to Tony Hawks Pro Skater 1+2 traps.
        """
        for v in traplink_itemname_mapping.values():
            self.assertIn(v, TonyHawksProSkater12APTrapTypes)
