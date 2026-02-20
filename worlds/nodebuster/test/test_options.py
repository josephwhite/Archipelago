from .bases import NodebusterTestBase
from .. import Options
from ..items import milestone_items
from ..locations import get_milestone_locations

class NoMilestonesWorldTestBase(NodebusterTestBase):
    options = {
        "milestone": Options.Milestones.option_false
    }

    def test_vanilla_milestone_locations(self):
        milestone_locations = get_milestone_locations()
        milestone_item_names: list[str] = []
        for i in milestone_items:
            milestone_item = i["name"]
            milestone_item_names.append(milestone_item)
        print(milestone_item_names)
        for loc in milestone_locations:
            with self.subTest("Only milestones in milestone locations", location=loc):
                item_in_loc = self.world.get_location(loc).item
                assert item_in_loc.name in milestone_item_names
