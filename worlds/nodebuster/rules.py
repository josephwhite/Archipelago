from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule
from Utils import visualize_regions

if TYPE_CHECKING:
    from . import NodebusterWorld
else:
    NodebusterWorld = object


def has_crypto_mine(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("CryptoMine", player)


def has_access_to_red_enemies(world:"NodebusterWorld", state: CollectionState, player: int):
    return True


def has_access_to_blue_enemies(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("NodeFinder1", player) or state.has("Progressive SpawnRate",player,15)


def has_milestones_upgrade(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("Milestones", player)


def has_access_to_net_and_nodes(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return has_crypto_mine(world, state, player) and has_access_to_blue_enemies(world, state, player)


def has_access_to_yellow_enemies(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("YellowSpawn1", player) or state.has("YellowSpawn2", player) or state.has("Progressive SpawnRate", player,26)


def has_all_infinities(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has_all(["Infinity1","Infinity2","Infinity3","Infinity4","Infinity5","Infinity6","Infinity7","Infinity8","Infinity9"], player)


def can_release_virus(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return has_crypto_mine(world, state, player) and state.has("Laboratory", player)


def released_virus(world:"NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("Virus Deployed", player)


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
                "Lifesteal1-5": lambda state: has_access_to_blue_enemies(world, state, player),
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
                "CryptoMine-1": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-1": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-2": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-3": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-4": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-5": lambda state: has_access_to_blue_enemies(world, state, player),
                "MovingPulserSize1-6": lambda state: has_access_to_blue_enemies(world, state, player),
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


def get_location_rules_lookup(world, player: int):
    rules_lookup = {
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
        "Lifesteal1-5": lambda state: has_access_to_blue_enemies(world, state, player),
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
        "CryptoMine-1": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-1": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-2": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-3": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-4": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-5": lambda state: has_access_to_blue_enemies(world, state, player),
        "MovingPulserSize1-6": lambda state: has_access_to_blue_enemies(world, state, player),
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
        "AutoCollect-8": lambda state: has_access_to_blue_enemies(world, state, player),
        "Virus Released": lambda state: can_release_virus(world, state, player),
    }
    return rules_lookup


def get_region_rules_lookup(world, player: int):
    rules_lookup = {
        # Bits
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
        # Node off of Netcoin
        "Thundering": lambda state: has_access_to_net_and_nodes(world, state, player),
        "Pulser Pursuit": lambda state: has_access_to_net_and_nodes(world, state, player),
        "Pulse Thumper": lambda state: has_access_to_net_and_nodes(world, state, player),
        "Unending Parasite": lambda state: has_access_to_net_and_nodes(world, state, player),
        # Netcoin
        "Bolt Lethality": lambda state: has_crypto_mine(world, state, player),
        "Drainer": lambda state: has_crypto_mine(world, state, player),
        "Blood Visage": lambda state: has_crypto_mine(world, state, player),
        "Processor Acquisition": lambda state: has_crypto_mine(world, state, player),
        "Auto Pulser": lambda state: has_crypto_mine(world, state, player),
        "Netblade": lambda state: has_crypto_mine(world, state, player),
        "Big Crit": lambda state: has_crypto_mine(world, state, player),
        "Transplant": lambda state: has_crypto_mine(world, state, player),
        "Net Armor": lambda state: has_crypto_mine(world, state, player),
        "Crypto Levels": lambda state: has_crypto_mine(world, state, player),
        # Milestones
        "Red": lambda state: has_milestones_upgrade(world, state, player),
        "Blue": lambda state: has_milestones_upgrade(world, state, player),
        "Yellow": lambda state: has_milestones_upgrade(world, state, player)
    }
    return rules_lookup

def set_all_rules(self) -> None:
    multiworld = self.world.multiworld
    player = self.player

    rules_lookup = get_rules_lookup(self, player)

    for entrance_name, rule in rules_lookup["regions"]:

        multiworld.get_entrance(entrance_name, player).access_rule = rule
    
    for location_name, rule in rules_lookup["locations"]:
        multiworld.get_location(location_name, player).access_rule = rule
    

def set_rules(self) -> None:

    multiworld = self.multiworld
    player = self.player

    rules_lookup = get_rules_lookup(self, player)

    region_list = list(multiworld.get_regions(player))

    for entrance_name, rule in rules_lookup["regions"].items():
        if region_list.count(entrance_name) <= 0: continue
        multiworld.get_entrance(entrance_name,player).access_rule = rule
        #set_rule(multiworld.get_entrance(entrance_name, player),rules_lookup["regions"][entrance_name])

    #for location_name, rule in rules_lookup["locations"].items():
    #    multiworld.get_location(location_name, player).access_rule = rule
        #set_rule(multiworld.get_location(location_name, player),rules_lookup["locations"][location_name])

    visualize_regions(multiworld.get_region("Menu",player), "nodebuster_world.puml")

    #for region in multiworld.get_regions(player):
    #    if region.name in rules_lookup["regions"]:
    #        for entrance in region.entrances:
    #            set_rule(entrance, rules_lookup["regions"][region.name])
    #    for loc in region.locations:
    #        if loc.name in rules_lookup["locations"]:
    #            set_rule(loc,rules_lookup["locations"][loc.name])


    multiworld.completion_condition[player] = lambda state: released_virus(state,player)

def set_nodebuster_lmao_rules(world: NodebusterWorld) -> None:
    player = world.player
    multiworld = world.multiworld

    location_rules_lookup = get_location_rules_lookup(world, player)
    for location_name, rule in location_rules_lookup.items():
        set_rule(world.get_location(location_name), rule)

    region_rules_lookup = get_region_rules_lookup(world, player)
    for region_name, rule in region_rules_lookup.items():
        r = world.get_region(region_name)
        for loc in r.locations:
            add_rule(loc, rule)

    if world.options.goal == "release_virus_with_infinity":
        multiworld.completion_condition[player] = lambda state: released_virus(world, state, player) and has_all_infinities(world, state, player)
    else:
        multiworld.completion_condition[player] = lambda state: released_virus(world, state, player)

    # visualize_regions(multiworld.get_region("Menu", player), "nodebuster_world.puml")