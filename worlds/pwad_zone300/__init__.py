import functools
import logging
from typing import Any, Dict, List

from BaseClasses import Entrance, CollectionState, Item, Location, MultiWorld, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from . import Items, Locations, Maps, Regions, Rules

from .Options import DOOM2Zone300Options

logger = logging.getLogger("Doom II - Zone 300")

DOOM_TYPE_LEVEL_COMPLETE = -2
DOOM_TYPE_COMPUTER_AREA_MAP = 2026


class DOOM2Zone300Location(Location):
    game: str = "Doom II - Zone 300"


class DOOM2Zone300Item(Item):
    game: str = "Doom II - Zone 300"


class DOOM2Zone300Web(WebWorld):
    tutorials = []
    theme = "dirt"


class DOOM2Zone300World(World):
    """
    Zone 300 is a 33-level PWAD for Doom II, released in 2013 by Paul Corfiatis.
    With the exception of MAP32 and MAP33, every map has at most 300 linedefs, resulting in short and concise maps.
    """
    options_dataclass = DOOM2Zone300Options
    options: DOOM2Zone300Options
    game = "Doom II - Zone 300"
    web = DOOM2Zone300Web()
    required_client_version = (0, 5, 0)  # 1.2.0-prerelease or higher

    item_name_to_id = {data["name"]: item_id for item_id, data in Items.item_table.items()}
    item_name_groups = Items.item_name_groups

    location_name_to_id = {data["name"]: loc_id for loc_id, data in Locations.location_table.items()}
    location_name_groups = Locations.location_name_groups

    starting_level_for_episode: Dict[int, str] = {
        1: "The Spaceport (MAP01)",
        2: "Simbattle (MAP11)",
        3: "Blood Lust (MAP21)"
    }

    # Item ratio that scales depending on episode count. These are the ratio for 3 episode.
    items_ratio: Dict[str, float] = {
        "Armor": 12,
        "Mega Armor": 16,
        "Berserk": 10,
        "Invulnerability": 10,
        "Partial invisibility": 8,
        "Supercharge": 20,
        "Medikit": 6,
        "Box of bullets": 8,
        "Box of rockets": 8,
        "Box of shotgun shells": 8,
        "Energy cell pack": 10,
        "Megasphere": 12
    }

    def __init__(self, multiworld: MultiWorld, player: int):
        self.included_episodes = [1, 1, 1, 0]
        self.location_count = 0
        self.starting_levels = []

        super().__init__(multiworld, player)

    def get_episode_count(self):
        # Don't include 4th, those are secret levels they are additive
        return sum(self.included_episodes[:3])

    def generate_early(self):
        # Cache which episodes are included
        self.included_episodes[0] = self.options.episode1.value
        self.included_episodes[1] = self.options.episode2.value
        self.included_episodes[2] = self.options.episode3.value
        self.included_episodes[3] = self.options.episode4.value # 4th episode are secret levels

        # If no episodes selected, select Episode 1
        if self.get_episode_count() == 0:
            self.included_episodes[0] = 1

        self.starting_levels = [level_name for (episode, level_name) in self.starting_level_for_episode.items()
                                if self.included_episodes[episode - 1]]

    def create_regions(self):
        pro = self.options.pro.value

        # Main regions
        menu_region = Region("Menu", self.player, self.multiworld)
        hub_region = Region("Hub", self.player, self.multiworld)
        self.multiworld.regions += [menu_region, hub_region]
        menu_region.add_exits(["Hub"])

        # Create regions and locations
        main_regions = []
        connections = []
        for region_dict in Regions.regions:
            if not self.included_episodes[region_dict["episode"] - 1]:
                continue

            region_name = region_dict["name"]
            if region_dict["connects_to_hub"]:
                main_regions.append(region_name)

            region = Region(region_name, self.player, self.multiworld)
            region.add_locations({
                loc["name"]: loc_id
                for loc_id, loc in Locations.location_table.items()
                if loc["region"] == region_name and self.included_episodes[loc["episode"] - 1]
            }, DOOM2Zone300Location)

            self.multiworld.regions.append(region)

            for connection_dict in region_dict["connections"]:
                # Check if it's a pro-only connection
                if connection_dict["pro"] and not pro:
                    continue
                connections.append((region, connection_dict["target"]))
        
        # Connect main regions to Hub
        hub_region.add_exits(main_regions)

        # Do the other connections between regions (They are not all both ways)
        for connection in connections:
            source = connection[0]
            target = self.multiworld.get_region(connection[1], self.player)

            entrance = Entrance(self.player, f"{source.name} -> {target.name}", source)
            source.exits.append(entrance)
            entrance.connect(target)

        # Sum locations for items creation
        self.location_count = len(self.multiworld.get_locations(self.player))

    def completion_rule(self, state: CollectionState):
        for map_name in Maps.map_names:
            if map_name + " - Exit" not in self.location_name_to_id:
                continue
            
            # Exit location names are in form: Entryway (MAP01) - Exit
            loc = Locations.location_table[self.location_name_to_id[map_name + " - Exit"]]
            if not self.included_episodes[loc["episode"] - 1]:
                continue

            # Map complete item names are in form: Entryway (MAP01) - Complete
            if not state.has(map_name + " - Complete", self.player, 1):
                return False
            
        return True

    def set_rules(self):
        pro = self.options.pro.value
        allow_death_logic = self.options.allow_death_logic.value

        Rules.set_rules(self, self.included_episodes, pro)
        self.multiworld.completion_condition[self.player] = lambda state: self.completion_rule(state)

        # Forbid progression items to locations that can be missed and can't be picked up. (e.g. One-time timed
        # platform) Unless the user allows for it.
        if not allow_death_logic:
            for death_logic_location in Locations.death_logic_locations:
                self.options.exclude_locations.value.add(death_logic_location)
    
    def create_item(self, name: str) -> DOOM2Zone300Item:
        item_id: int = self.item_name_to_id[name]
        return DOOM2Zone300Item(name, Items.item_table[item_id]["classification"], item_id, self.player)

    def create_items(self):
        itempool: List[DOOM2Zone300Item] = []
        start_with_computer_area_maps: bool = self.options.start_with_computer_area_maps.value

        # Items
        for item_id, item in Items.item_table.items():
            if item["doom_type"] == DOOM_TYPE_LEVEL_COMPLETE:
                continue # We'll fill it manually later

            if item["doom_type"] == DOOM_TYPE_COMPUTER_AREA_MAP and start_with_computer_area_maps:
                continue # We'll fill it manually, and we will put fillers in place

            if item["episode"] != -1 and not self.included_episodes[item["episode"] - 1]:
                continue

            count = item["count"] if item["name"] not in self.starting_levels else item["count"] - 1
            itempool += [self.create_item(item["name"]) for _ in range(count)]

        # Backpack(s) based on options
        if self.options.split_backpack.value:
            itempool += [self.create_item("Bullet capacity") for _ in range(self.options.backpack_count.value)]
            itempool += [self.create_item("Shell capacity") for _ in range(self.options.backpack_count.value)]
            itempool += [self.create_item("Energy cell capacity") for _ in range(self.options.backpack_count.value)]
            itempool += [self.create_item("Rocket capacity") for _ in range(self.options.backpack_count.value)]
        else:
            itempool += [self.create_item("Backpack") for _ in range(self.options.backpack_count.value)]

        # Place end level items in locked locations
        for map_name in Maps.map_names:
            loc_name = map_name + " - Exit"
            item_name = map_name + " - Complete"

            if loc_name not in self.location_name_to_id:
                continue

            if item_name not in self.item_name_to_id:
                continue

            loc = Locations.location_table[self.location_name_to_id[loc_name]]
            if not self.included_episodes[loc["episode"] - 1]:
                continue

            self.multiworld.get_location(loc_name, self.player).place_locked_item(self.create_item(item_name))
            self.location_count -= 1

        # Give starting levels right away
        for map_name in self.starting_levels:
            self.multiworld.push_precollected(self.create_item(map_name))
        
        # Give Computer area maps if option selected
        if start_with_computer_area_maps:
            for item_id, item_dict in Items.item_table.items():
                item_episode = item_dict["episode"]
                if item_episode > 0:
                    if item_dict["doom_type"] == DOOM_TYPE_COMPUTER_AREA_MAP and self.included_episodes[item_episode - 1]:
                        self.multiworld.push_precollected(self.create_item(item_dict["name"]))

        # Fill the rest starting with powerups, then fillers
        self.create_ratioed_items("Armor", itempool)
        self.create_ratioed_items("Mega Armor", itempool)
        self.create_ratioed_items("Berserk", itempool)
        self.create_ratioed_items("Invulnerability", itempool)
        self.create_ratioed_items("Partial invisibility", itempool)
        self.create_ratioed_items("Supercharge", itempool)
        self.create_ratioed_items("Megasphere", itempool)

        while len(itempool) < self.location_count:
            itempool.append(self.create_item(self.get_filler_item_name()))

        # add itempool to multiworld
        self.multiworld.itempool += itempool

    def get_filler_item_name(self):
        return self.multiworld.random.choice([
            "Medikit",
            "Box of bullets",
            "Box of rockets",
            "Box of shotgun shells",
            "Energy cell pack"
        ])

    def create_ratioed_items(self, item_name: str, itempool: List[DOOM2Zone300Item]):
        remaining_loc = self.location_count - len(itempool)
        ep_count = self.get_episode_count()

        # Was balanced based on DOOM 1993's first 3 episodes
        count = min(remaining_loc, max(1, int(round(self.items_ratio[item_name] * ep_count / 3))))
        if count == 0:
            logger.warning(f"Warning, no {item_name} will be placed.")
            return

        for i in range(count):
            itempool.append(self.create_item(item_name))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict("difficulty", "random_monsters", "random_pickups", "random_music", "flip_levels", "allow_death_logic", "pro", "death_link", "reset_level_on_death", "episode1", "episode2", "episode3", "episode4")

        # Send slot data for ammo capacity values; this must be generic because Heretic uses it too
        slot_data["ammo1start"] = self.options.max_ammo_bullets.value
        slot_data["ammo2start"] = self.options.max_ammo_shells.value
        slot_data["ammo3start"] = self.options.max_ammo_energy_cells.value
        slot_data["ammo4start"] = self.options.max_ammo_rockets.value
        slot_data["ammo1add"] = self.options.added_ammo_bullets.value
        slot_data["ammo2add"] = self.options.added_ammo_shells.value
        slot_data["ammo3add"] = self.options.added_ammo_energy_cells.value
        slot_data["ammo4add"] = self.options.added_ammo_rockets.value

        return slot_data
