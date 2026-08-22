from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
from .data.basegame import Y2ROLL_WORLD_LEVEL_INFO, get_y2roll_world_name
from .locations import get_y2roll_gem_locations

if TYPE_CHECKING:
    from .world import Y2ROLLWorld


def set_all_y2roll_rules(world: Y2ROLLWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: Y2ROLLWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.

    #menu_to_w1 = world.get_entrance("Menu to Purple Mountains")
    #menu_to_w2 = world.get_entrance("Menu to Deep Sea")
    #menu_to_w3 = world.get_entrance("Menu to Chilly Culdesac")
    #menu_to_w4 = world.get_entrance("Menu to Downtown City")
    #menu_to_w5 = world.get_entrance("Menu to Molten Crag")
    #menu_to_w6 = world.get_entrance("Menu to Starry Space")
    #menu_to_w7 = world.get_entrance("Menu to Empyrean")

    if world.options.level_unlocks == world.options.level_unlocks.option_world:
        for w in Y2ROLL_WORLD_LEVEL_INFO.keys():
            world_name = get_y2roll_world_name(w)
            world_access_rule = Has(f"{world_name} Access")
            world_entrance = world.get_entrance(f"Menu to {world_name}")
            world.set_rule(world_entrance, world_access_rule)


def set_all_location_rules(world: Y2ROLLWorld) -> None:
    if world.options.level_unlocks == world.options.level_unlocks.option_world:
        gem_locations = get_y2roll_gem_locations()
        for loc in gem_locations:
            foo = world.get_location(loc)
            world_number = int(loc[0])
            world_name = get_y2roll_world_name(world_number)
            world_access_rule = Has(f"{world_name} Access")
            world.set_rule(foo, world_access_rule)


def set_completion_condition(world: Y2ROLLWorld) -> None:
    world.set_completion_rule(Has("Empyrean Access"))
