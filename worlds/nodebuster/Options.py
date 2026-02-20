from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, PerGameCommonOptions, Range, OptionGroup, DeathLink


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
    """
    display_name = "Progressive Items"


class CryptoMine(Toggle):
    """
    Adds all 36 levels of the CryptoMine into the pool.
    When you level up the crypto mine, instead of speeding up the crypto mine it will instead give you a randomized item from the pool.
    """
    display_name = "Crypto Mine"


class AdditionalCryptoMineLevels(Range):
    """
    Adds additional levels to the CryptoMine.
    """
    display_name = "Additional Crypto Mine Levels"
    range_start = 0
    range_end = 100
    default = 0


class Milestones(Toggle):
    """
    Adds the Milestones Rewards and Locations to the item pool.
    """
    display_name = "Milestones"


class BossDrops(Choice):
    """
    Randomize Boss Drops.

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
    #addl_crypto: AdditionalCryptoMineLevels
    milestone: Milestones
    bossdrops: BossDrops
    progressive_items: ProgressiveItems


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

nodebuster_minsanity_options = {
    "goal": Goal.option_release_virus,
    "crypto": CryptoMine.option_false,
    "milestone": Milestones.option_false,
    "bossdrops": BossDrops.option_none,
    "progressive_items": ProgressiveItems.option_false,
}

nodebuster_maxsanity_options = {
    "goal": Goal.option_release_virus_with_infinity,
    "crypto": CryptoMine.option_true,
    "milestone": Milestones.option_true,
    "bossdrops": BossDrops.option_all_26,
    "progressive_items": ProgressiveItems.option_false,
}

nodebuster_options_presets = {
    "Minsanity": nodebuster_minsanity_options,
    "Maxsanity": nodebuster_maxsanity_options,
}
