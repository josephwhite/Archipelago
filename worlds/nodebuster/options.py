from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions, DefaultOnToggle



class Goal(Choice):
    """Defines the goal to accomplish in order to complete the randomizer.
       
    - Release Virus (Only one that works currently.)
    - Release Virus with all 9 infinity upgrades unlocked
    - Buy every upgrade
    - Buy every upgrade and unlock every milestone
    
    - complete all milestones"""
    display_name = "Goal"
    option_release_virus = 0
    option_release_virus_with_infinity = 1
    option_buy_every_upgrade = 2
    option_unlock_everything = 3
    default = 0


class CryptoMine(Choice):
    """Adds the crypto mine levels as a part of the item pool
       NOT ADDED YET!"""

    display_name = "Crypto Mine"
    option_crypto_unlock = 0
    option_crypto_levels = 1
    default = 0



@dataclass
class NodebusterOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    crypto: CryptoMine