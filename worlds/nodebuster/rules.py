from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule
from Utils import visualize_regions
from .items import progressive_item_to_vanilla, progressive_item_map, get_power_from_vanilla_items, get_power_from_progressive_item

if TYPE_CHECKING:
    from . import NodebusterWorld
else:
    NodebusterWorld = object


def has_boss_drops(world: NodebusterWorld, state: CollectionState, player: int, count: int) -> bool:
    return state.has("Boss Drop", player, count)


def has_crypto_mine(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return state.has("CryptoMine", player)


def has_access_to_blue_enemies(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return state.has_any(["NodeFinder1", "Progressive Blue Spawn"], player)


def has_milestones_upgrade(world: "NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has("Milestones", player)


def has_access_to_net_and_nodes(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return (
            has_crypto_mine(world, state, player)
            and has_access_to_blue_enemies(world, state, player)
    )


def has_access_to_yellow_enemies(world: "NodebusterWorld", state: CollectionState, player: int) -> bool:
    return state.has_any(["YellowSpawn1", "YellowSpawn2", "Progressive Yellow Spawn"], player)


def has_critical_damage(world: "NodebusterWorld", state: CollectionState, player: int) -> bool:
    return (
        state.has("CritChance1", player)
        and state.has_any(["CritDamage1","CritDamage2","Progressive Critical Damage"], player)
    )

def has_number_of_upgrades_per_category(world: NodebusterWorld, state: CollectionState, player: int, group: str, count: int) -> bool:
    vanilla_damage_reqs = progressive_item_to_vanilla(group, count)
    items_list = list(progressive_item_map[group].keys())
    return (
            state.has_all_counts(vanilla_damage_reqs, player)
            or state.has(group, player, count)
            or state.count_from_list(items_list, player) >= count
    )

def has_power_from_prog(world: NodebusterWorld, state: CollectionState, player: int, group: str, thresh: int = 0) -> bool:
    power_calc = 0
    vanilla_items_counted = list(progressive_item_map[group].keys())
    for vanilla_item in vanilla_items_counted:
        numof_item_in_state = state.count(vanilla_item, player)
        #print(f'we habe {numof_item_in_state} of {vanilla_item}')
        powerof_item_in_state = get_power_from_vanilla_items(vanilla_item, numof_item_in_state)
        power_calc = power_calc + powerof_item_in_state
        #print(power_calc)
    # Add power if progressive items are on
    prog_power = state.count(group, player)
    power_from_just_progressive = get_power_from_progressive_item(group, prog_power)
    power_calc = power_calc + power_from_just_progressive
    #print(f'{group} has {power_calc} power from {prog_power} items with {power_from_just_progressive} power, is it more than {thresh}?')
    return power_calc >= thresh


def can_grind_red_milestones(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return (
        has_milestones_upgrade(world, state, player)
        and can_beat_boss13(world, state, player)
        and has_power_from_prog(world, state, player, "Progressive SpawnRate", 3450)
    )

def can_grind_blue_milestones(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return (
            has_milestones_upgrade(world, state, player)
            and can_beat_boss13(world, state, player)
            and has_power_from_prog(world, state, player, "Progressive SpawnRate", 3450)
            and has_power_from_prog(world, state, player, "Progressive Blue Spawn", 5)
    )

def can_grind_yellow_milestones(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return (
            has_milestones_upgrade(world, state, player)
            and can_beat_boss13(world, state, player)
            and has_power_from_prog(world, state, player, "Progressive SpawnRate", 3450)
            and has_power_from_prog(world, state, player, "Progressive Yellow Spawn", 2)
    )

def can_beat_boss0(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 10
    # Health1 = 10
    # Armor1 = 3
    # Boss Armor 1 = 2
    # Regen 1 = 1
    return (
        has_power_from_prog(world, state, player, "Progressive Damage", 10)
        and has_power_from_prog(world, state, player, "Progressive Health", 40)
        and has_power_from_prog(world, state, player, "Progressive Regen", 1)
        and has_power_from_prog(world, state, player, "Progressive Armor", 1)
        and has_power_from_prog(world, state, player, "Progressive Boss Armor", 2)
    )


def can_beat_boss1(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15
    # Health1 = 10
    # Health2 = 4
    # Armor1 = 10
    # Boss Armor 1 = 10
    # Regen 1 = 5
    # Salvaging = 2
    # DamagerPer Enemy1 = 2
    # Spawnrate1 = 15
    # Spawnrate2 = 1
    # Boss Damage1 = 1
    return (
        has_power_from_prog(world, state, player, "Progressive Damage", 15)
        and has_power_from_prog(world, state, player, "Progressive Additional Damage", 5)
        and has_power_from_prog(world, state, player, "Progressive Health", 88)
        and has_power_from_prog(world, state, player, "Progressive Regen", 5)
        and has_power_from_prog(world, state, player, "Progressive Lifesteal", 2)
        and has_power_from_prog(world, state, player, "Progressive Armor", 10)
        and has_power_from_prog(world, state, player, "Progressive Boss Armor", 10)
        and has_power_from_prog(world, state, player, "Progressive Boss Damage", 50)
    )

def can_beat_boss2(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10
    # Health1 = 10, Health2 = 8, Health3 = 3
    # Armor1 = 10, Armor2 = 2
    # Boss Armor 1 = 10
    # Regen 1 = 5, HealthRegen2 = 1
    # Salvaging = 5
    # DamagerPer Enemy1 = 5
    # Spawnrate1 = 11, Spawnrate2 = 1
    # Boss Damage1 = 7
    # Attack Speed (@20%) = 1
    # Size1 = 8
    # RedDrop = 1
    # Nodefinder1 = 1
    # nodeboost = 1
    # milestones = 1

    # has_number_of_upgrades_per_category(world, state, player, "Progressive Damage", 15)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Boss Damage", 1)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Health", 14)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Boss Armor", 10)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Lifesteal", 2)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Additional Damage", 2)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Regen", 5)
    # and has_number_of_upgrades_per_category(world, state, player, "Progressive Armor", 10)
    # and has_spawnrate_and_damageperenemy(world, state, player)
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 45)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 5)
            and has_power_from_prog(world, state, player, "Progressive Health", 376)
            and has_power_from_prog(world, state, player, "Progressive Regen", 6)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 5)
            and has_power_from_prog(world, state, player, "Progressive Armor", 12)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 10)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 350)
    )

def can_beat_boss3(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10, Damage 3 = 3
    # Health1 = 10, Health2 = 8, Health3 = 7
    # Armor1 = 10, Armor2 = 5, Armor3 = 2
    # Boss Armor 1 = 10
    # Regen 1 = 5, HealthRegen2 = 1
    # Salvaging(1) = 5, Health on Hit(50) = 4, Salvaging 2(8) = 0
    # DamagerPer Enemy1 = 5
    # Spawnrate1 = 14, Spawnrate2 = 1
    # Boss Damage1 = 8
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10,
    # RedDrop = 1
    # Nodefinder1 = 1
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 2
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 63)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 5)
            and has_power_from_prog(world, state, player, "Progressive Health", 696)
            and has_power_from_prog(world, state, player, "Progressive Regen", 6)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 205)
            and has_power_from_prog(world, state, player, "Progressive Armor", 17)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 10)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 400)
    )

def can_beat_boss4(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10, Damage 3 = 6
    # Health1 = 10, Health2 = 8, Health3 = 10,
    # Armor1 = 10, Armor2 = 5, Armor3 = 10, Armor4 = 7
    # Boss Armor 1 = 10
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1
    # Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1
    # DamagerPer Enemy1 = 5, Undamaged1 = 2
    # Spawnrate1 = 15, Spawnrate2 = 1
    # Boss Damage1 = 10
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10,
    # RedDrop = 1
    # Nodefinder1 = 1
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 81)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 7)
            and has_power_from_prog(world, state, player, "Progressive Health", 1016)
            and has_power_from_prog(world, state, player, "Progressive Regen", 7)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 32)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 10)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 500)
    )


def can_beat_boss5(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3,
    # Health1 = 10, Health2 = 8, Health3 = 10,
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 1
    # Boss Armor 1 = 10, Boss Armor 2 = 6
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 7
    # Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1
    # DamagerPer Enemy1 = 5, Undamaged1 = 5, Execute1 = 1
    # Spawnrate1 = 15, Spawnrate2 = 1
    # Boss Damage1 = 10, Boss Damage2 = 2
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10,
    # RedDrop = 1
    # Nodefinder1 = 2
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Pickup Health (0.5%) = 1
    # Bolts = 1,
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 180)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 11)
            and has_power_from_prog(world, state, player, "Progressive Health", 1016)
            and has_power_from_prog(world, state, player, "Progressive Regen", 14)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 66)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 160)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 700)
    )


def can_beat_boss6(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3,
    # Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 4
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 3
    # Boss Armor 1 = 10, Boss Armor 2 = 8
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10,
    # Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1
    # DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 2, Execute2 = 2,
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 3
    # Boss Damage1 = 10, Boss Damage2 = 4
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 1, Bolt Damage = 1
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 180)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 21)
            and has_power_from_prog(world, state, player, "Progressive Health", 2216)
            and has_power_from_prog(world, state, player, "Progressive Regen", 17)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 98)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 900)
    )


def can_beat_boss7(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 4
    # Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10,
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 2
    # Boss Armor 1 = 10, Boss Armor 2 = 8
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10,
    # Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 1
    # DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4,
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 3
    # Boss Damage1 = 10, Boss Damage2 = 5
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 5, Bolt Damage = 1
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 580)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 25)
            and has_power_from_prog(world, state, player, "Progressive Health", 4016)
            and has_power_from_prog(world, state, player, "Progressive Regen", 17)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 8263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 102)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1000)
    )


def can_beat_boss8(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 1
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 3
    # Boss Armor 1 = 10, Boss Armor 2 = 8
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4,
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 4
    # Boss Damage1 = 10, Boss Damage2 = 5
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1,
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 25)
            and has_power_from_prog(world, state, player, "Progressive Health", 365936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1000)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 1)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 200)
            and has_critical_damage(world, state, player)
    )


def can_beat_boss9(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 1
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 3
    # (Full Boss Armor) Boss Armor 1 = 10, Boss Armor 2 = 8
    # Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # (Full Addl Damage) DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4, MaxHealthToDamage1 = 1
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 5
    # (Full Boss Damage) Boss Damage1 = 10, Boss Damage2 = 10
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3
    # nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1,
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 26)
            and has_power_from_prog(world, state, player, "Progressive Health", 365936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1500)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 3)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 500)
            and has_power_from_prog(world, state, player, "Progressive Infinity", 1)
            and has_critical_damage(world, state, player)
    )


def can_beat_boss10(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # (FULL HEALTH) Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 5
    # Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 5, MaxHealthToArmor2 = 1,
    # (Full Boss Armor) Boss Armor 1 = 10, Boss Armor 2 = 8
    # (Full Regen) Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # (Full Addl Damage) DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4, MaxHealthToDamage1 = 1
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 5
    # (Full Boss Damage) Boss Damage1 = 10, Boss Damage2 = 10
    # Crit Damage1 = 10. CritDamage2 = 0
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3, nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1, Bolt Damage3 = 3
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 26)
            and has_power_from_prog(world, state, player, "Progressive Health", 765936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1500)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 3)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 500)
            and has_power_from_prog(world, state, player, "Progressive Infinity", 1)
            and has_critical_damage(world, state, player)
    )


def can_beat_boss11(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # (FULL HEALTH) Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 5
    # (Full Armor) Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 5, MaxHealthToArmor2 = 1, RampArmor = 5
    # (Full Boss Armor) Boss Armor 1 = 10, Boss Armor 2 = 8
    # (Full Regen) Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # (Full Addl Damage) DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4, MaxHealthToDamage1 = 1
    # Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 5
    # (Full Boss Damage) Boss Damage1 = 10, Boss Damage2 = 10
    # Crit Damage1 = 10. CritDamage2 = 1
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3, nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1, Bolt Count2 = 1, Bolt Damage3 = 3, KillsToBolts = 6
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 26)
            and has_power_from_prog(world, state, player, "Progressive Health", 765936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1500)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 3)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 700)
            and has_power_from_prog(world, state, player, "Progressive Infinity", 1)
            and has_critical_damage(world, state, player)
    )

def can_beat_boss12(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # (FULL HEALTH) Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 5
    # (Full Armor) Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 5, MaxHealthToArmor2 = 1, RampArmor = 5
    # (Full Boss Armor) Boss Armor 1 = 10, Boss Armor 2 = 8
    # (Full Regen) Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # (Full Addl Damage) DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4, MaxHealthToDamage1 = 1
    # (Full Spawn) Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 5, SpawnRate4 = 5
    # (Full Boss Damage) Boss Damage1 = 10, Boss Damage2 = 10
    # (Full Crit) Crit Damage1 = 10. CritDamage2 = 8
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 3, nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # (full?) Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1, Bolt Count2 = 1, Bolt Damage3 = 3, KillsToBolts = 6
    # Lightning Chance = 3, Chain = 8, Damage = 8
    # Drone = 3, Size = 6, Size2 = 1, Speed = 5, MoveSpeed= 5
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 26)
            and has_power_from_prog(world, state, player, "Progressive Health", 765936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1500)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 3)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 2100)
            and has_power_from_prog(world, state, player, "Progressive Infinity", 1)
            and has_critical_damage(world, state, player)
    )

def can_beat_boss13(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    # (FULL DAMAGE) Damage1 = 15, Damage2 = 10, Damage3 = 10, Damage4 = 3, Damage5 = 5
    # (FULL HEALTH) Health1 = 10, Health2 = 8, Health3 = 10, Health4 = 10, Health5 = 3, Health6 = 5, Health7 = 5
    # (Full Armor) Armor1 = 10, Armor2 = 5, ArmorPerEnemy1 = 10, Armor3 = 10, Armor4 = 10, Armor5 = 20, Armor6 = 30, MaxHealthToArmor1 = 5, Armor7 = 5, FocusArmor1 = 5, MaxHealthToArmor2 = 1, RampArmor = 5
    # (Full Boss Armor) Boss Armor 1 = 10, Boss Armor 2 = 8
    # (Full Regen) Regen 1 = 5, HealthRegen2 = 1 , DropHeal1 = 1, MaxHealthHeal1 = 10, StealMaxHealth1 = 1, MaxHealthHeal2 = 5, StealMaxHealth2 = 1, StealMaxHealth3 = 1
    # (FULL LIFESTEAL) Salvaging(1) = 5, Health on Hit(50) = 5, Salvaging 2(8) = 1, Lifesteal2(1000) = 3, Lifesteal3(5000)= 2
    # (Full Addl Damage) DamagerPer Enemy1 = 5, Undamaged1 = 6, Execute1 = 6, Undamaged2 = 4, Execute2 = 4, MaxHealthToDamage1 = 1
    # (Full Spawn) Spawnrate1 = 15, Spawnrate2 = 1, Spawnrate3 = 5, SpawnRate4 = 5
    # (Full Boss Damage) Boss Damage1 = 10, Boss Damage2 = 10
    # (Full Crit) Crit Damage1 = 10. CritDamage2 = 8
    # Attack Speed (@20%) = 1, Another Attack Speed = 1
    # Size1 = 10, Size2 = 1, Size3 = 1
    # RedDrop = 1
    # Nodefinder1 = 5, nodeboost = 1
    # milestones = 1
    # exploder = 1, exploder size = 4
    # (full?) Bolts = 1, Bolt Count = 5, Bolt Damage = 10, Bolt Explode = 1, Bolt Count2 = 1, Bolt Damage3 = 3, KillsToBolts = 6
    # Lightning Chance = 5, Chain = 8, Damage = 8
    # Drone = 5, Size = 6, Size2 = 1, Speed = 5, MoveSpeed= 5
    return (
            has_power_from_prog(world, state, player, "Progressive Damage", 680)
            and has_power_from_prog(world, state, player, "Progressive Additional Damage", 26)
            and has_power_from_prog(world, state, player, "Progressive Health", 765936)
            and has_power_from_prog(world, state, player, "Progressive Regen", 25)
            and has_power_from_prog(world, state, player, "Progressive Lifesteal", 13263)
            and has_power_from_prog(world, state, player, "Progressive Armor", 108)
            and has_power_from_prog(world, state, player, "Progressive Boss Armor", 210)
            and has_power_from_prog(world, state, player, "Progressive Boss Damage", 1500)
            and has_power_from_prog(world, state, player, "Progressive Damage Per Second", 3)
            and has_power_from_prog(world, state, player, "Progressive Critical Damage", 2100)
            and has_power_from_prog(world, state, player, "Progressive Infinity", 1)
            and has_critical_damage(world, state, player)
    )


def has_all_infinities(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    all_infinities = [
        "Infinity1", "Infinity2", "Infinity3",
        "Infinity4", "Infinity5", "Infinity6",
        "Infinity7", "Infinity8", "Infinity9"
    ]
    prog_infinities = {"Progressive Infinity": 9}
    return (
            state.has_all(all_infinities, player)
            or state.has_all_counts(prog_infinities, player)
    )


def can_release_virus(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return (
            has_crypto_mine(world, state, player)
            and state.has("Laboratory", player)
    )


def released_virus(world: NodebusterWorld, state: CollectionState, player: int) -> bool:
    return state.has("Virus Deployed", player)


def get_location_rules_lookup(world, player: int) -> dict:
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
        "Blues500": lambda state: has_milestones_upgrade(world, state, player),
        "Reds10k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues800": lambda state: can_grind_blue_milestones(world, state, player),
        "Yellows5": lambda state: can_grind_yellow_milestones(world, state, player),
        "Reds15k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues1.2k": lambda state: can_grind_blue_milestones(world, state, player),
        "Yellows10": lambda state: can_grind_yellow_milestones(world, state, player),
        "Reds20k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues1.6k": lambda state:can_grind_blue_milestones(world, state, player),
        "Yellows15": lambda state: can_grind_yellow_milestones(world, state, player),
        "Reds30k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues2k": lambda state: can_grind_blue_milestones(world, state, player),
        "Reds50k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues4k": lambda state: can_grind_blue_milestones(world, state, player),
        "Reds100k": lambda state: can_grind_red_milestones(world, state, player),
        "Blues8k": lambda state: can_grind_blue_milestones(world, state, player),
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
        # Boss Drop progressive order
        "AttackSpeed1-1": lambda state: has_boss_drops(world, state, player, 1),
        "AttackSpeed2-1": lambda state: has_boss_drops(world, state, player, 2),
        "SpawnRate2-1": lambda state: has_boss_drops(world, state, player, 3),
        "DropHeal1-1": lambda state: has_boss_drops(world, state, player, 4),
        "Size2-1": lambda state: has_boss_drops(world, state, player, 5),
        "Size3-1": lambda state: has_boss_drops(world, state, player, 6),
        "MovingPulserSize2-1": lambda state: has_boss_drops(world, state, player, 7),
        "PulseBoltCount2-1": lambda state: has_boss_drops(world, state, player, 8),
        "Infinity1-1": lambda state: has_boss_drops(world, state, player, 9),
        "Infinity2-1": lambda state: has_boss_drops(world, state, player, 10),
        "Infinity3-1": lambda state: has_boss_drops(world, state, player, 11),
        "Infinity4-1": lambda state: has_boss_drops(world, state, player, 12),
        "Infinity5-1": lambda state: has_boss_drops(world, state, player, 13),
        "Infinity6-1": lambda state: has_boss_drops(world, state, player, 14),
        "Infinity7-1": lambda state: has_boss_drops(world, state, player, 15),
        "Infinity8-1": lambda state: has_boss_drops(world, state, player, 16),
        "Infinity9-1": lambda state: has_boss_drops(world, state, player, 17),
        # Boss Requirements
        "Boss-0": lambda state: can_beat_boss0(world, state, player),
        "Boss-1": lambda state: can_beat_boss1(world, state, player),
        "Boss-2": lambda state: can_beat_boss2(world, state, player),
        "Boss-3": lambda state: can_beat_boss3(world, state, player),
        "Boss-4": lambda state: can_beat_boss4(world, state, player),
        "Boss-5": lambda state: can_beat_boss5(world, state, player),
        "Boss-6": lambda state: can_beat_boss6(world, state, player),
        "Boss-7": lambda state: can_beat_boss7(world, state, player),
        "Boss-8": lambda state: can_beat_boss8(world, state, player),
        "Boss-9": lambda state: can_beat_boss9(world, state, player),
        "Boss-10": lambda state: can_beat_boss10(world, state, player),
        "Boss-11": lambda state: can_beat_boss11(world, state, player),
        "Boss-12": lambda state: can_beat_boss12(world, state, player),
        "Boss-13": lambda state: can_beat_boss13(world, state, player),
        "Boss-14": lambda state: can_beat_boss13(world, state, player),
        "Boss-15": lambda state: can_beat_boss13(world, state, player),
        "Boss-16": lambda state: can_beat_boss13(world, state, player),
        "Boss-17": lambda state: can_beat_boss13(world, state, player),
        "Boss-18": lambda state: can_beat_boss13(world, state, player),
        "Boss-19": lambda state: can_beat_boss13(world, state, player),
        "Boss-20": lambda state: can_beat_boss13(world, state, player),
        "Boss-21": lambda state: can_beat_boss13(world, state, player),
        "Boss-22": lambda state: can_beat_boss13(world, state, player),
        "Boss-23": lambda state: can_beat_boss13(world, state, player),
        "Boss-24": lambda state: can_beat_boss13(world, state, player),
        "Boss-25": lambda state: can_beat_boss13(world, state, player),
        # Goal
        "Virus Released": lambda state: can_release_virus(world, state, player),
    }
    return rules_lookup


def get_region_rules_lookup(world, player: int) -> dict:
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
        "Infinity": lambda state: has_access_to_blue_enemies(world, state, player),
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
        "Red Milestones": lambda state: has_milestones_upgrade(world, state, player),
        "Blue Milestones": lambda state: has_milestones_upgrade(world, state, player),
        "Yellow Milestones": lambda state: has_milestones_upgrade(world, state, player),
    }
    return rules_lookup


def set_nodebuster_rules(world: NodebusterWorld) -> None:
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
        multiworld.completion_condition[player] = lambda state: (
            released_virus(world, state, player) and has_all_infinities(world, state, player)
        )
    else:
        multiworld.completion_condition[player] = lambda state: (
            released_virus(world, state, player)
        )

    # visualize_regions(multiworld.get_region("Menu", player), "nodebuster_world.puml")
