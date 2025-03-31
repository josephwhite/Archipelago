from typing import Dict, Callable, TYPE_CHECKING
from BaseClasses import CollectionState, LocationProgressType
from .options import Goal

if TYPE_CHECKING:
    from . import NodebusterWorld
else:
    NodebusterWorld = object


class NodebusterRules:
    player: int
    world: NodebusterWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: NodebusterWorld) -> None:
        self.player = world.player
        self.world = world
        self.location_rules = {
            "Milestones-1": lambda state: self.has_milestone_upgrade(state),
            "NodeFinder1-1": lambda state: self.has_access_to_blue_enemies(state)
            #"NodeFinder1-2": self.has_access_to_blue_enemies,
            #"NodeFinder1-3": self.has_access_to_blue_enemies,
            #"NodeFinder1-4": self.has_access_to_blue_enemies,
            #"NodeFinder1-5": self.has_access_to_blue_enemies
        }
    

def get_rules_lookup(world, player: int):
    rules_lookup = {
        "locations": {
            "Milestones-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Reds500": lambda state: has_milestones_upgrade(world, state, player),
            "Blues10": lambda state: has_milestones_upgrade(world, state, player),
            "Reds2k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues100": lambda state: has_milestones_upgrade(world, state, player),
            "Reds4k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues200": lambda state: has_milestones_upgrade(world, state, player),
            "Reds6k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues300": lambda state: has_milestones_upgrade(world, state, player),
            "Reds8k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues300": lambda state: has_milestones_upgrade(world, state, player),
            "Reds8k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues500": lambda state: has_milestones_upgrade(world, state, player),
            "Reds10k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues800": lambda state: has_milestones_upgrade(world, state, player),
            "Yellows5": lambda state: has_milestones_upgrade(world, state, player),
            "Reds15k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues1.2k": lambda state: has_milestones_upgrade(world, state, player),
            "Yellows10": lambda state: has_milestones_upgrade(world, state, player),
            "Reds20k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues1.6k": lambda state: has_milestones_upgrade(world, state, player),
            "Yellows15": lambda state: has_milestones_upgrade(world, state, player),
            "Reds30k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues2k": lambda state: has_milestones_upgrade(world, state, player),
            "Reds50k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues4k": lambda state: has_milestones_upgrade(world, state, player),
            "Reds100k": lambda state: has_milestones_upgrade(world, state, player),
            "Blues8k": lambda state: has_milestones_upgrade(world, state, player),
            "NodeFinder1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "ExplodersChance-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Lifesteal1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Lifesteal1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "Lifesteal1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "Lifesteal1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "Lifesteal1,5": lambda state: has_access_to_blue_enemies(world, state, player),
            "Salvaging2-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "PulseBolts-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-7": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-8": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-9": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthHeal1-10": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-7": lambda state: has_access_to_blue_enemies(world, state, player),
            "BossArmor2-8": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-7": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-8": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-9": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage3-10": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage4-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage4-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "Damage4-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "CryptoMine": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSize1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSize1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSize1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSize1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSize1-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "MoveingPulserSize1-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "MaxHealthToArmor1-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "StealMaxHealth1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "PulseBoltExplode-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSpeed1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSpeed1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSpeed1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSpeed1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "MovingPulserSpeed1-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "StealMaxHealth2-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Health6-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "Health6-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "Health6-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "Health6-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "Health6-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-7": lambda state: has_access_to_blue_enemies(world, state, player),
            "LightningDamage1-8": lambda state: has_access_to_blue_enemies(world, state, player),
            "YellowSpawn2-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-2": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-3": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-4": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-5": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-6": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-7": lambda state: has_access_to_blue_enemies(world, state, player),
            "AutoCollect-8": lambda state: has_access_to_blue_enemies(world, state, player)
        }
    }
    return rules_lookup


    def has_milestone_upgrade(self, state: CollectionState) -> bool:
        return state.has("Milestones",self.player)
    
    def has_access_to_blue_enemies(self, state: CollectionState) -> bool:
        return state.has("NodeFinder1",self.player)

def has_crypto_mine(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("CryptoMine", player)


def has_access_to_blue_enemies(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("NodeFinder1", player)


def has_milestones_upgrade(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("Milestones", player)

def set_all_rules(self: "NodebusterWorld") -> None:
    multiworld = self.world.multiworld
    player = self.player

    rules_lookup = get_rules_lookup(self, player)

    for location_name, rule in rules_lookup["locations"].items():
        multiworld.get_location(location_name, player).access_rule = rule

   # for location_name, rule in self.location_rules.items():
    #    multiworld.get_location(location_name, player).access_rule = rule
       # for region in multiworld.get_regions(self.player):
       #     for loc in region.locations:
       #         if loc.name in self.location_rules:
       #             loc.access_rule = self.location_rules[loc.name]

    def released_virus(state: CollectionState) -> bool:
        return state.has("Virus Deployed", player)

    multiworld.completion_condition[player] = lambda state: released_virus(state)