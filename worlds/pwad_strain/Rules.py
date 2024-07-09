# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import DOOM2STRAINWorld


def set_episode1_rules(player, multiworld, pro):
    # Barracks (MAP01)
    set_rule(multiworld.get_entrance("Hub -> Barracks (MAP01) Main", player), lambda state:
        state.has("Barracks (MAP01)", player, 1))
    set_rule(multiworld.get_entrance("Barracks (MAP01) Main -> Barracks (MAP01) Red", player), lambda state:
        state.has("Barracks (MAP01) - Red keycard", player, 1))

    # Outskirts (MAP02)
    set_rule(multiworld.get_entrance("Hub -> Outskirts (MAP02) Main", player), lambda state:
        state.has("Outskirts (MAP02)", player, 1))
    set_rule(multiworld.get_entrance("Outskirts (MAP02) Main -> Outskirts (MAP02) Blue", player), lambda state:
        state.has("Outskirts (MAP02) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Outskirts (MAP02) Blue -> Outskirts (MAP02) Main", player), lambda state:
        state.has("Outskirts (MAP02) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Outskirts (MAP02) Blue -> Outskirts (MAP02) Red", player), lambda state:
       (state.has("Outskirts (MAP02) - Red skull key", player, 1)) and       (state.has("Sawed-off shotgun", player, 1) or
        state.has("Super shotgun", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Chainsaw", player, 1)))

    # Downtown (MAP03)
    set_rule(multiworld.get_entrance("Hub -> Downtown (MAP03) Outside", player), lambda state:
        state.has("Downtown (MAP03)", player, 1))
    set_rule(multiworld.get_entrance("Downtown (MAP03) Outside -> Downtown (MAP03) Main", player), lambda state:
        state.has("Sawed-off shotgun", player, 1) or
        state.has("Super shotgun", player, 1))
    set_rule(multiworld.get_entrance("Downtown (MAP03) Main -> Downtown (MAP03) Yellow", player), lambda state:
        state.has("Downtown (MAP03) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Downtown (MAP03) Yellow -> Downtown (MAP03) Main", player), lambda state:
        state.has("Downtown (MAP03) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Downtown (MAP03) Yellow -> Downtown (MAP03) Red", player), lambda state:
        state.has("Downtown (MAP03) - Red keycard", player, 1))

    # Industrial Zone (MAP04)
    set_rule(multiworld.get_entrance("Hub -> Industrial Zone (MAP04) Main", player), lambda state:
        state.has("Industrial Zone (MAP04)", player, 1))
    set_rule(multiworld.get_entrance("Industrial Zone (MAP04) Main -> Industrial Zone (MAP04) Blue", player), lambda state:
        state.has("Industrial Zone (MAP04) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Industrial Zone (MAP04) Main -> Industrial Zone (MAP04) Red", player), lambda state:
        state.has("Industrial Zone (MAP04) - Red keycard", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Sawed-off shotgun", player, 1))

    # Depot (MAP05)
    set_rule(multiworld.get_entrance("Hub -> Depot (MAP05) Main", player), lambda state:
        state.has("Depot (MAP05)", player, 1))
    set_rule(multiworld.get_entrance("Depot (MAP05) Main -> Depot (MAP05) Red", player), lambda state:
       (state.has("Depot (MAP05) - Red keycard", player, 1)) and       (state.has("Chainsaw", player, 1) or
        state.has("Chaingun", player, 1)))

    # Launch Control (MAP06)
    set_rule(multiworld.get_entrance("Hub -> Launch Control (MAP06) Main", player), lambda state:
       (state.has("Launch Control (MAP06)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Chaingun", player, 1) or
        state.has("Super shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Launch Control (MAP06) Main -> Launch Control (MAP06) Blue", player), lambda state:
        state.has("Launch Control (MAP06) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Launch Control (MAP06) Blue -> Launch Control (MAP06) Red", player), lambda state:
        state.has("Launch Control (MAP06) - Red keycard", player, 1))

    # En Route (MAP07)
    set_rule(multiworld.get_entrance("En Route (MAP07) Main -> En Route (MAP07) Blue", player), lambda state:
        state.has("En Route (MAP07) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("En Route (MAP07) Main -> En Route (MAP07) Yellow", player), lambda state:
        state.has("En Route (MAP07) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("En Route (MAP07) Blue -> En Route (MAP07) Main", player), lambda state:
        state.has("En Route (MAP07) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Hub -> En Route (MAP07) Starting Room", player), lambda state:
        state.has("En Route (MAP07)", player, 1))
    set_rule(multiworld.get_entrance("En Route (MAP07) Starting Room -> En Route (MAP07) Main", player), lambda state:
       (state.has("Sawed-off shotgun", player, 1)) and       (state.has("Super shotgun", player, 1) or
        state.has("Chaingun", player, 1)))
    set_rule(multiworld.get_entrance("En Route (MAP07) Yellow -> En Route (MAP07) Main", player), lambda state:
        state.has("En Route (MAP07) - Yellow keycard", player, 1))

    # Hangar (MAP08)
    set_rule(multiworld.get_entrance("Hub -> Hangar (MAP08) Start", player), lambda state:
        state.has("Hangar (MAP08)", player, 1))
    set_rule(multiworld.get_entrance("Hangar (MAP08) Start -> Hangar (MAP08) Main", player), lambda state:
       (state.has("Sawed-off shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Super shotgun", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Hangar (MAP08) Main -> Hangar (MAP08) Red", player), lambda state:
        state.has("Hangar (MAP08) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Hangar (MAP08) Main -> Hangar (MAP08) Blue", player), lambda state:
        state.has("Hangar (MAP08) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Hangar (MAP08) Blue -> Hangar (MAP08) Yellow", player), lambda state:
        state.has("Hangar (MAP08) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Hangar (MAP08) Yellow -> Hangar (MAP08) Blue", player), lambda state:
        state.has("Hangar (MAP08) - Yellow keycard", player, 1))

    # Cargo Bay (MAP09)
    set_rule(multiworld.get_entrance("Hub -> Cargo Bay (MAP09) Start", player), lambda state:
        state.has("Cargo Bay (MAP09)", player, 1))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Start -> Cargo Bay (MAP09) Main", player), lambda state:
       (state.has("Sawed-off shotgun", player, 1)) and       (state.has("Chaingun", player, 1) or
        state.has("Super shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Main -> Cargo Bay (MAP09) Red", player), lambda state:
        state.has("Cargo Bay (MAP09) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Main -> Cargo Bay (MAP09) Yellow", player), lambda state:
       (state.has("Cargo Bay (MAP09) - Yellow keycard", player, 1) and
        state.has("Super shotgun", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Main -> Cargo Bay (MAP09) Blue", player), lambda state:
        state.has("Cargo Bay (MAP09) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Red -> Cargo Bay (MAP09) Main", player), lambda state:
        state.has("Cargo Bay (MAP09) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP09) Blue -> Cargo Bay (MAP09) Main", player), lambda state:
        state.has("Cargo Bay (MAP09) - Blue keycard", player, 1))

    # Entryway (MAP10)
    set_rule(multiworld.get_entrance("Hub -> Entryway (MAP10) Main", player), lambda state:
       (state.has("Entryway (MAP10)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Chaingun", player, 1) or
        state.has("Super shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Entryway (MAP10) Main -> Entryway (MAP10) Baron Room", player), lambda state:
       (state.has("Chaingun", player, 1)) and       (state.has("Super shotgun", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Entryway (MAP10) Main -> Entryway (MAP10) Blue", player), lambda state:
       (state.has("Super shotgun", player, 1) and
        state.has("Entryway (MAP10) - Blue skull key", player, 1)) and       (state.has("NFG", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Entryway (MAP10) Linedef Skip -> Entryway (MAP10) Blue", player), lambda state:
       (state.has("Super shotgun", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1)))

    # Command Control (MAP11)
    set_rule(multiworld.get_entrance("Hub -> Command Control (MAP11) Main", player), lambda state:
        state.has("Command Control (MAP11)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Main -> Command Control (MAP11) Blue", player), lambda state:
        state.has("Command Control (MAP11) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Main -> Command Control (MAP11) Yellow", player), lambda state:
       (state.has("Command Control (MAP11) - Yellow keycard", player, 1) and
        state.has("Super shotgun", player, 1)) and       (state.has("NFG", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Blue -> Command Control (MAP11) Main", player), lambda state:
        state.has("Command Control (MAP11) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Yellow -> Command Control (MAP11) Main", player), lambda state:
        state.has("Command Control (MAP11) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Yellow -> Command Control (MAP11) Red", player), lambda state:
       (state.has("Command Control (MAP11) - Red keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1) or
        state.has("NFG", player, 1)))
    set_rule(multiworld.get_entrance("Command Control (MAP11) Red -> Command Control (MAP11) Yellow", player), lambda state:
        state.has("Command Control (MAP11) - Red keycard", player, 1))


def set_episode2_rules(player, multiworld, pro):
    # Power Station (MAP12)
    set_rule(multiworld.get_entrance("Hub -> Power Station (MAP12) Start", player), lambda state:
        state.has("Power Station (MAP12)", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Start -> Power Station (MAP12) Main", player), lambda state:
        state.has("Sawed-off shotgun", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Main -> Power Station (MAP12) Barons", player), lambda state:
        state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Main -> Power Station (MAP12) Holobots", player), lambda state:
        state.has("Super shotgun", player, 1) or
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Main -> Power Station (MAP12) Blue", player), lambda state:
       (state.has("Power Station (MAP12) - Blue keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1)))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Holobots -> Power Station (MAP12) Central", player), lambda state:
        state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Central -> Power Station (MAP12) Yellow", player), lambda state:
        state.has("Power Station (MAP12) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Blue -> Power Station (MAP12) Main", player), lambda state:
        state.has("Power Station (MAP12) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Power Station (MAP12) Blue -> Power Station (MAP12) Red", player), lambda state:
        state.has("Power Station (MAP12) - Red keycard", player, 1))

    # Ruins (MAP13)
    set_rule(multiworld.get_entrance("Hub -> Ruins (MAP13) Entrance", player), lambda state:
        state.has("Ruins (MAP13)", player, 1))
    set_rule(multiworld.get_entrance("Ruins (MAP13) Entrance -> Ruins (MAP13) Main", player), lambda state:
       (state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chaingun", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Ruins (MAP13) Main -> Ruins (MAP13) All Keys", player), lambda state:
        state.has("Ruins (MAP13) - Blue skull key", player, 1) and
        state.has("Ruins (MAP13) - Yellow skull key", player, 1) and
        state.has("Ruins (MAP13) - Red skull key", player, 1))

    # Engineering (MAP14)
    set_rule(multiworld.get_entrance("Hub -> Engineering (MAP14) Main", player), lambda state:
        state.has("Engineering (MAP14)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Engineering (MAP14) Main -> Engineering (MAP14) Blue", player), lambda state:
       (state.has("Engineering (MAP14) - Blue keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Engineering (MAP14) Main -> Engineering (MAP14) Yellow", player), lambda state:
       (state.has("Engineering (MAP14) - Yellow keycard", player, 1)) and       (state.has("NFG", player, 1) or
        state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Engineering (MAP14) Main -> Engineering (MAP14) All Keys", player), lambda state:
       (state.has("Engineering (MAP14) - Blue keycard", player, 1) and
        state.has("Engineering (MAP14) - Yellow keycard", player, 1) and
        state.has("Engineering (MAP14) - Red keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1) or
        state.has("NFG", player, 1)))
    set_rule(multiworld.get_entrance("Engineering (MAP14) Blue -> Engineering (MAP14) Main", player), lambda state:
        state.has("Engineering (MAP14) - Blue keycard", player, 1))

    # Subsidiary Power (MAP15)
    set_rule(multiworld.get_entrance("Hub -> Subsidiary Power (MAP15) Main", player), lambda state:
       (state.has("Subsidiary Power (MAP15)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1) or
        state.has("NFG", player, 1)))
    set_rule(multiworld.get_entrance("Subsidiary Power (MAP15) Main -> Subsidiary Power (MAP15) Yellow", player), lambda state:
        state.has("Subsidiary Power (MAP15) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Subsidiary Power (MAP15) Main -> Subsidiary Power (MAP15) Blue", player), lambda state:
        state.has("Subsidiary Power (MAP15) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Subsidiary Power (MAP15) Yellow -> Subsidiary Power (MAP15) Main", player), lambda state:
        state.has("Subsidiary Power (MAP15) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Subsidiary Power (MAP15) Blue -> Subsidiary Power (MAP15) Red", player), lambda state:
        state.has("Subsidiary Power (MAP15) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Subsidiary Power (MAP15) Red -> Subsidiary Power (MAP15) Blue", player), lambda state:
        state.has("Subsidiary Power (MAP15) - Red keycard", player, 1))

    # Living Quarters (MAP16)
    set_rule(multiworld.get_entrance("Hub -> Living Quarters (MAP16) Main", player), lambda state:
        state.has("Living Quarters (MAP16)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Living Quarters (MAP16) Main -> Living Quarters (MAP16) Red", player), lambda state:
       (state.has("Living Quarters (MAP16) - Red skull key", player, 1)) and       (state.has("NFG", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Living Quarters (MAP16) Main -> Living Quarters (MAP16) Blue", player), lambda state:
        state.has("Living Quarters (MAP16) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Living Quarters (MAP16) Main -> Living Quarters (MAP16) Yellow", player), lambda state:
        state.has("Living Quarters (MAP16) - Yellow skull key", player, 1) and
        state.has("NFG", player, 1))
    set_rule(multiworld.get_entrance("Living Quarters (MAP16) Red -> Living Quarters (MAP16) Main", player), lambda state:
        state.has("Living Quarters (MAP16) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Living Quarters (MAP16) Yellow -> Living Quarters (MAP16) Main", player), lambda state:
        state.has("Living Quarters (MAP16) - Yellow skull key", player, 1))

    # Promenade (MAP17)
    set_rule(multiworld.get_entrance("Hub -> Promenade (MAP17) Main", player), lambda state:
        state.has("Promenade (MAP17)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Promenade (MAP17) Main -> Promenade (MAP17) Blue", player), lambda state:
       (state.has("Chaingun", player, 1) and
        state.has("Promenade (MAP17) - Blue keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1) or
        state.has("NFG", player, 1)))
    set_rule(multiworld.get_entrance("Promenade (MAP17) Blue -> Promenade (MAP17) Main", player), lambda state:
        state.has("Promenade (MAP17) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Promenade (MAP17) Blue -> Promenade (MAP17) Red", player), lambda state:
        state.has("Promenade (MAP17) - Red keycard", player, 1))

    # Relay Station (MAP18)
    set_rule(multiworld.get_entrance("Hub -> Relay Station (MAP18) Main", player), lambda state:
       (state.has("Relay Station (MAP18)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Relay Station (MAP18) Main -> Relay Station (MAP18) Blue", player), lambda state:
        state.has("Relay Station (MAP18) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Relay Station (MAP18) Main -> Relay Station (MAP18) Yellow Solo", player), lambda state:
        state.has("Relay Station (MAP18) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Relay Station (MAP18) Main -> Relay Station (MAP18) Red", player), lambda state:
        state.has("Relay Station (MAP18) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Relay Station (MAP18) Blue -> Relay Station (MAP18) Yellow from Blue", player), lambda state:
        state.has("Relay Station (MAP18) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Relay Station (MAP18) Yellow from Blue -> Relay Station (MAP18) Blue", player), lambda state:
        state.has("Relay Station (MAP18) - Yellow keycard", player, 1))

    # Waste Processing (MAP19)
    set_rule(multiworld.get_entrance("Hub -> Waste Processing (MAP19) Main", player), lambda state:
        state.has("Waste Processing (MAP19)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Main -> Waste Processing (MAP19) Yellow", player), lambda state:
        state.has("Waste Processing (MAP19) - Yellow keycard", player, 1) and
        state.has("Super shotgun", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Main -> Waste Processing (MAP19) Blue", player), lambda state:
        state.has("Waste Processing (MAP19) - Blue keycard", player, 1) and
        state.has("Rocket launcher", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Yellow -> Waste Processing (MAP19) Main", player), lambda state:
        state.has("Waste Processing (MAP19) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Yellow -> Waste Processing (MAP19) Blue from Yellow", player), lambda state:
        state.has("Waste Processing (MAP19) - Blue keycard", player, 1) and
        state.has("Rocket launcher", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Blue -> Waste Processing (MAP19) Main", player), lambda state:
        state.has("Waste Processing (MAP19) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Waste Processing (MAP19) Blue from Yellow -> Waste Processing (MAP19) Red", player), lambda state:
        state.has("Waste Processing (MAP19) - Red keycard", player, 1))

    # Reactor (MAP20)
    set_rule(multiworld.get_entrance("Hub -> Reactor (MAP20) Start", player), lambda state:
        state.has("Reactor (MAP20)", player, 1))
    set_rule(multiworld.get_entrance("Reactor (MAP20) Start -> Reactor (MAP20) Main", player), lambda state:
       (state.has("Sawed-off shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Super shotgun", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))


def set_episode3_rules(player, multiworld, pro):
    # Maintenance (MAP21)
    set_rule(multiworld.get_entrance("Hub -> Maintenance (MAP21) Main", player), lambda state:
        state.has("Maintenance (MAP21)", player, 1))
    set_rule(multiworld.get_entrance("Maintenance (MAP21) Main -> Maintenance (MAP21) Yellow", player), lambda state:
        state.has("Maintenance (MAP21) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Maintenance (MAP21) Main -> Maintenance (MAP21) Blue", player), lambda state:
        state.has("Maintenance (MAP21) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Maintenance (MAP21) Yellow -> Maintenance (MAP21) Red", player), lambda state:
        state.has("Maintenance (MAP21) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Maintenance (MAP21) Blue -> Maintenance (MAP21) Cacodemons", player), lambda state:
        state.has("Sawed-off shotgun", player, 1) or
        state.has("Rocket launcher", player, 1) or
        state.has("NFG", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Psychic blaster", player, 1) or
        state.has("Super shotgun", player, 1))

    # Specimen Storage (MAP22)
    set_rule(multiworld.get_entrance("Hub -> Specimen Storage (MAP22) Start", player), lambda state:
        state.has("Specimen Storage (MAP22)", player, 1))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Start -> Specimen Storage (MAP22) Main", player), lambda state:
       (state.has("Super shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chaingun", player, 1)) and       (state.has("Psychic blaster", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Main -> Specimen Storage (MAP22) Red", player), lambda state:
        state.has("Specimen Storage (MAP22) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Main -> Specimen Storage (MAP22) Yellow and Blue", player), lambda state:
        state.has("Specimen Storage (MAP22) - Yellow keycard", player, 1) and
        state.has("Specimen Storage (MAP22) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Main -> Specimen Storage (MAP22) Blue", player), lambda state:
        state.has("Specimen Storage (MAP22) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Red -> Specimen Storage (MAP22) Main", player), lambda state:
        state.has("Specimen Storage (MAP22) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Specimen Storage (MAP22) Yellow and Blue -> Specimen Storage (MAP22) Main", player), lambda state:
        state.has("Specimen Storage (MAP22) - Blue skull key", player, 1) and
        state.has("Specimen Storage (MAP22) - Yellow keycard", player, 1))

    # Dispensary Alpha (MAP23)
    set_rule(multiworld.get_entrance("Hub -> Dispensary Alpha (MAP23) Entry", player), lambda state:
        state.has("Dispensary Alpha (MAP23)", player, 1) and
        state.has("Sawed-off shotgun", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Alpha (MAP23) Entry -> Dispensary Alpha (MAP23) Main", player), lambda state:
       (state.has("Super shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Dispensary Alpha (MAP23) Main -> Dispensary Alpha (MAP23) Yellow", player), lambda state:
        state.has("Dispensary Alpha (MAP23) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Alpha (MAP23) Main -> Dispensary Alpha (MAP23) Blue", player), lambda state:
        state.has("Dispensary Alpha (MAP23) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Alpha (MAP23) Yellow -> Dispensary Alpha (MAP23) Main", player), lambda state:
        state.has("Dispensary Alpha (MAP23) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Alpha (MAP23) Yellow -> Dispensary Alpha (MAP23) Red", player), lambda state:
        state.has("Dispensary Alpha (MAP23) - Red keycard", player, 1))

    # Sub-Laboratory (MAP24)
    set_rule(multiworld.get_entrance("Hub -> Sub-Laboratory (MAP24) Main", player), lambda state:
       (state.has("Sub-Laboratory (MAP24)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Psychic blaster", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Sub-Laboratory (MAP24) Main -> Sub-Laboratory (MAP24) Blue", player), lambda state:
        state.has("Sub-Laboratory (MAP24) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Sub-Laboratory (MAP24) Main -> Sub-Laboratory (MAP24) Yellow", player), lambda state:
        state.has("Sub-Laboratory (MAP24) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Sub-Laboratory (MAP24) Blue -> Sub-Laboratory (MAP24) Main", player), lambda state:
        state.has("Sub-Laboratory (MAP24) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Sub-Laboratory (MAP24) Yellow -> Sub-Laboratory (MAP24) Red", player), lambda state:
        state.has("Sub-Laboratory (MAP24) - Red skull key", player, 1))

    # Main Laboratory (MAP25)
    set_rule(multiworld.get_entrance("Hub -> Main Laboratory (MAP25) Main", player), lambda state:
       (state.has("Main Laboratory (MAP25)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Main -> Main Laboratory (MAP25) Blue", player), lambda state:
        state.has("Main Laboratory (MAP25) - Blue keycard", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Psychic blaster", player, 1) and
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Main -> Main Laboratory (MAP25) Red", player), lambda state:
        state.has("Main Laboratory (MAP25) - Red keycard", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Psychic blaster", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Main -> Main Laboratory (MAP25) Blue Armory", player), lambda state:
        state.has("Main Laboratory (MAP25) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Red -> Main Laboratory (MAP25) Yellow", player), lambda state:
        state.has("Main Laboratory (MAP25) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Yellow -> Main Laboratory (MAP25) Red", player), lambda state:
        state.has("Main Laboratory (MAP25) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory (MAP25) Blue Armory -> Main Laboratory (MAP25) Main", player), lambda state:
        state.has("Main Laboratory (MAP25) - Blue keycard", player, 1))

    # Main Laboratory II (MAP26)
    set_rule(multiworld.get_entrance("Hub -> Main Laboratory II (MAP26) Main", player), lambda state:
       (state.has("Main Laboratory II (MAP26)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chaingun", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("Psychic blaster", player, 1)))
    set_rule(multiworld.get_entrance("Main Laboratory II (MAP26) Main -> Main Laboratory II (MAP26) Yellow", player), lambda state:
        state.has("Main Laboratory II (MAP26) - Yellow skull key", player, 1))
    set_rule(multiworld.get_entrance("Main Laboratory II (MAP26) Yellow -> Main Laboratory II (MAP26) Blue", player), lambda state:
        state.has("Main Laboratory II (MAP26) - Blue skull key", player, 1))

    # Dispensary Beta (MAP27)
    set_rule(multiworld.get_entrance("Hub -> Dispensary Beta (MAP27) Main", player), lambda state:
        state.has("Dispensary Beta (MAP27)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Super shotgun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Psychic blaster", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Main -> Dispensary Beta (MAP27) Southern", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Main -> Dispensary Beta (MAP27) Red", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Main -> Dispensary Beta (MAP27) Yellow", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Southern -> Dispensary Beta (MAP27) Main", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Southern -> Dispensary Beta (MAP27) Red", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Red -> Dispensary Beta (MAP27) Main", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Dispensary Beta (MAP27) Yellow -> Dispensary Beta (MAP27) Main", player), lambda state:
        state.has("Dispensary Beta (MAP27) - Yellow keycard", player, 1))

    # Unknown (MAP28)
    set_rule(multiworld.get_entrance("Hub -> Unknown (MAP28) Main", player), lambda state:
        state.has("Unknown (MAP28)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Psychic blaster", player, 1) and
        state.has("Super shotgun", player, 1))

    # Self-Destruct (MAP29)
    set_rule(multiworld.get_entrance("Hub -> Self-Destruct (MAP29) Main", player), lambda state:
        state.has("Self-Destruct (MAP29)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Psychic blaster", player, 1) and
        state.has("Super shotgun", player, 1))

    # Boss (MAP30)
    set_rule(multiworld.get_entrance("Hub -> Boss (MAP30) Safe Area", player), lambda state:
        state.has("Boss (MAP30)", player, 1))
    set_rule(multiworld.get_entrance("Boss (MAP30) Safe Area -> Boss (MAP30) Main", player), lambda state:
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Psychic blaster", player, 1) and
        state.has("Super shotgun", player, 1))


def set_episode4_rules(player, multiworld, pro):
    # Secret (MAP31)
    set_rule(multiworld.get_entrance("Hub -> Secret (MAP31) Main", player), lambda state:
       (state.has("Secret (MAP31)", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Super shotgun", player, 1) or
        state.has("Chaingun", player, 1)))
    set_rule(multiworld.get_entrance("Secret (MAP31) Main -> Secret (MAP31) Red", player), lambda state:
        state.has("Secret (MAP31) - Red keycard", player, 1) and
        state.has("Super shotgun", player, 1))

    # Super-Secret (MAP32)
    set_rule(multiworld.get_entrance("Hub -> Super-Secret (MAP32) Main", player), lambda state:
        state.has("Super-Secret (MAP32)", player, 1) and
        state.has("Sawed-off shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("NFG", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Psychic blaster", player, 1) and
        state.has("Super shotgun", player, 1))
    set_rule(multiworld.get_entrance("Super-Secret (MAP32) Main -> Super-Secret (MAP32) Red", player), lambda state:
        state.has("Super-Secret (MAP32) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Super-Secret (MAP32) Red -> Super-Secret (MAP32) Main", player), lambda state:
        state.has("Super-Secret (MAP32) - Red skull key", player, 1))


def set_rules(pwad_strain_world: "DOOM2STRAINWorld", included_episodes, pro):
    player = pwad_strain_world.player
    multiworld = pwad_strain_world.multiworld

    if included_episodes[0]:
        set_episode1_rules(player, multiworld, pro)
    if included_episodes[1]:
        set_episode2_rules(player, multiworld, pro)
    if included_episodes[2]:
        set_episode3_rules(player, multiworld, pro)
    if included_episodes[3]:
        set_episode4_rules(player, multiworld, pro)
