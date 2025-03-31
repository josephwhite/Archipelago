#from .Options import InscryptionOptions, Goal, EpitaphPiecesRandomization, PaintingChecksBalancing
from .options import NodebusterOptions, Goal, CryptoMine
from .items import upgrade_items, ItemDict, base_id, NodebusterItem, milestone_items
from .locations import upgrade_locations, milestone_locations, regions_to_locations
from .regions import nodebuster_regions_all
#from .Items import act1_items, act2_items, act3_items, filler_items, base_id, InscryptionItem, ItemDict
#from .Locations import act1_locations, act2_locations, act3_locations, regions_to_locations
#from .Regions import inscryption_regions_all, inscryption_regions_act_1
from typing import Dict, Any
from . import rules
from .rules import set_all_rules
from BaseClasses import Region, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld


class NodebusterWeb(WebWorld):
    theme = "dirt"

    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Nodebuster Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Emerald"]
    )

    tutorials = [guide_en]

    bug_report_page = "https://github.com/Emerald836/Archipelago-Nodebuster/issues"


class NodebusterWorld(World):
    """
    Nodebuster is a short, experimental incremental game about busting nodes and destroying reality.
    """
    game = "Nodebuster"
    web = NodebusterWeb()
    options_dataclass = NodebusterOptions
    options: NodebusterOptions
    all_items = upgrade_items + milestone_items
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}
    all_locations = upgrade_locations + milestone_locations
    location_name_to_id = {location: i + base_id for i, location in enumerate(all_locations)}


    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_items[item_id - base_id]
        return NodebusterItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        for item in self.all_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        used_regions = nodebuster_regions_all
        for region_name in used_regions.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))

        for region_name, region_connections in used_regions.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations({
                location: self.location_name_to_id[location] for location in regions_to_locations[region_name]
            })

    set_all_rules = set_all_rules
   # def set_rules(self) -> None:
        #rules
        #rules.NodebusterRules(self).set_all_rules()



    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "goal"
        )
