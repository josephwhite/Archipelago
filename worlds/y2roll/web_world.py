from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from worlds.y2roll.options import y2roll_options_groups


class Y2ROLLWebWorld(WebWorld):
    game = "Y2ROLL"
    theme = "partyTime"
    option_groups = y2roll_options_groups
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Y2ROLL for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["josephwhite"],
    )
    tutorials = [setup_en]

