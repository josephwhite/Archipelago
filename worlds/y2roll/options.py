from dataclasses import dataclass

from Options import DeathLink, PerGameCommonOptions, OptionGroup, Choice, Toggle, Visibility


class LevelUnlocks(Choice):
    """
    Determine how worlds/levels will be unlocked.

    World - Worlds are unlocks (all levels per world are available)
    """
    display_name = "Level Unlocks"
    option_world = 0
    default = option_world


class MakePuml(Toggle):
    """
    Should This APWorld Make a Puml File?
    """
    display_name = "Make Puml"
    visibility = Visibility.none
    default = False


y2roll_options_groups = [
    OptionGroup("Game Options", [
        LevelUnlocks
    ]),
    OptionGroup("DeathLink Options", [
        DeathLink
    ]),
]


@dataclass
class Y2ROLLOptions(PerGameCommonOptions):
    level_unlocks: LevelUnlocks
    death_link: DeathLink
    make_puml: MakePuml
