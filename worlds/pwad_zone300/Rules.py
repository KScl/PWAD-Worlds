# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import DOOM2Zone300World


def set_episode1_rules(player, multiworld, pro):
    # The Spaceport (MAP01)
    set_rule(multiworld.get_entrance("Hub -> The Spaceport (MAP01) Main", player), lambda state:
        state.has("The Spaceport (MAP01)", player, 1))

    # Control Facility (MAP02)
    set_rule(multiworld.get_entrance("Hub -> Control Facility (MAP02) Main", player), lambda state:
        state.has("Control Facility (MAP02)", player, 1))
    set_rule(multiworld.get_entrance("Control Facility (MAP02) Main -> Control Facility (MAP02) Yellow", player), lambda state:
       (state.has("Control Facility (MAP02) - Yellow keycard", player, 1)) and       (state.has("Super Shotgun", player, 1) or
        state.has("Shotgun", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Chainsaw", player, 1)))
    set_rule(multiworld.get_entrance("Control Facility (MAP02) Yellow -> Control Facility (MAP02) Red", player), lambda state:
        state.has("Control Facility (MAP02) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Control Facility (MAP02) Yellow -> Control Facility (MAP02) Blue", player), lambda state:
        state.has("Control Facility (MAP02) - Blue keycard", player, 1))

    # The Alleyway (MAP03)
    set_rule(multiworld.get_entrance("Hub -> The Alleyway (MAP03) Main", player), lambda state:
       (state.has("The Alleyway (MAP03)", player, 1)) and
       (state.has("Shotgun", player, 1) or
        state.has("Super Shotgun", player, 1) or
        state.has("Chainsaw", player, 1) or
        state.has("Chaingun", player, 1)))
    set_rule(multiworld.get_entrance("The Alleyway (MAP03) Main -> The Alleyway (MAP03) Blue", player), lambda state:
        state.has("The Alleyway (MAP03) - Blue keycard", player, 1))

    # Canyon Hub (MAP04)
    set_rule(multiworld.get_entrance("Hub -> Canyon Hub (MAP04) Main", player), lambda state:
       (state.has("Canyon Hub (MAP04)", player, 1)) and
       (state.has("Shotgun", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Super Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Canyon Hub (MAP04) Main -> Canyon Hub (MAP04) Yellow", player), lambda state:
        state.has("Canyon Hub (MAP04) - Yellow keycard", player, 1))

    # Skybase 300 (MAP05)
    set_rule(multiworld.get_entrance("Hub -> Skybase 300 (MAP05) Main", player), lambda state:
       (state.has("Skybase 300 (MAP05)", player, 1) and
        state.has("Shotgun", player, 1)) and
       (state.has("Super Shotgun", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Skybase 300 (MAP05) Main -> Skybase 300 (MAP05) Blue", player), lambda state:
        state.has("Skybase 300 (MAP05) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Skybase 300 (MAP05) Blue -> Skybase 300 (MAP05) Yellow", player), lambda state:
        state.has("Skybase 300 (MAP05) - Yellow keycard", player, 1))
    set_rule(multiworld.get_entrance("Skybase 300 (MAP05) Yellow -> Skybase 300 (MAP05) Blue", player), lambda state:
        state.has("Skybase 300 (MAP05) - Yellow keycard", player, 1))

    # Whispering Corridor (MAP06)
    set_rule(multiworld.get_entrance("Hub -> Whispering Corridor (MAP06) Main", player), lambda state:
       (state.has("Whispering Corridor (MAP06)", player, 1) and
        state.has("Super Shotgun", player, 1)) and
       (state.has("Shotgun", player, 1) or
        state.has("Chaingun", player, 1) or
        state.has("Plasma gun", player, 1)))
    set_rule(multiworld.get_entrance("Whispering Corridor (MAP06) Main -> Whispering Corridor (MAP06) Blue", player), lambda state:
        state.has("Whispering Corridor (MAP06) - Blue skull key", player, 1))

    # Heavyweight (MAP07)
    set_rule(multiworld.get_entrance("Hub -> Heavyweight (MAP07) Main", player), lambda state:
        state.has("Heavyweight (MAP07)", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Plasma gun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1))

    # Waste Disposal Plant (MAP08)
    set_rule(multiworld.get_entrance("Hub -> Waste Disposal Plant (MAP08) Main", player), lambda state:
       (state.has("Waste Disposal Plant (MAP08)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Super Shotgun", player, 1)) and
       (state.has("Chaingun", player, 1) or
        state.has("Plasma gun", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Waste Disposal Plant (MAP08) Main -> Waste Disposal Plant (MAP08) Red", player), lambda state:
        state.has("Waste Disposal Plant (MAP08) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Waste Disposal Plant (MAP08) Red -> Waste Disposal Plant (MAP08) Blue", player), lambda state:
        state.has("Waste Disposal Plant (MAP08) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Waste Disposal Plant (MAP08) Red -> Waste Disposal Plant (MAP08) Main", player), lambda state:
        state.has("Waste Disposal Plant (MAP08) - Red keycard", player, 1))

    # Nuclear Power Station (MAP09)
    set_rule(multiworld.get_entrance("Hub -> Nuclear Power Station (MAP09) Main", player), lambda state:
        state.has("Nuclear Power Station (MAP09)", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Nuclear Power Station (MAP09) Main -> Nuclear Power Station (MAP09) Red", player), lambda state:
       (state.has("Nuclear Power Station (MAP09) - Red keycard", player, 1)) and       (state.has("Super Shotgun", player, 1) or
        state.has("Rocket launcher", player, 1)))
    set_rule(multiworld.get_entrance("Nuclear Power Station (MAP09) Main -> Nuclear Power Station (MAP09) Blue", player), lambda state:
        state.has("Nuclear Power Station (MAP09) - Blue keycard", player, 1) and
        state.has("Super Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Nuclear Power Station (MAP09) Main -> Nuclear Power Station (MAP09) Yellow", player), lambda state:
       (state.has("Nuclear Power Station (MAP09) - Yellow keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Super Shotgun", player, 1)))

    # Cargo Bay (MAP10)
    set_rule(multiworld.get_entrance("Hub -> Cargo Bay (MAP10) Main", player), lambda state:
       (state.has("Cargo Bay (MAP10)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Chainsaw", player, 1)) and
       (state.has("Chaingun", player, 1) or
        state.has("Super Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Cargo Bay (MAP10) Main -> Cargo Bay (MAP10) Red", player), lambda state:
       (state.has("Cargo Bay (MAP10) - Red keycard", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Plasma gun", player, 1) or
        state.has("BFG9000", player, 1)))


def set_episode2_rules(player, multiworld, pro):
    # Simbattle (MAP11)
    set_rule(multiworld.get_entrance("Hub -> Simbattle (MAP11) Start", player), lambda state:
        state.has("Simbattle (MAP11)", player, 1))
    set_rule(multiworld.get_entrance("Simbattle (MAP11) Start -> Simbattle (MAP11) Main", player), lambda state:
        state.has("Super Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Simbattle (MAP11) Main -> Simbattle (MAP11) Blue", player), lambda state:
        state.has("Simbattle (MAP11) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Simbattle (MAP11) Main -> Simbattle (MAP11) Red", player), lambda state:
        state.has("Simbattle (MAP11) - Red keycard", player, 1))
    set_rule(multiworld.get_entrance("Simbattle (MAP11) Main -> Simbattle (MAP11) Yellow", player), lambda state:
        state.has("Simbattle (MAP11) - Yellow keycard", player, 1))

    # Villa of Pain (MAP12)
    set_rule(multiworld.get_entrance("Hub -> Villa of Pain (MAP12) Main", player), lambda state:
        state.has("Villa of Pain (MAP12)", player, 1) and
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Villa of Pain (MAP12) Main -> Villa of Pain (MAP12) Yellow", player), lambda state:
       (state.has("Villa of Pain (MAP12) - Yellow skull key", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("Super Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Villa of Pain (MAP12) Yellow -> Villa of Pain (MAP12) Red", player), lambda state:
        state.has("Villa of Pain (MAP12) - Red skull key", player, 1))

    # Dark Crypt (MAP13)
    set_rule(multiworld.get_entrance("Hub -> Dark Crypt (MAP13) Main", player), lambda state:
       (state.has("Dark Crypt (MAP13)", player, 1)) and
       (state.has("Super Shotgun", player, 1) or
        state.has("Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Dark Crypt (MAP13) Main -> Dark Crypt (MAP13) Blue", player), lambda state:
        state.has("Dark Crypt (MAP13) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Dark Crypt (MAP13) Main -> Dark Crypt (MAP13) Yellow", player), lambda state:
       (state.has("Chaingun", player, 1) and
        state.has("Dark Crypt (MAP13) - Yellow keycard", player, 1)) and       (state.has("Plasma gun", player, 1) or
        state.has("Super Shotgun", player, 1) or
        state.has("Rocket launcher", player, 1)))

    # The Circle (MAP14)
    set_rule(multiworld.get_entrance("Hub -> The Circle (MAP14) Main", player), lambda state:
       (state.has("The Circle (MAP14)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1)) and
       (state.has("Chainsaw", player, 1) or
        state.has("Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("The Circle (MAP14) Main -> The Circle (MAP14) Red", player), lambda state:
        state.has("The Circle (MAP14) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("The Circle (MAP14) Main -> The Circle (MAP14) Yellow", player), lambda state:
        state.has("The Circle (MAP14) - Yellow skull key", player, 1))

    # Trouble Town (MAP15)
    set_rule(multiworld.get_entrance("Hub -> Trouble Town (MAP15) Start", player), lambda state:
        state.has("Trouble Town (MAP15)", player, 1))
    set_rule(multiworld.get_entrance("Trouble Town (MAP15) Start -> Trouble Town (MAP15) Main", player), lambda state:
        state.has("Shotgun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Trouble Town (MAP15) Main -> Trouble Town (MAP15) All Keys", player), lambda state:
       (state.has("Rocket launcher", player, 1) and
        state.has("Trouble Town (MAP15) - Blue keycard", player, 1) and
        state.has("Trouble Town (MAP15) - Yellow keycard", player, 1) and
        state.has("Trouble Town (MAP15) - Red keycard", player, 1)) and       (state.has("Plasma gun", player, 1) or
        state.has("BFG9000", player, 1)))

    # Bruiser Fortress (MAP16)
    set_rule(multiworld.get_entrance("Hub -> Bruiser Fortress (MAP16) Main", player), lambda state:
       (state.has("Bruiser Fortress (MAP16)", player, 1) and
        state.has("Super Shotgun", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("BFG9000", player, 1)))
    set_rule(multiworld.get_entrance("Bruiser Fortress (MAP16) Main -> Bruiser Fortress (MAP16) Yellow", player), lambda state:
        state.has("Bruiser Fortress (MAP16) - Yellow skull key", player, 1))

    # Constriction (MAP17)
    set_rule(multiworld.get_entrance("Hub -> Constriction (MAP17) Main", player), lambda state:
        state.has("Constriction (MAP17)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Rocket launcher", player, 1))
    set_rule(multiworld.get_entrance("Constriction (MAP17) Main -> Constriction (MAP17) Red", player), lambda state:
        state.has("Constriction (MAP17) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Constriction (MAP17) Main -> Constriction (MAP17) Blue", player), lambda state:
        state.has("Constriction (MAP17) - Blue skull key", player, 1))

    # Zombie Hideout (MAP18)
    set_rule(multiworld.get_entrance("Hub -> Zombie Hideout (MAP18) Main", player), lambda state:
       (state.has("Zombie Hideout (MAP18)", player, 1) and
        state.has("Shotgun", player, 1)) and
       (state.has("Super Shotgun", player, 1) or
        state.has("Chaingun", player, 1)))
    set_rule(multiworld.get_entrance("Zombie Hideout (MAP18) Main -> Zombie Hideout (MAP18) Blue", player), lambda state:
       (state.has("Chainsaw", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Zombie Hideout (MAP18) - Blue skull key", player, 1)) and       (state.has("Rocket launcher", player, 1) or
        state.has("BFG9000", player, 1) or
        state.has("Plasma gun", player, 1)))
    set_rule(multiworld.get_entrance("Zombie Hideout (MAP18) Main -> Zombie Hideout (MAP18) Yellow", player), lambda state:
        state.has("Rocket launcher", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Zombie Hideout (MAP18) - Yellow skull key", player, 1))

    # The Invasion (MAP19)
    set_rule(multiworld.get_entrance("Hub -> The Invasion (MAP19) Main", player), lambda state:
       (state.has("The Invasion (MAP19)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("Plasma gun", player, 1) or
        state.has("BFG9000", player, 1)))
    set_rule(multiworld.get_entrance("The Invasion (MAP19) Main -> The Invasion (MAP19) Yellow", player), lambda state:
        state.has("The Invasion (MAP19) - Yellow skull key", player, 1))
    set_rule(multiworld.get_entrance("The Invasion (MAP19) Main -> The Invasion (MAP19) Red", player), lambda state:
        state.has("The Invasion (MAP19) - Red skull key", player, 1))

    # Death Row (MAP20)
    set_rule(multiworld.get_entrance("Hub -> Death Row (MAP20) Main", player), lambda state:
        state.has("Death Row (MAP20)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Death Row (MAP20) Main -> Death Row (MAP20) Blue", player), lambda state:
        state.has("Rocket launcher", player, 1) and
        state.has("Death Row (MAP20) - Blue keycard", player, 1))
    set_rule(multiworld.get_entrance("Death Row (MAP20) Main -> Death Row (MAP20) Red", player), lambda state:
        state.has("Plasma gun", player, 1) and
        state.has("BFG9000", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Death Row (MAP20) - Red keycard", player, 1))


def set_episode3_rules(player, multiworld, pro):
    # Blood Lust (MAP21)
    set_rule(multiworld.get_entrance("Hub -> Blood Lust (MAP21) Start", player), lambda state:
        state.has("Blood Lust (MAP21)", player, 1))
    set_rule(multiworld.get_entrance("Blood Lust (MAP21) Start -> Blood Lust (MAP21) Main", player), lambda state:
        state.has("Super Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Blood Lust (MAP21) Start -> Blood Lust (MAP21) Red", player), lambda state:
        state.has("Blood Lust (MAP21) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Blood Lust (MAP21) Red -> Blood Lust (MAP21) Red Exit", player), lambda state:
       (state.has("Super Shotgun", player, 1)) and       (state.has("Plasma gun", player, 1) or
        state.has("BFG9000", player, 1) or
        state.has("Rocket launcher", player, 1)))

    # Firestorm Tomb (MAP22)
    set_rule(multiworld.get_entrance("Hub -> Firestorm Tomb (MAP22) Main", player), lambda state:
       (state.has("Firestorm Tomb (MAP22)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Rocket launcher", player, 1)) and
       (state.has("Chaingun", player, 1) or
        state.has("Shotgun", player, 1)))
    set_rule(multiworld.get_entrance("Firestorm Tomb (MAP22) Main -> Firestorm Tomb (MAP22) Red", player), lambda state:
        state.has("Firestorm Tomb (MAP22) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Firestorm Tomb (MAP22) Main -> Firestorm Tomb (MAP22) Yellow", player), lambda state:
        state.has("Firestorm Tomb (MAP22) - Yellow skull key", player, 1))

    # Dungeon of Inferno (MAP23)
    set_rule(multiworld.get_entrance("Hub -> Dungeon of Inferno (MAP23) Main", player), lambda state:
        state.has("Dungeon of Inferno (MAP23)", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Dungeon of Inferno (MAP23) Main -> Dungeon of Inferno (MAP23) Red", player), lambda state:
        state.has("Dungeon of Inferno (MAP23) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Dungeon of Inferno (MAP23) Main -> Dungeon of Inferno (MAP23) Blue", player), lambda state:
       (state.has("Dungeon of Inferno (MAP23) - Blue skull key", player, 1)) and       (state.has("BFG9000", player, 1) or
        state.has("Plasma gun", player, 1)))

    # Cavern of the Evil Spirit (MAP24)
    set_rule(multiworld.get_entrance("Hub -> Cavern of the Evil Spirit (MAP24) Main", player), lambda state:
       (state.has("Cavern of the Evil Spirit (MAP24)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1)) and
       (state.has("Rocket launcher", player, 1) or
        state.has("BFG9000", player, 1) or
        state.has("Plasma gun", player, 1)))
    set_rule(multiworld.get_entrance("Cavern of the Evil Spirit (MAP24) Main -> Cavern of the Evil Spirit (MAP24) Blue", player), lambda state:
        state.has("Cavern of the Evil Spirit (MAP24) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Cavern of the Evil Spirit (MAP24) Blue -> Cavern of the Evil Spirit (MAP24) Red", player), lambda state:
        state.has("Cavern of the Evil Spirit (MAP24) - Red skull key", player, 1))

    # Hellucination (MAP25)
    set_rule(multiworld.get_entrance("Hub -> Hellucination (MAP25) Main", player), lambda state:
        state.has("Hellucination (MAP25)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Plasma gun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Hellucination (MAP25) Main -> Hellucination (MAP25) Yellow", player), lambda state:
        state.has("Hellucination (MAP25) - Yellow skull key", player, 1) and
        state.has("BFG9000", player, 1))
    set_rule(multiworld.get_entrance("Hellucination (MAP25) Main -> Hellucination (MAP25) Red", player), lambda state:
        state.has("Hellucination (MAP25) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Hellucination (MAP25) Main -> Hellucination (MAP25) Blue", player), lambda state:
        state.has("Hellucination (MAP25) - Blue skull key", player, 1))

    # Valley of Brimstone (MAP26)
    set_rule(multiworld.get_entrance("Hub -> Valley of Brimstone (MAP26) Main", player), lambda state:
       (state.has("Valley of Brimstone (MAP26)", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Super Shotgun", player, 1)) and
       (state.has("BFG9000", player, 1) or
        state.has("Plasma gun", player, 1)))
    set_rule(multiworld.get_entrance("Valley of Brimstone (MAP26) Main -> Valley of Brimstone (MAP26) Yellow", player), lambda state:
        state.has("Valley of Brimstone (MAP26) - Yellow skull key", player, 1))

    # Dissect (MAP27)
    set_rule(multiworld.get_entrance("Hub -> Dissect (MAP27) Start", player), lambda state:
        state.has("Dissect (MAP27)", player, 1))
    set_rule(multiworld.get_entrance("Dissect (MAP27) Start -> Dissect (MAP27) Main", player), lambda state:
       (state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Rocket launcher", player, 1)) and       (state.has("BFG9000", player, 1) or
        state.has("Plasma gun", player, 1)))
    set_rule(multiworld.get_entrance("Dissect (MAP27) Main -> Dissect (MAP27) Red", player), lambda state:
        state.has("Dissect (MAP27) - Red skull key", player, 1) and
        state.has("BFG9000", player, 1))

    # Unholy Demise (MAP28)
    set_rule(multiworld.get_entrance("Hub -> Unholy Demise (MAP28) Main", player), lambda state:
        state.has("Unholy Demise (MAP28)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Plasma gun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("BFG9000", player, 1) and
        state.has("Super Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Unholy Demise (MAP28) Main -> Unholy Demise (MAP28) Yellow", player), lambda state:
        state.has("Unholy Demise (MAP28) - Yellow skull key", player, 1))
    set_rule(multiworld.get_entrance("Unholy Demise (MAP28) Main -> Unholy Demise (MAP28) Red", player), lambda state:
        state.has("Unholy Demise (MAP28) - Red skull key", player, 1))

    # Den of Torture (MAP29)
    set_rule(multiworld.get_entrance("Hub -> Den of Torture (MAP29) Main", player), lambda state:
        state.has("Den of Torture (MAP29)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Plasma gun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("BFG9000", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Den of Torture (MAP29) Main -> Den of Torture (MAP29) Blue", player), lambda state:
        state.has("Den of Torture (MAP29) - Blue skull key", player, 1))

    # Eternal Core (MAP30)
    set_rule(multiworld.get_entrance("Hub -> Eternal Core (MAP30) Safe Area", player), lambda state:
        state.has("Eternal Core (MAP30)", player, 1))
    set_rule(multiworld.get_entrance("Eternal Core (MAP30) Safe Area -> Eternal Core (MAP30) Main", player), lambda state:
        state.has("Super Shotgun", player, 1) and
        state.has("BFG9000", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Chainsaw", player, 1) and
        state.has("Plasma gun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Shotgun", player, 1))


def set_episode4_rules(player, multiworld, pro):
    # Creepy (MAP31)
    set_rule(multiworld.get_entrance("Hub -> Creepy (MAP31) Main", player), lambda state:
       (state.has("Creepy (MAP31)", player, 1) and
        state.has("Shotgun", player, 1)) and
       (state.has("Super Shotgun", player, 1) or
        state.has("Plasma gun", player, 1) or
        state.has("Rocket launcher", player, 1) or
        state.has("BFG9000", player, 1)))
    set_rule(multiworld.get_entrance("Creepy (MAP31) Main -> Creepy (MAP31) All Keys", player), lambda state:
        state.has("Creepy (MAP31) - Blue keycard", player, 1) and
        state.has("Creepy (MAP31) - Yellow keycard", player, 1) and
        state.has("Creepy (MAP31) - Red keycard", player, 1))

    # Condemnation (MAP32)
    set_rule(multiworld.get_entrance("Hub -> Condemnation (MAP32) Main", player), lambda state:
        state.has("Condemnation (MAP32)", player, 1) and
        state.has("Shotgun", player, 1) and
        state.has("Super Shotgun", player, 1) and
        state.has("Chaingun", player, 1) and
        state.has("Rocket launcher", player, 1) and
        state.has("Chainsaw", player, 1))
    set_rule(multiworld.get_entrance("Condemnation (MAP32) Main -> Condemnation (MAP32) Blue", player), lambda state:
        state.has("Condemnation (MAP32) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Condemnation (MAP32) Blue -> Condemnation (MAP32) Red", player), lambda state:
        state.has("Condemnation (MAP32) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Condemnation (MAP32) Red -> Condemnation (MAP32) Yellow", player), lambda state:
        state.has("BFG9000", player, 1) and
        state.has("Condemnation (MAP32) - Yellow skull key", player, 1))

    # Zerstorung (MAP33)
    set_rule(multiworld.get_entrance("Hub -> Zerstorung (MAP33) Start", player), lambda state:
        state.has("Zerstorung (MAP33)", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) Start -> Zerstorung (MAP33) Main", player), lambda state:
        state.has("Super Shotgun", player, 1) or
        state.has("Shotgun", player, 1) or
        state.has("Chaingun", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) Main -> Zerstorung (MAP33) Blue", player), lambda state:
        state.has("Zerstorung (MAP33) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) Blue -> Zerstorung (MAP33) Main", player), lambda state:
        state.has("Zerstorung (MAP33) - Blue skull key", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) Blue -> Zerstorung (MAP33) Bosses", player), lambda state:
        state.has("BFG9000", player, 1) and
        state.has("Super Shotgun", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) Bosses -> Zerstorung (MAP33) All Keys", player), lambda state:
        state.has("Zerstorung (MAP33) - Yellow skull key", player, 1) and
        state.has("Zerstorung (MAP33) - Red skull key", player, 1))
    set_rule(multiworld.get_entrance("Zerstorung (MAP33) All Keys -> Zerstorung (MAP33) Bosses", player), lambda state:
        state.has("Zerstorung (MAP33) - Yellow skull key", player, 1) and
        state.has("Zerstorung (MAP33) - Red skull key", player, 1))


def set_rules(pwad_zone300_world: "DOOM2Zone300World", included_episodes, pro):
    player = pwad_zone300_world.player
    multiworld = pwad_zone300_world.multiworld

    if included_episodes[0]:
        set_episode1_rules(player, multiworld, pro)
    if included_episodes[1]:
        set_episode2_rules(player, multiworld, pro)
    if included_episodes[2]:
        set_episode3_rules(player, multiworld, pro)
    if included_episodes[3]:
        set_episode4_rules(player, multiworld, pro)
