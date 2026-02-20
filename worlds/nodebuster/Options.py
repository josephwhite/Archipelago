from dataclasses import dataclass

<<<<<<< nodebuster-crypto
from Options import Toggle, Choice, DeathLinkMixin, PerGameCommonOptions, Range, OptionGroup, DeathLink
=======
from Options import Toggle, Choice, DeathLinkMixin, PerGameCommonOptions
>>>>>>> nodebuster-dev


class Goal(Choice):
    """
    Defines the goal to accomplish in order to complete the randomizer.

    - Release Virus.
    - Release Virus with all 9 infinity upgrades unlocked.
    """
    display_name = "Goal"
    option_release_virus = 0
    option_release_virus_with_infinity = 1
    default = 0


class ProgressiveItems(Toggle):
    """
    Replaces a large portion of items in the pool with progressive versions for the respective upgrade.
<<<<<<< nodebuster-crypto

    WARNING!!! This setting is in very early development. And as such may cause SOFTLOCKS!
=======
>>>>>>> nodebuster-dev
    """
    display_name = "Progressive Items"


class CryptoMine(Toggle):
    """
<<<<<<< nodebuster-crypto
    Adds all  36 levels of the CryptoMine into the pool.
    When you level up the crypto mine, instead of speeding up the crypto mine it will instead give you a randomized item from the pool.
    """
    display_name = "Crypto Mine"
=======
    Adds the 36 levels of the CryptoMine into the pool.
    When you level up the crypto mine, instead of speeding up the crypto mine it will instead give you a randomized item from the pool.
    """
>>>>>>> nodebuster-dev

class AdditionalCryptoMineLevels(Range):
    """
    Adds additional levels to the CryptoMine
    """
    display_name = "Crypto Mine"
    range_start = 0
    range_end = 100
    default = 0


<<<<<<< nodebuster-crypto
class Milestones(Toggle):
    """Adds the Milestones Rewards and Locations to the item pool"""
=======

class Milestones(Toggle):
    """
    Adds the Milestones Rewards and Locations to the item pool.
    """
>>>>>>> nodebuster-dev
    display_name = "Milestones"


class BossDrops(Choice):
    """
<<<<<<< nodebuster-crypto
    Randomize Boss Drops
    Enabling this setting in any capacity could prevent you from being able to beat the game due upgrades being trapped behind bosses that are too strong.
    
=======
    Randomize Boss Drops.

>>>>>>> nodebuster-dev
    - None - No boss drops will be randomized.
    - Necessary Only - All boss drops are randomized but only 18 cores and 8 filler items.
    - All 26 - All 26 levels of boss drops will be randomized.
    """
    display_name = "Boss Drops"
    option_none = 0
    option_necessary = 1
    option_all_26 = 2
    default = 0


@dataclass
class NodebusterOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    crypto: CryptoMine
    milestone: Milestones
    bossdrops: BossDrops
<<<<<<< nodebuster-crypto
    progressiveItems: ProgressiveItems

nodebuster_options_groups = [
    OptionGroup("Goal Options", [
        Goal,
    ]),
    OptionGroup("Gameplay Options", [
        DeathLink,
        ProgressiveItems,
    ]),
    OptionGroup("Logic Options", [
        CryptoMine,
        AdditionalCryptoMineLevels,
        Milestones,
        BossDrops,
    ]),
]
=======
    progressive_items: ProgressiveItems
>>>>>>> nodebuster-dev
