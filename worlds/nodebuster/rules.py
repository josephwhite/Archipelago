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
            "Milestones-1": lambda state: has_milestones_upgrade(world, state, player),
            "NodeFinder1-1": lambda state: has_access_to_blue_enemies(world, state, player),
            "CryptoMine": lambda state: has_crypto_mine(world, state, player)
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