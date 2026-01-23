from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, PerGameCommonOptions, Range


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


class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps.
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class CameraShakeTrapWeight(Choice):
    """
    Likelihood of a receiving a trap which activates an intense shaky camera visual effect for a short period of time.
    """
    display_name = "Camera Shake Trap Weight"
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 3
    default = 2


class CRTTrapWeight(Choice):
    """
    Likelihood of a receiving a trap which activates an intense CRT visual effect for a short period of time.
    """
    display_name = "CRT Trap Weight"
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 3
    default = 2


class GlitchTrapWeight(Choice):
    """
    Likelihood of a receiving a trap which activates an intense glitchy visual effect for a short period of time.
    """
    display_name = "Glitch Trap Weight"
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 3
    default = 2



class TrapLink(Toggle):
    """
    Whether your received traps are linked to other players.
    """
    display_name = "Trap Link"


@dataclass
class NodebusterOptions(DeathLinkMixin, PerGameCommonOptions):
    goal: Goal
    crypto: CryptoMine
    milestone: Milestones
    bossdrops: BossDrops
    progressive_items: ProgressiveItems
    trap_fill_percentage: TrapFillPercentage
    camera_shake_trap_weight: CameraShakeTrapWeight
    crt_trap_weight: CRTTrapWeight
    glitch_trap_weight: GlitchTrapWeight
    trap_link: TrapLink
