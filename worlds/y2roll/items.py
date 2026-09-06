from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class Y2ROLLItem(Item):
    game = "Y2ROLL"


class Y2ROLLItemData(NamedTuple):
    classification: ItemClassification = ItemClassification.progression
    groups: list[str] = []


def get_y2roll_item_groups() -> dict[str, set[str]]:
    result_item_groups: dict[str, set[str]] = {}
    for item in all_items:
        groups = all_items[item].groups
        for group in groups:
            if group not in result_item_groups:
                result_item_groups[group]: set[str] = set()
            result_item_groups[group].add(item)
    return result_item_groups


gem_item_data_table: dict[str, Y2ROLLItemData] = {
    "Gem": Y2ROLLItemData(ItemClassification.progression, []),
}

world_access_item_data_table: dict[str, Y2ROLLItemData] = {
    "Purple Mountains Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Deep Sea Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Chilly Culdesac Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Downtown City Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Molten Crag Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Starry Space Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
    "Empyrean Access": Y2ROLLItemData(ItemClassification.progression, ["World Access"]),
}

trap_item_data_table: dict[str, Y2ROLLItemData] = {
    "Saturation Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    "Grayscale Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    ":) Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    "Minimap Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    "Taunt Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    # TODO: Traps that can change some aspect of the level/world
    #"World Distraction Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
    #"Level Distraction Trap": Y2ROLLItemData(ItemClassification.trap, ["Traps"]),
}

junk_item_data_table: dict[str, Y2ROLLItemData] = {
    "A feeling of nostalgia": Y2ROLLItemData(ItemClassification.filler, ["Junk"]),
}

all_items = world_access_item_data_table | gem_item_data_table | trap_item_data_table | junk_item_data_table
all_items_to_id = {key: index + 1 for index, (key, values) in enumerate(all_items.items())}
