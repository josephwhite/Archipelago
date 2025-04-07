from typing import Dict, List

from BaseClasses import Location

base_id = 268000



class NodebusterLocation(Location):
    game: str = "Nodebuster"


def get_locations() -> List:
    return damage_1_locations + potency_locations + pulse_bolts_locations + skilled_salvager_locations + sapper_locations + scaling_regeneration_locations + anti_purple_locations + blood_armor_locations + auto_collect_locations + crypto_mine_locations + milestone_locations + spawn_exploders_locations + thundering_locations + pulser_pursuit_locations + pulse_thumper_locations + unending_parasite_locations + bolt_lethality_locations + drainer_locations + blood_visage_locations + processor_acquisition_locations + auto_pulser_locations + netblade_locations + big_crit_locations + overloaded_location + transplant_locations + net_armor_locations


def get_milestone_locations() -> List:
    return red_locations + blue_locations + yellow_locations

def get_boss_locations() -> List:
    return boss_locations

def get_crypto_locations() -> List:
    return crypto_mine_levels


damage_1_locations = [
    "Damage1-1", "Damage1-2", "Damage1-3", "Damage1-4",
    "Damage1-5", "Damage1-6", "Damage1-7", "Damage1-8",
    "Damage1-9", "Damage1-10", "Damage1-11", "Damage1-12",
    "Damage1-13", "Damage1-14", "Damage1-15","Health1-1",
    "Health1-2", "Health1-3", "Health1-4", "Health1-5",
    "Health1-6", "Health1-7", "Health1-8", "Health1-9",
    "Health1-10", "SpawnRate1-1", "SpawnRate1-2", "SpawnRate1-3",
    "SpawnRate1-4", "SpawnRate1-5", "SpawnRate1-6", "SpawnRate1-7",
    "SpawnRate1-8", "SpawnRate1-9", "SpawnRate1-10", "SpawnRate1-11",
    "SpawnRate1-12", "SpawnRate1-13", "SpawnRate1-14", "SpawnRate1-15",
    "Armor1-1", "Armor1-2", "Armor1-3", "Armor1-4", "Armor1-5", "Armor1-6",
    "Armor1-7", "Armor1-8", "Armor1-9", "Armor1-10", "BitBoost1-1", "Size1-1",
    "Size1-2", "Size1-3", "Size1-4", "Size1-5", "Size1-6", "Size1-7", "Size1-8",
    "Size1-9", "Size1-10", "BossArmor1-1", "BossArmor1-2", "BossArmor1-3",
    "BossArmor1-4", "BossArmor1-5", "BossArmor1-6", "BossArmor1-7", "BossArmor1-8",
    "BossArmor1-9", "BossArmor1-10", "HealthRegen1-1", "HealthRegen1-2",
    "HealthRegen1-3", "HealthRegen1-4", "HealthRegen1-5", "NodeFinder1-1",
    "NodeFinder1-2", "NodeFinder1-3", "NodeFinder1-4", "NodeFinder1-5",
    "Salvaging1-1", "Salvaging1-2", "Salvaging1-3", "Salvaging1-4",
    "Salvaging1-5", "DamagePerEnemy1-1", "DamagePerEnemy1-2", "DamagePerEnemy1-3",
    "DamagePerEnemy1-4", "DamagePerEnemy1-5", "BossDamage1-1", "BossDamage1-2",
    "BossDamage1-3", "BossDamage1-4", "BossDamage1-5", "BossDamage1-6",
    "BossDamage1-7", "BossDamage1-8", "BossDamage1-9", "BossDamage1-10",
    "AttackSpeed1-1", "BonusDropChance1-1", "BonusDropChance1-2",
    "BonusDropChance1-3", "BonusDropChance1-4", "BonusDropChance1-5",
    "Health2-1", "Health2-2", "Health2-3", "Health2-4",
    "Health2-5", "Health2-6", "Health2-7", "Health2-8", "Armor2-1", "Armor2-2",
    "Armor2-3", "Armor2-4", "Armor2-5","Damage2-1", "Damage2-2",
    "Damage2-3", "Damage2-4", "Damage2-5", "Damage2-6", "Damage2-7", "Damage2-8",
    "Damage2-9", "Damage2-10", "PickupRadius1-1", "PickupRadius1-2",
    "PickupRadius1-3", "PickupRadius1-4", "PickupRadius1-5", "HealthRegen2-1",
    "AttackSpeed2-1", "SpawnRate2-1",
    "NodeBoost1-1", "ArmorPerEnemy1-1", "ArmorPerEnemy1-2", "ArmorPerEnemy1-3",
    "ArmorPerEnemy1-4", "ArmorPerEnemy1-5", "ArmorPerEnemy1-6", "ArmorPerEnemy1-7",
    "ArmorPerEnemy1-8", "ArmorPerEnemy1-9", "ArmorPerEnemy1-10", "Armor3-1",
    "Armor3-2", "Armor3-3", "Armor3-4", "Armor3-5", "Armor3-6", "Armor3-7",
    "Armor3-8", "Armor3-9", "Armor3-10","Health3-1", "Health3-2",
    "Health3-3", "Health3-4", "Health3-5", "Health3-6", "Health3-7", "Health3-8",
    "Health3-9", "Health3-10","Armor4-1", "Armor4-2", "Armor4-3",
    "Armor4-4", "Armor4-5", "Armor4-6", "Armor4-7", "Armor4-8", "Armor4-9",
    "Armor4-10","SpawnRate3-1", "SpawnRate3-2",
    "SpawnRate3-3", "SpawnRate3-4", "SpawnRate3-5", "Armor5-1", "Armor5-2",
    "Armor5-3", "Armor5-4", "Armor5-5", "Armor5-6", "Armor5-7", "Armor5-8",
    "Armor5-9", "Armor5-10", "Armor5-11", "Armor5-12", "Armor5-13", "Armor5-14",
    "Armor5-15", "Armor5-16", "Armor5-17", "Armor5-18", "Armor5-19", "Armor5-20","Size2-1",
    "Armor6-1", "Armor6-2",
    "Armor6-3", "Armor6-4", "Armor6-5", "Armor6-6", "Armor6-7", "Armor6-8",
    "Armor6-9", "Armor6-10", "Armor6-11", "Armor6-12", "Armor6-13", "Armor6-14",
    "Armor6-15", "Armor6-16", "Armor6-17", "Armor6-18", "Armor6-19", "Armor6-20",
    "Armor6-21", "Armor6-22", "Armor6-23", "Armor6-24", "Armor6-25", "Armor6-26",
    "Armor6-27", "Armor6-28", "Armor6-29", "Armor6-30", "BossDamage2-1",
    "BossDamage2-2", "BossDamage2-3", "BossDamage2-4", "BossDamage2-5",
    "BossDamage2-6", "BossDamage2-7", "BossDamage2-8", "BossDamage2-9",
    "BossDamage2-10","Size3-1", "Size3-2", "Size3-3","FocusArmor1-1", "FocusArmor1-2", "FocusArmor1-3",
    "FocusArmor1-4", "FocusArmor1-5"
]

potency_locations = [
    "Damage3-1",
    "Damage3-2", "Damage3-3", "Damage3-4", "Damage3-5", "Damage3-6", "Damage3-7",
    "Damage3-8", "Damage3-9", "Damage3-10", "Undamaged1-1", "Undamaged1-2",
    "Undamaged1-3", "Undamaged1-4", "Undamaged1-5", "Undamaged1-6", "Execute1-1",
    "Execute1-2", "Execute1-3", "Execute1-4", "Execute1-5", "Execute1-6",
    "CritChance1-1", "CritChance1-2", "CritChance1-3", "CritChance1-4",
    "CritChance1-5", "CritChance1-6", "CritChance1-7", "CritChance1-8",
    "CritChance1-9", "CritChance1-10","Damage4-1", "Damage4-2", "Damage4-3",
    "CritDamage1-1", "CritDamage1-2", "CritDamage1-3",
    "CritDamage1-4", "CritDamage1-5", "CritDamage1-6", "CritDamage1-7",
    "CritDamage1-8", "CritDamage1-9", "CritDamage1-10","Undamaged2-1", "Undamaged2-2", "Undamaged2-3",
    "Undamaged2-4", "Execute2-1", "Execute2-2", "Execute2-3", "Execute2-4"
]

pulse_bolts_locations = [
    "PulseBolts-1", "PulseBoltDamage1-1",
    "PulseBoltDamage1-2", "PulseBoltDamage1-3", "PulseBoltDamage1-4",
    "PulseBoltDamage1-5", "PulseBoltDamage1-6", "PulseBoltDamage1-7",
    "PulseBoltDamage1-8", "PulseBoltDamage1-9", "PulseBoltDamage1-10",
    "PulseBoltCount1-1", "PulseBoltCount1-2", "PulseBoltCount1-3",
    "PulseBoltCount1-4", "PulseBoltCount1-5","PulseBoltExplode-1",
    "PulseBoltCount2-1"
]

skilled_salvager_locations = [
    "Salvaging2-1"
]

sapper_locations = [
    "Lifesteal1-1", "Lifesteal1-2",
    "Lifesteal1-3", "Lifesteal1-4", "Lifesteal1-5", "DropHeal1-1"
]

scaling_regeneration_locations = [
    "MaxHealthHeal1-1", "MaxHealthHeal1-2", "MaxHealthHeal1-3", "MaxHealthHeal1-4",
    "MaxHealthHeal1-5", "MaxHealthHeal1-6", "MaxHealthHeal1-7", "MaxHealthHeal1-8",
    "MaxHealthHeal1-9", "MaxHealthHeal1-10"
]

anti_purple_locations = [
    "BossArmor2-1", "BossArmor2-2", "BossArmor2-3", "BossArmor2-4",
    "BossArmor2-5", "BossArmor2-6", "BossArmor2-7", "BossArmor2-8"
]

blood_armor_locations = [
    "MaxHealthToArmor1-1",
    "MaxHealthToArmor1-2", "MaxHealthToArmor1-3", "MaxHealthToArmor1-4",
    "MaxHealthToArmor1-5"
]

auto_collect_locations = [
    "AutoCollect-1", "AutoCollect-2",
    "AutoCollect-3", "AutoCollect-4", "AutoCollect-5", "AutoCollect-6",
    "AutoCollect-7", "AutoCollect-8"
]

crypto_mine_locations = [
    "CryptoMine-1"
]

milestone_locations = [
    "Milestones-1"
]

spawn_exploders_locations = [
    "ExplodersChance-1","ExplodersSize-1",
    "ExplodersSize-2", "ExplodersSize-3", "ExplodersSize-4", "ExplodersSize-5"
]

thundering_locations = [
    "LightningDamage1-1", "LightningDamage1-2",
    "LightningDamage1-3", "LightningDamage1-4", "LightningDamage1-5",
    "LightningDamage1-6", "LightningDamage1-7", "LightningDamage1-8"
]

pulser_pursuit_locations = [
    "MovingPulserSpeed1-1",
    "MovingPulserSpeed1-2", "MovingPulserSpeed1-3", "MovingPulserSpeed1-4",
    "MovingPulserSpeed1-5"
    
]

pulse_thumper_locations = [
    "MovingPulserSize1-1",
    "MovingPulserSize1-2", "MovingPulserSize1-3", "MovingPulserSize1-4",
    "MovingPulserSize1-5", "MovingPulserSize1-6","MovingPulserSize2-1",
    "MovingPulserAttackSpeed1-1",
    "MovingPulserAttackSpeed1-2", "MovingPulserAttackSpeed1-3",
    "MovingPulserAttackSpeed1-4", "MovingPulserAttackSpeed1-5"
]

unending_parasite_locations = [
    "StealMaxHealth1-1","StealMaxHealth2-1","Health6-1",
    "Health6-2", "Health6-3", "Health6-4", "Health6-5", "StealMaxHealth3-1",
    "Health7-1", "Health7-2", "Health7-3", "Health7-4",
    "Health7-5", "Infinity1-1", "Infinity2-1", "Infinity3-1", "Infinity4-1",
    "Infinity5-1", "Infinity6-1", "Infinity7-1", "Infinity8-1", "Infinity9-1",
    "Laboratory-1", "YellowSpawn2-1"
]

bolt_lethality_locations = [
    "PulseBoltDamage2-1",
    "PulseBoltDamage2-2", "PulseBoltDamage2-3",
    "EnemyDeathPulseBolts-1", "EnemyDeathPulseBolts-2", "EnemyDeathPulseBolts-3",
    "EnemyDeathPulseBolts-4", "EnemyDeathPulseBolts-5", "EnemyDeathPulseBolts-6"
]

drainer_locations = [
    "Lifesteal2-1", "Lifesteal2-2", "Lifesteal2-3",
    "Lifesteal3-1", "Lifesteal3-2"
]

blood_visage_locations = [
    "MaxHealthToArmor2-1","RampingArmor1-1", "RampingArmor1-2",
    "RampingArmor1-3", "RampingArmor1-4", "RampingArmor1-5"
]

processor_acquisition_locations = [
    "YellowSpawn1-1"
]

auto_pulser_locations = [
    "MovingPulser1-1", "MovingPulser1-2", "MovingPulser1-3", "MovingPulser1-4",
    "MovingPulser1-5"
]

netblade_locations = [
    "Damage5-1", "Damage5-2",
    "Damage5-3", "Damage5-4", "Damage5-5",
    "RampingDamage1-1", "RampingDamage1-2", "RampingDamage1-3",
    "LightningChance1-1", "LightningChance1-2", "LightningChance1-3",
    "LightningChance1-4", "LightningChance1-5","LightningChainCount1-1",
    "LightningChainCount1-2", "LightningChainCount1-3", "LightningChainCount1-4",
    "LightningChainCount1-5", "LightningChainCount1-6", "LightningChainCount1-7",
    "LightningChainCount1-8","MaxHealthToDamage1-1"
]

big_crit_locations = [
    "CritDamage2-1", "CritDamage2-2", "CritDamage2-3", "CritDamage2-4",
    "CritDamage2-5", "CritDamage2-6", "CritDamage2-7", "CritDamage2-8"
]

overloaded_location = [
    "SpawnRate4-1", "SpawnRate4-2", "SpawnRate4-3", "SpawnRate4-4", "SpawnRate4-5"
]

transplant_locations = [
    "Health4-1",
    "Health4-2", "Health4-3", "Health4-4", "Health4-5", "Health4-6", "Health4-7",
    "Health4-8", "Health4-9", "Health4-10","Health5-1",
    "Health5-2", "Health5-3","MaxHealthHeal2-1",
    "MaxHealthHeal2-2", "MaxHealthHeal2-3", "MaxHealthHeal2-4",
    "MaxHealthHeal2-5"
]

net_armor_locations = [
    "Armor7-1", "Armor7-2", "Armor7-3",
    "Armor7-4", "Armor7-5"
]

blue_locations = [
    "Blues10","Blues100","Blues200","Blues300","Blues500","Blues800","Blues1.2k","Blues1.6k","Blues2k","Blues4k","Blues8k"
]

yellow_locations = [
    "Yellows5","Yellows10","Yellows15"
]

red_locations = [
    "Reds500",
    "Reds2k",
    "Reds4k",
    "Reds6k",
    "Reds8k",
    "Reds10k",
    "Reds15k",
    "Reds20k",
    "Reds30k",
    "Reds50k",
    "Reds100k"
    
]

boss_locations = [
    "Boss-0",
    "Boss-1","Boss-2","Boss-3","Boss-4","Boss-5",
    "Boss-6","Boss-7","Boss-8","Boss-9","Boss-10",
    "Boss-11","Boss-12","Boss-13","Boss-14","Boss-15",
    "Boss-16","Boss-17","Boss-18","Boss-19","Boss-20",
    "Boss-21","Boss-22","Boss-23","Boss-24","Boss-25"
]

crypto_mine_levels = [
    "CryptoLevel-1","CryptoLevel-2","CryptoLevel-3",
    "CryptoLevel-4","CryptoLevel-5","CryptoLevel-6",
    "CryptoLevel-7","CryptoLevel-8","CryptoLevel-9",
    "CryptoLevel-10","CryptoLevel-11","CryptoLevel-12",
    "CryptoLevel-13","CryptoLevel-14","CryptoLevel-15",
    "CryptoLevel-16","CryptoLevel-17","CryptoLevel-18",
    "CryptoLevel-19","CryptoLevel-20","CryptoLevel-21",
    "CryptoLevel-22","CryptoLevel-23","CryptoLevel-24",
    "CryptoLevel-25","CryptoLevel-26","CryptoLevel-27",
    "CryptoLevel-28","CryptoLevel-29","CryptoLevel-30",
    "CryptoLevel-31","CryptoLevel-32","CryptoLevel-33",
    "CryptoLevel-34","CryptoLevel-35","CryptoLevel-36"
]


goal_locations = [
    "Virus Released"
]


regions_to_locations: Dict[str, List[str]] = {
    "Menu": [],
    "Damage1Root": damage_1_locations,
    "Potency": potency_locations,
    "Pulse Bolts": pulse_bolts_locations,
    "Skilled Salvager": skilled_salvager_locations,
    "Sapper": sapper_locations,
    "Scaling Regeneration": scaling_regeneration_locations,
    "Anti-Purple": anti_purple_locations,
    "Blood Armor": blood_armor_locations,
    "Auto-Collect": auto_collect_locations,
    "Crypto Mine": crypto_mine_locations,
    "Milestones": milestone_locations,
    "Spawn Exploders": spawn_exploders_locations,

    # Node Regions off of netcoin
    "Thundering": thundering_locations,
    "Pulser Pursuit": pulser_pursuit_locations,
    "Pulse Thumper": pulse_thumper_locations,
    "Unending Parasite": unending_parasite_locations,

    # Netcoint Regions
    "Bolt Lethality": bolt_lethality_locations,
    "Drainer": drainer_locations,
    "Blood Visage": blood_visage_locations,
    "Processor Acquisition": processor_acquisition_locations,
    "Auto Pulser": auto_pulser_locations,
    "Netblade": netblade_locations,
    "Big Crit": big_crit_locations,
    "Overloaded": overloaded_location,
    
    # Netcoin Regions off of main.
    "Transplant": transplant_locations,
    "Net Armor": net_armor_locations,

    # Milestone Regions
    "Red": red_locations,
    "Blue": blue_locations,
    "Yellow": yellow_locations,

    # Boss Regions
    "Boss Drops": boss_locations,

    # Crypto Mine Levels
    "Levels": crypto_mine_levels,
    "Epilogue": []
}
