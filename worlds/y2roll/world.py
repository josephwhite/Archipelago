import typing
from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import options as y2roll_options
from .data.basegame import Y2ROLL_LEVEL_BY_KEY, get_y2roll_world_name
from .items import (
    Y2ROLLItem,
    all_items,
    all_items_to_id,
    get_y2roll_item_groups,
    junk_item_data_table,
    trap_item_data_table,
    world_access_item_data_table,
)
from .locations import (
    Y2ROLLLocation,
    all_locations_to_id,
    get_y2roll_gem_locations,
    get_y2roll_goal_locations,
    get_y2roll_medal_locations,
)
from .regions import create_and_connect_regions
from .rules import set_all_y2roll_rules
from .web_world import Y2ROLLWebWorld


class Y2ROLLWorld(World):
    """
    Y2ROLL is an N64-style minimalistic physics-based arcade-style marble rolling game
    that will take you back to the turn of the millennium.
    """
    game = "Y2ROLL"
    web = Y2ROLLWebWorld()
    hidden = False
    topology_present = False
    origin_region_name = "Menu"
    hint_blacklist = []

    options_dataclass = y2roll_options.Y2ROLLOptions
    options: y2roll_options.Y2ROLLOptions

    location_name_to_id = all_locations_to_id
    item_name_to_id = all_items_to_id
    item_name_groups = get_y2roll_item_groups()

    # Universal Tracker
    disable_ut = True

    def create_regions(self) -> None:
        create_and_connect_regions(self)
        # Create locations
        for k, v in Y2ROLL_LEVEL_BY_KEY.items():
            world_number = v["world"]
            level_number = v["level_in_world"]
            world_reg = self.get_region(get_y2roll_world_name(world_number))
            # Level Goals
            goal_locs = get_y2roll_goal_locations(world_number, level_number)
            for loc in goal_locs:
                foo = Y2ROLLLocation(self.player, loc, all_locations_to_id[loc], world_reg)
                world_reg.locations.append(foo)
            # Gems
            if self.options.include_gems:
                gem_locs = get_y2roll_gem_locations(world_number, level_number)
                for loc in gem_locs:
                    foo = Y2ROLLLocation(self.player, loc, all_locations_to_id[loc], world_reg)
                    world_reg.locations.append(foo)
            # Gold Medals
            if self.options.include_gold:
                gold_locs = get_y2roll_medal_locations(world_number, level_number)
                for loc in gold_locs:
                    foo = Y2ROLLLocation(self.player, loc, all_locations_to_id[loc], world_reg)
                    world_reg.locations.append(foo)

    def set_rules(self) -> None:
        set_all_y2roll_rules(self)
        if "Make PUML" in self.options.dev.value:
            from Utils import visualize_regions
            multiworld = self.multiworld
            player = self.player
            puml_name = f"y2roll_world_{self.player_name}_{self.multiworld.seed_name}.puml"
            visualize_regions(multiworld.get_region("Menu", player), puml_name)

    def post_fill(self) -> None:
        pass

    def create_items(self) -> None:
        itempool = []
        # Progression
        if self.options.level_unlocks == self.options.level_unlocks.option_world:
            for k in world_access_item_data_table.keys():
                itempool.append(self.create_item(k))
        # Get count of traps/junk needed
        number_of_items = len(itempool)
        number_of_unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
        needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
        trap_items_needed: int = round((self.options.trap_percentage / 100) * needed_number_of_filler_items)
        needed_number_of_filler_items -= trap_items_needed
        # Traps
        if trap_items_needed > 0:
            trap_items: list[str] = list(trap_item_data_table.keys())
            trap_item_weights: list[int] = []
            for c, i in enumerate(trap_item_data_table.keys()):
                trap_item_weights.append(self.options.trap_weights[i])
            # If traps are needed and weights are missing, reset weights
            if sum(trap_item_weights) == 0:
                trap_item_weights = [1 for _ in trap_item_weights]
            trap_names = self.random.choices(trap_items, trap_item_weights, k=trap_items_needed)
            for name in trap_names:
                itempool.append(self.create_item(name))
        # Junk
        itempool += [self.create_filler() for _ in range(needed_number_of_filler_items)]
        # Start with the first world unlocked
        if self.options.level_unlocks == self.options.level_unlocks.option_world:
            self.push_precollected(self.create_item("Purple Mountains Access"))
        # Final step, always
        self.multiworld.itempool += itempool

    def create_item(self, name: str) -> Y2ROLLItem:
        data = all_items[name]
        item_id = all_items_to_id[name]
        item = Y2ROLLItem(name, data.classification, item_id, self.player)
        return item

    def get_filler_item_name(self) -> str:
        item = self.random.choice(list(junk_item_data_table))
        return item

    def fill_slot_data(self) -> Mapping[str, Any]:
        # Options
        data = self.options.as_dict(
            "level_unlocks",
            "include_gems",
            "include_gold",
            "trap_percentage",
        )
        # Options (but modified)
        data["trap_weights"] = self.output_trap_weights()
        # Metadata
        data["world_version"] = self.world_version
        return data

    def output_trap_weights(self):
        """
        Safely export trap weights to slot data
        """
        trap_data = {}
        for trap_type_name, weight in self.options.trap_weights.value.items():
            if isinstance(weight, int) and weight >= 0:
                trap_data[trap_type_name] = weight
        return trap_data

    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        if "Trap Counts in Spoiler" in self.options.dev.value and self.options.trap_percentage > 0:
            trap_list = [item for item in self.multiworld.itempool if item.trap and item.player == self.player]
            trap_counts = {name: trap_list.count(name) for name in trap_list}
            for name, count in trap_counts.items():
                spoiler_handle.write(f"{name}: {count}\n")
