from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item, ItemClassification

class Y2ROLLItem(Item):
    game = "Y2ROLL"


class Y2ROLLItemData(NamedTuple):
    classification: ItemClassification = ItemClassification.progression
    groups: list[str] = []


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
    "Saturation Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
    "Grayscale Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
    ":) Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
    "Minimap Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
    "World Distraction Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
    "Level Distraction Trap": Y2ROLLItemData(ItemClassification.progression, ["Traps"]),
}

junk_item_data_table: dict[str, Y2ROLLItemData] = {
    "A feeling of nostalgia": Y2ROLLItemData(ItemClassification.filler,),
}

all_items = world_access_item_data_table | gem_item_data_table | trap_item_data_table | junk_item_data_table
all_items_to_id = {key: index for index, (key, values) in enumerate(all_items.items())}
