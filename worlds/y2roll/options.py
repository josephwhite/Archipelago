from dataclasses import dataclass

from Options import (
    Choice,
    DeathLink,
    OptionDict,
    OptionGroup,
    OptionSet,
    PerGameCommonOptions,
    Range,
    Toggle,
    Visibility,
)
from worlds.y2roll.items import trap_item_data_table


class LevelUnlocks(Choice):
    """
    Determine how worlds/levels will be unlocked.

    World - Worlds are unlocks (all levels per world are available)
    """
    display_name = "Level Unlocks"
    option_world = 0
    default = option_world


class IncludeGems(Toggle):
    """
    Adds gems in levels as checks. Gem numbers correspond to gems collected, not individual gems.

    Adds 938 possible locations.
    """
    display_name = "Gem Checks"


class IncludeGold(Toggle):
    """
    Adds Gold Medals for levels as checks. Requires clearing the level in a fast time.

    Adds 100 possible locations.
    """
    display_name = "Gold Medal Link"


# TODO: Readd option when functional in client
class Y2ROLLDeathLink(DeathLink):
    visibility = Visibility.none


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.
    """

    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class TrapWeights(OptionDict):
    """
    Determines the relative weights of each Trap type, if Trap Percentage is greater than 0.

    Each weight is required to be zero or more.

    Trap Items are made up of the following types:
    - Saturation Trap: Excessive color on screen
    - Grayscale Trap: Lack of color on screen
    - :) Trap: Gives you a smile
    - Minimap Trap: Replaces screen with JUST the minimap
    - Taunt Trap: Displays various taunts on screen
    """
    display_name = "Trap Weights"
    default = dict.fromkeys(trap_item_data_table.keys(), 1)


# TODO: Readd option when functional in client
class TrapLink(Toggle):
    """
    Whether your received traps are linked to other players

    You will also receive any linked traps from other players with Trap Link enabled,
    if you have a weight above "none" set for that trap
    """
    display_name = "Trap Link"
    visibility = Visibility.none


class Y2ROLLDEV(OptionSet):
    """
    Developer and advanced user options that don't impact game randomization.

    - Trap Counts in Spoiler: Adds count for traps in spoiler.
    - Make PUML: Creates a diagram of connected regions and locations.
    """
    display_name = "Dev"
    valid_keys = [
        "Trap Counts in Spoiler",
        "Make PUML"
    ]
    visibility = Visibility.template | Visibility.spoiler
    default = []


y2roll_options_groups = [
    OptionGroup("Game Options", [
        LevelUnlocks,
        IncludeGems,
        IncludeGold
    ]),
    OptionGroup("DeathLink Options", [
        DeathLink
    ]),
    OptionGroup("Trap Options", [
        TrapPercentage,
        TrapWeights,
        TrapLink
    ]),
    OptionGroup("Dev Options", [
        Y2ROLLDEV
    ])
]


@dataclass
class Y2ROLLOptions(PerGameCommonOptions):
    level_unlocks: LevelUnlocks
    include_gems: IncludeGems
    include_gold: IncludeGold
    death_link: Y2ROLLDeathLink
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_link: TrapLink
    dev: Y2ROLLDEV
