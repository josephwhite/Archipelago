from BaseClasses import Location

from .data.basegame import Y2ROLL_LEVEL_BY_KEY, get_level_gem_count


class Y2ROLLLocation(Location):
    game = "Y2ROLL"


def get_y2roll_gem_locations(world_num: int | None = None, level_num: int | None = None) -> list[str]:
    gem_locations: list[str] = []
    for k, v in Y2ROLL_LEVEL_BY_KEY.items():
        if world_num is None or v["world"] == world_num:
            if level_num is None or v["level_in_world"] == level_num:
                level = v["display_name"]
                count = get_level_gem_count(k)
                for i in range(1, count + 1):
                    loc_name = f"{level} - Gem {i}"
                    gem_locations.append(loc_name)
    return gem_locations


all_locations = get_y2roll_gem_locations()
all_locations_to_id = {item: index + 1 for index, item in enumerate(all_locations)}


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: all_locations_to_id[location_name] for location_name in location_names}
