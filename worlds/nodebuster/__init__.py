from typing import Any

from BaseClasses import Entrance, EntranceType, Item, ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World

from . import rules
from .items import (
    NodebusterItem,
    base_id,
    boss_drop_items,
    crypto_level_items,
    junk_items,
    milestone_items,
    progressive_items,
    progressive_items_exclude_list,
    upgrade_items, all_items_to_id,
    all_items
)
from .locations import (
    NodebusterLocation,
    get_boss_locations,
    get_crypto_locations,
    get_locations,
    get_milestone_locations,
    regions_to_locations, all_locations_to_id, crypto_mine_levels, red_locations, yellow_locations, blue_locations,
    boss_locations,
)
from .Options import NodebusterOptions
from .regions import (
    _add_boss_regions,
    _add_crypto_regions,
    _add_milestone_regions,
    _add_milestone_regions,
    every_region,
    nodebuster_regions_all,
)
from .rules import set_all_rules, set_nodebuster_lmao_rules


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

    bug_report_page = "https://github.com/josephwhite/Emerlads-Nodebuster_AP_Mod/issues"


class NodebusterWorld(World):
    """
    Nodebuster is a short, experimental incremental game about busting nodes and destroying reality.
    """
    game = "Nodebuster"
    web = NodebusterWeb()
    options_dataclass = NodebusterOptions
    options: NodebusterOptions
    topology_present = True
    #rule = rules
    item_name_to_id = all_items_to_id
    location_name_to_id = all_locations_to_id

    item_name_groups = {
        "Damage Increase": {
            "Damage1", "DamagePerEnemy1", "BossDamage1", "Damage2", "Damage3", "Undamaged1",
            "Execute1", "Damage4", "BossDamage2", "CritDamage1", "Damage5", "Undamaged2", "Execute2",
            "RampingDamage1", "CritDamage2", "MaxHealthToDamage1"
        },
        "Attack Speed": {
            "AttackSpeed1", "AttackSpeed2"
        },
        "Max Health Increase": {
            "Health1", "Health2", "Health3", "Health4", "Health5", "Health6", "Health7"
        },
        "Health Regen": {
            "HealthRegen1", "Salvaging1", "Lifesteal1", "HealthRegen2", "Salvaging2",
            "DropHeal1", "MaxHealthHeal1", "Lifesteal2", "Lifesteal3",
            "StealMaxHealth1", "MaxHealthHeal2", "StealMaxHealth2", "StealMaxHealth3"
        },
        "SpawnRate Increase": {
            "SpawnRate1", "SpawnRate2", "SpawnRate3", "SpawnRate4", "NodeFinder1", "YellowSpawn1", "YellowSpawn2"
        },
        "Armor Increase": {
            "Armor1", "BossArmor1", "Armor2", "ArmorPerEnemy1", "Armor3", "Armor4", "BossArmor2", "Armor5", "Armor6",
            "MaxHealthToArmor1", "Armor7", "FocusArmor1", "MaxHealthToArmor2", "RampingArmor1"
        },
        "Infinity": {
            "Infinity1", "Infinity2", "Infinity3", "Infinity4", "Infinity5", "Infinity6", "Infinity7", "Infinity8",
            "Infinity9"
        },
        "Red Milestone Rewards": {
            "Reds500", "Reds2k", "Reds4k", "Reds6k", "Reds8k",
            "Reds10k", "Reds15k", "Reds20k", "Reds30k", "Reds50k", "Reds100k",
        },
        "Blue Milestone Rewards": {
            "Blues10", "Blues100", "Blues200", "Blues300", "Blues500",
            "Blues800", "Blues1.2k", "Blues1.6k", "Blues2k", "Blues4k", "Blues8k"
        },
        "Yellow Milestone Rewards": {
            "Yellows5", "Yellows10", "Yellows15"
        },
        "Milestone Rewards": {
            "Reds500", "Blues10", "Reds2k", "Blues100", "Reds4k", "Blues200", "Reds6k", "Blues300", "Reds8k",
            "Blues500",
            "Reds10k", "Blues800", "Yellows5", "Reds15k", "Blues1.2k", "Yellows10", "Reds20k", "Blues1.6k", "Yellows15",
            "Reds30k", "Blues2k", "Reds50k", "Blues4k", "Reds100k", "Blues8k"
        }
    }

    def generate_basic(self):
        self.multiworld.get_location("Virus Released", self.player).place_locked_item(
            self.create_item("Virus Deployed"))

        if not self.options.crypto:
            for cml in crypto_mine_levels:
                self.multiworld.get_location(cml, self.player).place_locked_item(self.create_item("CryptoLevel"))

        if not self.options.milestone:
            if self.options.progressiveItems:
                for red in red_locations:
                    self.multiworld.get_location(red, self.player).place_locked_item(
                        self.create_item("Progressive Red Milestone Reward"))
                for blue in blue_locations:
                    self.multiworld.get_location(blue, self.player).place_locked_item(
                        self.create_item("Progressive Blue Milestone Reward"))
                for yellow in yellow_locations:
                    self.multiworld.get_location(yellow, self.player).place_locked_item(
                        self.create_item("Progressive Yellow Milestone Reward"))
            else:
                for red in red_locations:
                    self.multiworld.get_location(red, self.player).place_locked_item(self.create_item(red))
                for blue in blue_locations:
                    self.multiworld.get_location(blue, self.player).place_locked_item(self.create_item(blue))
                for yellow in yellow_locations:
                    self.multiworld.get_location(yellow, self.player).place_locked_item(self.create_item(yellow))

        if not self.options.bossdrops:
            for boss in boss_locations:
                self.multiworld.get_location(boss, self.player).place_locked_item(self.create_item("Boss Drop"))

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = all_items[item_id - base_id]
        return NodebusterItem(name, item_data["classification"], item_id, self.player)

    def create_regions(self) -> None:
        # Create Regions
        for region, connected_regions in nodebuster_regions_all.items():
            r = Region(region, self.player, self.multiworld)
            for i in regions_to_locations[region]:
                loc = NodebusterLocation(self.player, i, self.location_name_to_id.get(i, None), r)
                r.locations.append(loc)
            self.multiworld.regions.append(r)
        # Connect Regions
        for region, connected_regions in nodebuster_regions_all.items():
            r = self.multiworld.get_region(region, self.player)
            for conn in connected_regions:
                c = self.multiworld.get_region(conn, self.player)
                r.connect(c)

    def create_items(self) -> None:
        for item in all_items:
            if not self.options.milestone:
                if item in milestone_items:
                    item["count"] = 0
                    continue
                if item["name"] == "Progressive Milestone Reward":
                    item["count"] = 0
                    continue
                elif item["name"] == "Progressive Red Milestone Reward":
                    item["count"] = 0
                    continue
                elif item["name"] == "Progressive Blue Milestone Reward":
                    item["count"] = 0
                    continue
                elif item["name"] == "Progressive Yellow Milestone Reward":
                    item["count"] = 0
                    continue
            if not self.options.crypto:
                if item in crypto_level_items:
                    item["count"] = 0
                    continue
            if not self.options.progressiveItems:
                if item in progressive_items:
                    continue
            else:
                if item["name"] in progressive_items_exclude_list:
                    continue
            match self.options.bossdrops:
                case 0:
                    if item in boss_drop_items:
                        item["count"] = 0
                        continue
                case 1:
                    if item["name"] == "Boss Drop":
                        item["count"] = 18
                    elif item["name"] == "Extra Bits":
                        item["count"] = 4
                    elif item["name"] == "Extra Nodes":
                        item["count"] = 4
                case 2:
                    if item["name"] == "Boss Drop":
                        item["count"] = 26
                    elif item["name"] == "Extra Bits":
                        item["count"] = 0
                        continue
                    elif item["name"] == "Extra Nodes":
                        item["count"] = 0
                        continue

            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)

        #junk = len(self.all_locations) - len(self.all_items)
        #self.multiworld.itempool += [self.create_item("Nothing") for _ in range(junk)]

    def set_rules(self):
        set_nodebuster_lmao_rules(self)

    def fill_slot_data(self) -> dict[str, Any]:
        return self.options.as_dict(
            "death_link",
            "goal"
        )
