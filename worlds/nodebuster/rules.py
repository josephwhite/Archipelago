from typing import Dict, Callable, TYPE_CHECKING
from BaseClasses import CollectionState, Location, Entrance, LocationProgressType
from worlds.generic.Rules import set_rule
from .Options import Goal

if TYPE_CHECKING:
    from . import NodebusterWorld
else:
    NodebusterWorld = object

def has_crypto_mine(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("CryptoMine", player)

def has_access_to_blue_enemies(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("NodeFinder1", player)

def has_milestones_upgrade(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("Milestones", player)

def has_access_to_net_and_nodes(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return has_crypto_mine(world,state,player) and has_access_to_blue_enemies(world,state,player)

def has_access_to_yellow_enemies(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("YellowSpawn1", player) or state.has("YellowSpawn2", player)

def get_rules_lookup(world, player: int):
        rules_lookup = {
            "locations": {
                """"Milestones-1": lambda state: has_access_to_blue_enemies(world, state, player),
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
                "AutoCollect-8": lambda state: has_access_to_blue_enemies(world, state, player)"""
            },
            "regions": {
                # Node
                "Potency": lambda state: has_access_to_blue_enemies(world, state, player), 
                "Pulse Bolts": lambda state: has_access_to_blue_enemies(world, state, player),
                "Skilled Salvager": lambda state: has_access_to_blue_enemies(world, state, player),
                "Sapper": lambda state: has_access_to_blue_enemies(world, state, player),
                "Scaling Regeneration": lambda state: has_access_to_blue_enemies(world, state, player),
                "Anti-Purple": lambda state: has_access_to_blue_enemies(world, state, player),
                "Blood Armor": lambda state: has_access_to_blue_enemies(world, state, player),
                "Auto-Collect": lambda state: has_access_to_blue_enemies(world, state, player),
                "Crypto Mine": lambda state: has_access_to_blue_enemies(world, state, player),
                "Milestones": lambda state: has_access_to_blue_enemies(world, state, player),
                "Spawn Exploders": lambda state: has_access_to_blue_enemies(world, state, player),
                #Node off of Netcoin
                "Thundering": lambda state: has_access_to_net_and_nodes(world, state, player),
                "Pulser Pursuit": lambda state: has_access_to_net_and_nodes(world, state, player),
                "Pulse Thumper": lambda state: has_access_to_net_and_nodes(world, state, player),
                "Unending Parasite": lambda state: has_access_to_net_and_nodes(world, state, player),
                #Netcoin
                "Bolt Lethality": lambda state: has_crypto_mine(world, state, player),
                "Drainer": lambda state: has_crypto_mine(world, state, player),
                "Blood Visage": lambda state: has_crypto_mine(world, state, player),
                "Processor Acquisition": lambda state: has_crypto_mine(world, state, player),
                "Auto Pulser": lambda state: has_crypto_mine(world, state, player),
                "Netblade": lambda state: has_crypto_mine(world, state, player),
                "Big Crit": lambda state: has_crypto_mine(world, state, player),
                "Transplant": lambda state: has_crypto_mine(world, state, player),
                "Net Armor": lambda state: has_crypto_mine(world, state, player),

                #Milestones
                "Red": lambda state: has_milestones_upgrade(world, state, player),
                "Blue": lambda state: has_milestones_upgrade(world, state, player),
                "Yellow": lambda state: has_milestones_upgrade(world, state, player)
            }
        }
        return rules_lookup

def set_all_rules(self) -> None:
    multiworld = self.world.multiworld
    player = self.player

    rules_lookup = get_rules_lookup(self, player)

    for entrance_name, rule in rules_lookup["locations"]:
        multiworld.get_entrance(entrance_name, player).access_rule = rule
    
    for location_name, rule in rules_lookup["locations"]:
        multiworld.get_location(location_name, player).access_rule = rule
    

    

    #for region in multiworld.get_regions(player):
    #    if region.name in rules_lookup["regions"]:
    #        for entrance in region.entrances:
    #            set_rule(entrance, rules_lookup["regions"][region.name])
    #    for loc in region.locations:
    #        if loc.name in rules_lookup["locations"]:
    #            set_rule(loc,rules_lookup["locations"][loc.name])

    

    def released_virus(state: CollectionState,player: int) -> bool:
        return state.has("Virus Deployed", player)

    multiworld.completion_condition[player] = lambda state: released_virus(state,player)
