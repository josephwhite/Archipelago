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

from .data.basegame import Y2ROLL_LEVEL_BY_KEY


class LevelUnlocks(Choice):
    """
    Determine how worlds/levels will be unlocked.

    World - Worlds are unlocks (all levels per world are available)
    Level - Levels are unlocks (all worlds are available)
    """
    display_name = "Level Unlocks"
    option_world = 0
    option_level = 1
    alias_vanilla = 0
    default = option_world


class StartingLevelCount(Range):
    """
    Sets how many levels to start with when Level Unlocks is set to "Level"
    """
    display_name = "Starting Levels"
    range_start = 1
    range_end = 15
    default = 5


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
    display_name = "Gold Medal Checks"


class LevelBlacklist(OptionSet):
    """
    List of levels to exclude.
    """
    display_name = "Level Blacklist"
    valid_keys = [
        i["display_name"]
        for i in Y2ROLL_LEVEL_BY_KEY.values()
        if i["world-level_key"] != "7-15" and not i["world-level_key"].startswith("1-")
    ]
    default = []


class Y2ROLLDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__ + "\n\n    In Y2ROLL, fall outs and time outs send a death."


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
    - Smile Trap: Gives you a smile
    - Minimap Trap: Replaces screen with JUST the minimap
    - Taunt Trap: Displays various taunts on screen
    """
    display_name = "Trap Weights"
    default = dict.fromkeys(trap_item_data_table.keys(), 1)


class TrapLink(Toggle):
    """
    Whether your received traps are linked to other players.

    You will also receive any linked traps from other players with Trap Link enabled,
    if you have a weight above "none" set for that trap
    """
    display_name = "Trap Link"


y2roll_options_groups = [
    OptionGroup("Game Options", [
        LevelUnlocks,
        StartingLevelCount,
        IncludeGems,
        IncludeGold,
        LevelBlacklist
    ]),
    OptionGroup("DeathLink Options", [
        Y2ROLLDeathLink
    ]),
    OptionGroup("Trap Options", [
        TrapPercentage,
        TrapWeights,
        TrapLink
    ]),
]


@dataclass
class Y2ROLLOptions(PerGameCommonOptions):
    level_unlocks: LevelUnlocks
    starting_levels_count: StartingLevelCount
    include_gems: IncludeGems
    include_gold: IncludeGold
    level_blacklist: LevelBlacklist
    death_link: Y2ROLLDeathLink
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_link: TrapLink
