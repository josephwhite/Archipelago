from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from .data.basegame import Y2ROLL_LEVEL_BY_KEY, get_y2roll_world_name

from .items import Y2ROLLItem, all_items_to_id, junk_item_data_table, all_items, world_access_item_data_table
from .locations import all_locations_to_id, get_y2roll_gem_locations, Y2ROLLLocation
from .regions import create_and_connect_regions
from .rules import set_all_y2roll_rules
from .web_world import Y2ROLLWebWorld
from . import options as y2roll_options


class Y2ROLLWorld(World):
    """
    Y2ROLL is an N64-style minimalistic physics-based arcade-style marble rolling game
    that will take you back to the turn of the millennium.
    """
    game = "Y2ROLL"
    web = Y2ROLLWebWorld()

    options_dataclass = y2roll_options.Y2ROLLOptions
    options: y2roll_options.Y2ROLLOptions

    location_name_to_id = all_locations_to_id
    item_name_to_id = all_items_to_id

    # There is always one region that the generator starts from & assumes you can always go back to.
    # This defaults to "Menu", but you can change it by overriding origin_region_name.
    origin_region_name = "Menu"

    # Our world class must have certain functions ("steps") that get called during generation.
    # The main ones are: create_regions, set_rules, create_items.
    # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        create_and_connect_regions(self)
        # Create locations
        for k, v in Y2ROLL_LEVEL_BY_KEY.items():
            world_number = v['world']
            level_number = v['level_in_world']
            world_reg = self.get_region(get_y2roll_world_name(world_number))
            gem_locs = get_y2roll_gem_locations(world_number, level_number)
            for loc in gem_locs:
                foo = Y2ROLLLocation(self.player, loc, all_locations_to_id[loc], world_reg)
                world_reg.locations.append(foo)

    def set_rules(self) -> None:
        set_all_y2roll_rules(self)
        if self.options.make_puml:
            from Utils import visualize_regions
            multiworld = self.multiworld
            visualize_regions(multiworld.get_region("Menu", self.player), "y2roll_world.puml")

    def post_fill(self) -> None:
        pass

    def create_items(self) -> None:
        itempool = []
        # Progression
        if self.options.level_unlocks == self.options.level_unlocks.option_world:
            for k in world_access_item_data_table.keys():
                itempool.append(self.create_item(k))
        # Junk / Traps
        number_of_items = len(itempool)
        number_of_unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
        needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
        itempool += [self.create_filler() for _ in range(needed_number_of_filler_items)]

        self.multiworld.itempool += itempool

        # Start with the first world unlocked
        if self.options.level_unlocks == self.options.level_unlocks.option_world:
            self.push_precollected(self.create_item("Purple Mountains Access"))

    def create_item(self, name: str) -> Y2ROLLItem:
        data = all_items[name]
        id = all_items_to_id[name]
        item = Y2ROLLItem(name, data.classification, id, self.player)
        return item

    def get_filler_item_name(self) -> str:
        item = self.random.choice(list(junk_item_data_table))
        return item

    def fill_slot_data(self) -> Mapping[str, Any]:
        # Options
        data = self.options.as_dict(
            "level_unlocks",
            "death_link"
        )
        data["world_version"] = self.world_version
        return data
