from dataclasses import dataclass

from Options import Toggle, Choice, PerGameCommonOptions, Range, DeathLink


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
    Adds the 36 levels of the CryptoMine into the pool.
    When you level up the crypto mine, instead of speeding up the crypto mine it will instead give you a randomized item from the pool.
    """

    display_name = "Crypto Mine"


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


class DeathLinkAmnesty(Range):
    """
    Amount of Deaths to take before sending a DeathLink signal, for balancing difficulty.
    """
    display_name = "Death Link Amnesty"
    range_start = 0
    range_end = 30
    default = 15


class SendDeathLinkChance(Range):
    """
    When dying, the chance of sending a death link to another player.
    """
    display_name = "Send Death Link Chance"
    range_start = 1
    range_end = 100
    default = 100


class ReceiveDeathLinkChance(Range):
    """
    When receiving a death link, the chance of dying.
    """
    display_name = "Receive Death Link Chance"
    range_start = 1
    range_end = 100
    default = 100


@dataclass
class NodebusterOptions(PerGameCommonOptions):
    goal: Goal
    crypto: CryptoMine
    milestone: Milestones
    bossdrops: BossDrops
    progressive_items: ProgressiveItems
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
    send_death_link_chance: SendDeathLinkChance
    receive_death_link_chance: ReceiveDeathLinkChance
