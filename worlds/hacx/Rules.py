# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import HacXWorld


def set_episode1_rules(player, multiworld, pro):
    # GenEmp Corp. (MAP01)
    set_rule(multiworld.get_entrance("Hub -> GenEmp Corp. (MAP01) Main", player), lambda state:
        state.has("GenEmp Corp. (MAP01)", player, 1))
    set_rule(multiworld.get_entrance("GenEmp Corp. (MAP01) Main -> GenEmp Corp. (MAP01) Keycard", player), lambda state:
        state.has("GenEmp Corp. (MAP01) - Keycard", player, 1))
    set_rule(multiworld.get_entrance("GenEmp Corp. (MAP01) Keycard -> GenEmp Corp. (MAP01) Password", player), lambda state:
       (state.has("GenEmp Corp. (MAP01) - Password", player, 1)) and       (state.has("Cryogun", player, 1) or
        state.has("Tazer", player, 1)))

    # Tunnel Town (MAP02)
    set_rule(multiworld.get_entrance("Hub -> Tunnel Town (MAP02) Main", player), lambda state:
        state.has("Tunnel Town (MAP02)", player, 1))
    set_rule(multiworld.get_entrance("Tunnel Town (MAP02) Main -> Tunnel Town (MAP02) Keycard", player), lambda state:
       (state.has("Tunnel Town (MAP02) - Keycard", player, 1)) and       (state.has("Tazer", player, 1) or
        state.has("Photon 'zooka", player, 1) or
        state.has("Cryogun", player, 1) or
        state.has("HOIG Reznator", player, 1)))
    set_rule(multiworld.get_entrance("Tunnel Town (MAP02) Keycard -> Tunnel Town (MAP02) Password", player), lambda state:
        state.has("Tunnel Town (MAP02) - Password", player, 1))

    # Lava Annex (MAP03)
    set_rule(multiworld.get_entrance("Hub -> Lava Annex (MAP03) Opening", player), lambda state:
        state.has("Lava Annex (MAP03)", player, 1))
    set_rule(multiworld.get_entrance("Lava Annex (MAP03) Opening -> Lava Annex (MAP03) Main", player), lambda state:
        state.has("Tazer", player, 1) or
        state.has("HOIG Reznator", player, 1) or
        state.has("Cryogun", player, 1))
    set_rule(multiworld.get_entrance("Lava Annex (MAP03) Main -> Lava Annex (MAP03) Keycard", player), lambda state:
       (state.has("Lava Annex (MAP03) - Keycard", player, 1)) and       (state.has("Tazer", player, 1) or
        state.has("Cryogun", player, 1)))
    set_rule(multiworld.get_entrance("Lava Annex (MAP03) Keycard -> Lava Annex (MAP03) Password", player), lambda state:
        state.has("Lava Annex (MAP03) - Password", player, 1) and
        state.has("Photon 'zooka", player, 1))

    # Alcatraz (MAP04)
    set_rule(multiworld.get_entrance("Hub -> Alcatraz (MAP04) Main", player), lambda state:
       (state.has("Alcatraz (MAP04)", player, 1) and
        state.has("HOIG Reznator", player, 1) and
        state.has("Tazer", player, 1)) and
       (state.has("Photon 'zooka", player, 1) or
        state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1)))

    # Cyber Circus (MAP05)
    set_rule(multiworld.get_entrance("Hub -> Cyber Circus (MAP05) Main", player), lambda state:
       (state.has("Cyber Circus (MAP05)", player, 1) and
        state.has("Tazer", player, 1)) and
       (state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1)))
    set_rule(multiworld.get_entrance("Cyber Circus (MAP05) Main -> Cyber Circus (MAP05) Sigma", player), lambda state:
        state.has("Cyber Circus (MAP05) - C-key", player, 1))

    # Digi-Ota (MAP06)
    set_rule(multiworld.get_entrance("Hub -> Digi-Ota (MAP06) Main", player), lambda state:
       (state.has("Digi-Ota (MAP06)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("HOIG Reznator", player, 1)) and
       (state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1)))
    set_rule(multiworld.get_entrance("Digi-Ota (MAP06) Main -> Digi-Ota (MAP06) Password", player), lambda state:
        state.has("Digi-Ota (MAP06) - Password", player, 1))
    set_rule(multiworld.get_entrance("Digi-Ota (MAP06) Password -> Digi-Ota (MAP06) Keycard", player), lambda state:
        state.has("Digi-Ota (MAP06) - Keycard", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("Photon 'zooka", player, 1))


def set_episode2_rules(player, multiworld, pro):
    # The Great Wall (MAP07)
    set_rule(multiworld.get_entrance("Hub -> The Great Wall (MAP07) Opening", player), lambda state:
        state.has("The Great Wall (MAP07)", player, 1))
    set_rule(multiworld.get_entrance("The Great Wall (MAP07) Opening -> The Great Wall (MAP07) Main", player), lambda state:
        state.has("Tazer", player, 1))
    set_rule(multiworld.get_entrance("The Great Wall (MAP07) Main -> The Great Wall (MAP07) Password", player), lambda state:
       (state.has("The Great Wall (MAP07) - Password", player, 1)) and       (state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1)))

    # Garden of Delight (MAP08)
    set_rule(multiworld.get_entrance("Hub -> Garden of Delight (MAP08) Main", player), lambda state:
        state.has("Garden of Delight (MAP08)", player, 1) and
        state.has("HOIG Reznator", player, 1))
    set_rule(multiworld.get_entrance("Garden of Delight (MAP08) Main -> Garden of Delight (MAP08) Garden", player), lambda state:
        state.has("Tazer", player, 1) or
        state.has("Photon 'zooka", player, 1) or
        state.has("Cryogun", player, 1))

    # Hidden Fortress (MAP09)
    set_rule(multiworld.get_entrance("Hub -> Hidden Fortress (MAP09) Main", player), lambda state:
       (state.has("Hidden Fortress (MAP09)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Cryogun", player, 1) and
        state.has("Uzi", player, 1)) and
       (state.has("Stick", player, 1) or
        state.has("Photon 'zooka", player, 1)))
    set_rule(multiworld.get_entrance("Hidden Fortress (MAP09) Fortress -> Hidden Fortress (MAP09) Z-Blue", player), lambda state:
        state.has("Hidden Fortress (MAP09) - Blue Z-key", player, 1))

    # Anarchist Dream (MAP10)
    set_rule(multiworld.get_entrance("Hub -> Anarchist Dream (MAP10) Main", player), lambda state:
       (state.has("Anarchist Dream (MAP10)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("Cryogun", player, 1) and
        state.has("Photon 'zooka", player, 1) and
        state.has("HOIG Reznator", player, 1)) and
       (state.has("Stick", player, 1) or
        state.has("Nuker", player, 1)))

    # Notus Us! (MAP11)
    set_rule(multiworld.get_entrance("Hub -> Notus Us! (MAP11) Main", player), lambda state:
       (state.has("Notus Us! (MAP11)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("Cryogun", player, 1)) and
       (state.has("Photon 'zooka", player, 1) or
        state.has("Stick", player, 1) or
        state.has("Nuker", player, 1)))
    set_rule(multiworld.get_entrance("Notus Us! (MAP11) Main -> Notus Us! (MAP11) Password", player), lambda state:
        state.has("Notus Us! (MAP11) - Password", player, 1))
    set_rule(multiworld.get_entrance("Notus Us! (MAP11) Password -> Notus Us! (MAP11) Keycard", player), lambda state:
        state.has("Notus Us! (MAP11) - Keycard", player, 1))


def set_episode3_rules(player, multiworld, pro):
    # Gothik Gauntlet (MAP12)
    set_rule(multiworld.get_entrance("Hub -> Gothik Gauntlet (MAP12) Start", player), lambda state:
        state.has("Gothik Gauntlet (MAP12)", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Start -> Gothik Gauntlet (MAP12) Main", player), lambda state:
        state.has("Tazer", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Main -> Gothik Gauntlet (MAP12) West City", player), lambda state:
        state.has("Photon 'zooka", player, 1) and
        state.has("Uzi", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Main -> Gothik Gauntlet (MAP12) Password", player), lambda state:
        state.has("Gothik Gauntlet (MAP12) - Password", player, 1) and
        state.has("Uzi", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Main -> Gothik Gauntlet (MAP12) Keycard", player), lambda state:
        state.has("Gothik Gauntlet (MAP12) - Keycard", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Lift Jump -> Gothik Gauntlet (MAP12) Password", player), lambda state:
        state.has("Uzi", player, 1))
    set_rule(multiworld.get_entrance("Gothik Gauntlet (MAP12) Keycard -> Gothik Gauntlet (MAP12) Main", player), lambda state:
        state.has("Gothik Gauntlet (MAP12) - Keycard", player, 1))

    # The Sewers (MAP13)
    set_rule(multiworld.get_entrance("Hub -> The Sewers (MAP13) Main", player), lambda state:
       (state.has("The Sewers (MAP13)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Photon 'zooka", player, 1) and
        state.has("HOIG Reznator", player, 1) and
        state.has("Uzi", player, 1)) and
       (state.has("Cryogun", player, 1) or
        state.has("Stick", player, 1)))
    set_rule(multiworld.get_entrance("The Sewers (MAP13) Main -> The Sewers (MAP13) Z Blue", player), lambda state:
        state.has("The Sewers (MAP13) - Blue Z-key", player, 1))
    set_rule(multiworld.get_entrance("The Sewers (MAP13) Z Blue -> The Sewers (MAP13) Z Red", player), lambda state:
        state.has("The Sewers (MAP13) - Red Z-key", player, 1))

    # 'Trode Wars (MAP14)
    set_rule(multiworld.get_entrance("Hub -> 'Trode Wars (MAP14) Main", player), lambda state:
       (state.has("'Trode Wars (MAP14)", player, 1) and
        state.has("Uzi", player, 1)) and
       (state.has("Tazer", player, 1) or
        state.has("Cryogun", player, 1)))
    set_rule(multiworld.get_entrance("'Trode Wars (MAP14) Main -> 'Trode Wars (MAP14) Sigma", player), lambda state:
        state.has("'Trode Wars (MAP14) - C-key", player, 1) and
        state.has("Photon 'zooka", player, 1))

    # Twilight of EnKs (MAP15)
    set_rule(multiworld.get_entrance("Hub -> Twilight of EnKs (MAP15) Main", player), lambda state:
       (state.has("Twilight of EnKs (MAP15)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Cryogun", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("HOIG Reznator", player, 1)) and
       (state.has("Stick", player, 1) or
        state.has("Nuker", player, 1) or
        state.has("Photon 'zooka", player, 1)))
    set_rule(multiworld.get_entrance("Twilight of EnKs (MAP15) Main -> Twilight of EnKs (MAP15) Z Blue", player), lambda state:
        state.has("Twilight of EnKs (MAP15) - Blue Z-key", player, 1))
    set_rule(multiworld.get_entrance("Twilight of EnKs (MAP15) Main -> Twilight of EnKs (MAP15) Z Orange", player), lambda state:
        state.has("Twilight of EnKs (MAP15) - Yellow Z-key", player, 1) and
        state.has("Twilight of EnKs (MAP15) - Red Z-key", player, 1))


def set_episode4_rules(player, multiworld, pro):
    # Desiccant Room (MAP31)
    set_rule(multiworld.get_entrance("Hub -> Desiccant Room (MAP31) Main", player), lambda state:
        state.has("Desiccant Room (MAP31)", player, 1))
    set_rule(multiworld.get_entrance("Desiccant Room (MAP31) Main -> Desiccant Room (MAP31) Keycard", player), lambda state:
        state.has("Desiccant Room (MAP31) - Keycard", player, 1))
    set_rule(multiworld.get_entrance("Desiccant Room (MAP31) Keycard -> Desiccant Room (MAP31) Outer", player), lambda state:
        state.has("Tazer", player, 1) or
        state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1))

    # Protean Cybex (MAP16)
    set_rule(multiworld.get_entrance("Hub -> Protean Cybex (MAP16) From Hub", player), lambda state:
        state.has("Protean Cybex (MAP16)", player, 1))
    set_rule(multiworld.get_entrance("Protean Cybex (MAP16) From Hub -> Protean Cybex (MAP16) Main", player), lambda state:
       (state.has("Tazer", player, 1)) and       (state.has("Stick", player, 1) or
        state.has("Nuker", player, 1) or
        state.has("Cryogun", player, 1) or
        state.has("Uzi", player, 1)))

    # River of Blood (MAP17)
    set_rule(multiworld.get_entrance("Hub -> River of Blood (MAP17) Entry", player), lambda state:
        state.has("River of Blood (MAP17)", player, 1))
    set_rule(multiworld.get_entrance("River of Blood (MAP17) Entry -> River of Blood (MAP17) Main", player), lambda state:
       (state.has("Uzi", player, 1) and
        state.has("Tazer", player, 1)) and       (state.has("Stick", player, 1) or
        state.has("Photon 'zooka", player, 1) or
        state.has("Cryogun", player, 1)))

    # Bizarro (MAP18)
    set_rule(multiworld.get_entrance("Hub -> Bizarro (MAP18) Opening", player), lambda state:
       (state.has("Bizarro (MAP18)", player, 1) and
        state.has("Tazer", player, 1)) and
       (state.has("Uzi", player, 1) or
        state.has("Cryogun", player, 1)))
    set_rule(multiworld.get_entrance("Bizarro (MAP18) Opening -> Bizarro (MAP18) All", player), lambda state:
       (state.has("Photon 'zooka", player, 1)) and       (state.has("Stick", player, 1) or
        state.has("Nuker", player, 1)))

    # The War Rooms (MAP19)
    set_rule(multiworld.get_entrance("Hub -> The War Rooms (MAP19) Main", player), lambda state:
       (state.has("The War Rooms (MAP19)", player, 1) and
        state.has("HOIG Reznator", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("Cryogun", player, 1) and
        state.has("Photon 'zooka", player, 1) and
        state.has("Tazer", player, 1)) and
       (state.has("Nuker", player, 1) or
        state.has("Stick", player, 1)))

    # Intruder Alert! (MAP20)
    set_rule(multiworld.get_entrance("Hub -> Intruder Alert! (MAP20) Main", player), lambda state:
        state.has("Intruder Alert! (MAP20)", player, 1) and
        state.has("Tazer", player, 1) and
        state.has("Photon 'zooka", player, 1) and
        state.has("Stick", player, 1) and
        state.has("HOIG Reznator", player, 1) and
        state.has("Uzi", player, 1) and
        state.has("Nuker", player, 1) and
        state.has("Cryogun", player, 1))
    set_rule(multiworld.get_entrance("Intruder Alert! (MAP20) Main -> Intruder Alert! (MAP20) Sigma", player), lambda state:
        state.has("Intruder Alert! (MAP20) - C-key", player, 1))


def set_rules(hacx_world: "HacXWorld", included_episodes, pro):
    player = hacx_world.player
    multiworld = hacx_world.multiworld

    if included_episodes[0]:
        set_episode1_rules(player, multiworld, pro)
    if included_episodes[1]:
        set_episode2_rules(player, multiworld, pro)
    if included_episodes[2]:
        set_episode3_rules(player, multiworld, pro)
    if included_episodes[3]:
        set_episode4_rules(player, multiworld, pro)
