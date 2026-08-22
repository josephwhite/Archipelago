from __future__ import annotations

import typing
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, MultiWorld
from .data.basegame import Y2ROLL_WORLD_LEVEL_INFO

if TYPE_CHECKING:
    from .world import Y2ROLLWorld


class Y2ROLLRegion(Region):
    subregions: typing.List[Region] = []


def create_and_connect_regions(world: Y2ROLLWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: Y2ROLLWorld) -> None:
    menu_region = Region("Menu", world.player, world.multiworld)
    w1 = Region("Purple Mountains", world.player, world.multiworld)
    w2 = Region("Deep Sea", world.player, world.multiworld)
    w3 = Region("Chilly Culdesac", world.player, world.multiworld)
    w4 = Region("Downtown City", world.player, world.multiworld)
    w5 = Region("Molten Crag", world.player, world.multiworld)
    w6 = Region("Starry Space", world.player, world.multiworld)
    w7 = Region("Empyrean", world.player, world.multiworld)

    regions = [
        menu_region,
        w1,
        w2,
        w3,
        w4,
        w5,
        w6,
        w7
    ]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: Y2ROLLWorld) -> None:
    menu_region = world.get_region("Menu")
    w1 = world.get_region("Purple Mountains")
    w2 = world.get_region("Deep Sea")
    w3 = world.get_region("Chilly Culdesac")
    w4 = world.get_region("Downtown City")
    w5 = world.get_region("Molten Crag")
    w6 = world.get_region("Starry Space")
    w7 = world.get_region("Empyrean")

    menu_region.connect(w1, "Menu to Purple Mountains")
    menu_region.connect(w2, "Menu to Deep Sea")
    menu_region.connect(w3, "Menu to Chilly Culdesac")
    menu_region.connect(w4, "Menu to Downtown City")
    menu_region.connect(w5, "Menu to Molten Crag")
    menu_region.connect(w6, "Menu to Starry Space")
    menu_region.connect(w7, "Menu to Empyrean")

    #for w in Y2ROLL_WORLD_LEVEL_INFO.keys():
    #    world_name = get_y2roll_world_name(w)
    #    w = world.get_region(world_name)
    #    entrance_name = f"Menu to {world_name}"
    #    menu_region.connect(w, entrance_name)


def create_region(name: str, player: int, world: Y2ROLLWorld) -> Y2ROLLRegion:
    region = Y2ROLLRegion(name, player, world.multiworld)
    world.multiworld.regions.append(region)
    return region


def create_subregion(source_region: Region, name: str) -> Y2ROLLRegion:
    region = Y2ROLLRegion(name, source_region.player, source_region.multiworld)
    connection = Entrance(source_region.player, name, source_region)
    source_region.exits.append(connection)
    connection.connect(region)
    source_region.multiworld.regions.append(region)
    return region
