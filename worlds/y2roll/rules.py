from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has

from .data.basegame import Y2ROLL_LEVEL_BY_KEY, Y2ROLL_WORLD_LEVEL_INFO, get_y2roll_level_entry, get_y2roll_world_name
from .locations import get_y2roll_gem_locations, get_y2roll_goal_locations, get_y2roll_medal_locations

if TYPE_CHECKING:
    from .world import Y2ROLLWorld


def set_all_y2roll_rules(world: Y2ROLLWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: Y2ROLLWorld) -> None:
    if world.options.level_unlocks == world.options.level_unlocks.option_world:
        for w in Y2ROLL_WORLD_LEVEL_INFO.keys():
            world_name = get_y2roll_world_name(w)
            world_access_rule = Has(f"{world_name} Access")
            world_entrance = world.get_entrance(f"Menu to {world_name}")
            world.set_rule(world_entrance, world_access_rule)
    elif world.options.level_unlocks == world.options.level_unlocks.option_level:
        for k, v in Y2ROLL_LEVEL_BY_KEY.items():
            level_name = v["display_name"]
            level_access_rule = Has(f"{level_name} - Access")
            level_entrance = world.get_entrance(f"Menu to {level_name}")
            world.set_rule(level_entrance, level_access_rule)


def set_all_location_rules(world: Y2ROLLWorld) -> None:
    current_locations: list[str] = get_y2roll_goal_locations()
    if world.options.include_gems == world.options.include_gems.option_true:
        gems = get_y2roll_gem_locations()
        current_locations += gems
    if world.options.include_gold == world.options.include_gold.option_true:
        medals = get_y2roll_medal_locations()
        current_locations += medals
    # World/Level Access
    if world.options.level_unlocks == world.options.level_unlocks.option_world:
        for loc in current_locations:
            foo = world.get_location(loc)
            world_number = int(loc[0])
            world_name = get_y2roll_world_name(world_number)
            world_access_rule = Has(f"{world_name} Access")
            world.set_rule(foo, world_access_rule)
    elif world.options.level_unlocks == world.options.level_unlocks.option_level:
        for loc in current_locations:
            foo = world.get_location(loc)
            level_string = loc.split(":", 1)
            world_num, level_num = level_string[0].split("-", 1)
            level_entry = get_y2roll_level_entry(int(world_num), int(level_num))
            level_name = level_entry["display_name"]
            level_access_rule = Has(f"{level_name} - Access")
            world.set_rule(foo, level_access_rule)


def set_completion_condition(world: Y2ROLLWorld) -> None:
    if world.options.level_unlocks == world.options.level_unlocks.option_world:
        world.set_completion_rule(Has("Empyrean Access"))
    elif world.options.level_unlocks == world.options.level_unlocks.option_level:
        world.set_completion_rule(Has("7-15: ASCENDANCE - Access"))
