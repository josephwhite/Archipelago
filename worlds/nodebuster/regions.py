from typing import Dict, List
from BaseClasses import CollectionState

nodebuster_regions_all: Dict[str, List[str]] = {
    "Menu": ["Upgrade Tree"],
    # Bit Regions
    #"Upgrades": ["Milestones"],
    "Damage1Root": ["Potency","Pulse Bolts","Skilled Salvager","Sapper","Scaling Regeneration",
                    "Anti-Purple","Blood Armor","Auto-Collect","Crypto Mine","Milestones",
                    "Spawn Exploders","Net Armor","Transplant","Overloaded"],
    # Node Regions
    "Potency": ["Big Crit","Netblade","Auto Pulser"],
    "Pulse Bolts": ["Bolt Lethality"],
    "Skilled Salvager": [],
    "Sapper": [],
    "Scaling Regeneration": ["Drainer"],
    "Anti-Purple": [],
    "Blood Armor": ["Blood Visage"],
    "Auto-Collect": [],
    "Crypto Mine": ["Processor Acquisition"],
    "Milestones": [],
    "Spawn Exploders": [],

    # Node Regions off of netcoin
    "Thundering": [],
    "Pulser Pursuit": [],
    "Pulse Thumper": [],
    "Unending Parasite": [],

    # Netcoint Regions
    "Bolt Lethality": [],
    "Drainer": [],
    "Blood Visage": [],
    "Processor Acquisition": [],
    "Auto Pulser": ["Pulser Pursuit","Pulse Thumper"],
    "Netblade": ["Thundering"],
    "Big Crit": [],
    "Overloaded": [],
    
    # Netcoin Regions off of main.
    "Transplant": ["Unending Parasite"],
    "Net Armor": [],

    "Upgrade Tree": ["Damage1Root"]

    # Milestone Regions
    #"Red": [],
    #"Blue": [],
    #"Yellow": []
}

every_region: Dict[str,Dict[str,List[str]]] = {
    "regions": {

        "Menu": ["Upgrade Tree"],

        # Bit Regions
        "Damage1Root": ["Damage1Entr"],

        # Node Regions
        "Potency": ["PotencyEntr"],
        "Pulse Bolts": ["PulseBoltsEntr"],
        "Skilled Salvager": [],
        "Sapper": [],
        "Scaling Regeneration": ["ScalingRegenEntr"],
        "Anti-Purple": [],
        "Blood Armor": ["BloodArmorEntr"],
        "Auto-Collect": [],
        "Crypto Mine": ["CryptoMineEntr"],
        "Milestones": ["MilestonesEntr"],
        "Spawn Exploders": [],

        # Node Regions off of netcoin
        "Thundering": [],
        "Pulser Pursuit": [],
        "Pulse Thumper": [],
        "Unending Parasite": [],

        # Netcoint Regions
        "Bolt Lethality": [],
        "Drainer": [],
        "Blood Visage": [],
        "Processor Acquisition": [],
        "Auto Pulser": ["AutoPulserEntr"],
        "Netblade": ["NetbladeEntr"],
        "Big Crit": [],
        "Overloaded": [],

        # Netcoin Regions off of main.
        "Transplant": ["TransplantEntr"],
        "Net Armor": []
    },

    "mandatory_regions": {
        "Upgrade Tree": ["Damage1Root"],
        "Damage1Entr": ["Potency","Pulse Bolts","Skilled Salvager","Sapper","Scaling Regeneration",
                        "Anti-Purple","Blood Armor","Auto-Collect","Crypto Mine","Milestones",
                        "Spawn Exploders","Net Armor","Transplant","Overloaded","Boss Drops"],
        "PotencyEntr": ["Big Crit","Netblade","Auto Pulser"],
        "PulseBoltsEntr": ["Bolt Lethality"],
        "ScalingRegenEntr":["Drainer"],
        "BloodArmorEntr":["Blood Visage"],
        "CryptoMineEntr":["Processor Acquisition","Levels"],
        "MilestonesEntr":["Red","Blue","Yellow"],
        "AutoPulserEntr":["Pulser Pursuit","Pulse Thumper"],
        "NetbladeEntr":["Thundering"],
        "TransplantEntr":["Unending Parasite"],
    },

    "milestone_regions":{
        "Red": [],
        "Blue": [],
        "Yellow": []
    },

    "crypto_regions":{
        "Levels": []
    },

    "boss_regions":{
        "Boss Drops": []
    }
}


milestone_regions_all: Dict[str, List[str]] = {
    "Red": [],
    "Blue": [],
    "Yellow": []
}

crypto_regions_all: Dict[str, List[str]] = {
    "Levels": []
}

boss_regions_all: Dict[str, List[str]] = {
    "Boss Drops": []
}


def _add_milestone_regions() -> None:
    for region in milestone_regions_all.keys():
        nodebuster_regions_all[region] = milestone_regions_all[region]
        nodebuster_regions_all["Milestones"].append(region)

def _add_crypto_regions() -> None:
    for region in crypto_regions_all.keys():
        nodebuster_regions_all[region] = crypto_regions_all[region]
        nodebuster_regions_all["Crypto Mine"].append(region)

def _add_boss_regions() -> None:
    nodebuster_regions_all["Boss Drops"] = []
    nodebuster_regions_all["Damage1Root"].append("Boss Drops")
    return
    for region in boss_regions_all.keys():
        nodebuster_regions_all[region] = boss_regions_all[region]
        nodebuster_regions_all["Damage1Root"].append(region)