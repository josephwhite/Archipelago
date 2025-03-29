from . import SM64MultiworldTestBase
from .. import Options
from ..Locations import loc100Coin_table


class VanillaCoinStarsMultiworldTestBase(SM64MultiworldTestBase):
    options_per_world = [
        {
            "enable_coin_stars": Options.EnableCoinStars.option_vanilla,
        },
        {
            "enable_coin_stars": Options.EnableCoinStars.option_vanilla,
        },
    ]

    # Vanilla Coin Stars option should give the players their own Power Stars.
    def test_items_in_coin_star_locations(self):
        for player in self.multiworld.player_ids:
            for loc in loc100Coin_table:
                # Use subtest to force all locations to be tested
                with self.subTest("Location created for {player}", location=loc):
                    item_in_loc = self.multiworld.worlds[player].get_location(loc).item
                    assert item_in_loc.name == "Power Star"
                    assert item_in_loc.player == player
