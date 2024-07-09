# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from BaseClasses import ItemClassification
from typing import TypedDict, Dict, Set 


class ItemDict(TypedDict, total=False): 
    classification: ItemClassification 
    count: int 
    name: str 
    doom_type: int # Unique numerical id used to spawn the item. -1 is level item, -2 is level complete item. 
    episode: int # Relevant if that item targets a specific level, like keycard or map reveal pickup. 
    map: int 


item_table: Dict[int, ItemDict] = {
    364000: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tazer',
             'doom_type': 2001,
             'episode': -1,
             'map': -1},
    364001: {'classification': ItemClassification.progression,
             'count': 1,
             'name': "Photon 'zooka",
             'doom_type': 2003,
             'episode': -1,
             'map': -1},
    364002: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Stick',
             'doom_type': 2004,
             'episode': -1,
             'map': -1},
    364003: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'HOIG Reznator',
             'doom_type': 2005,
             'episode': -1,
             'map': -1},
    364004: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Uzi',
             'doom_type': 2002,
             'episode': -1,
             'map': -1},
    364005: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Nuker',
             'doom_type': 2006,
             'episode': -1,
             'map': -1},
    364006: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Cryogun',
             'doom_type': 82,
             'episode': -1,
             'map': -1},
    364007: {'classification': ItemClassification.useful,
             'count': 0,
             'name': 'Valise',
             'doom_type': 8,
             'episode': -1,
             'map': -1},
    364008: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Kevlar vest',
             'doom_type': 2018,
             'episode': -1,
             'map': -1},
    364009: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Super kevlar vest',
             'doom_type': 2019,
             'episode': -1,
             'map': -1},
    364010: {'classification': ItemClassification.filler,
             'count': 0,
             'name': '007Microtel',
             'doom_type': 2023,
             'episode': -1,
             'map': -1},
    364011: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Force field',
             'doom_type': 2022,
             'episode': -1,
             'map': -1},
    364012: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'EnK blinder',
             'doom_type': 2024,
             'episode': -1,
             'map': -1},
    364013: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Centrophenoxine',
             'doom_type': 2013,
             'episode': -1,
             'map': -1},
    364014: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Body armor',
             'doom_type': 83,
             'episode': -1,
             'map': -1},
    364015: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Hypo',
             'doom_type': 2012,
             'episode': -1,
             'map': -1},
    364016: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Case of rounds',
             'doom_type': 2048,
             'episode': -1,
             'map': -1},
    364017: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Case of torpedoes',
             'doom_type': 2046,
             'episode': -1,
             'map': -1},
    364018: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Case of cartridges',
             'doom_type': 2049,
             'episode': -1,
             'map': -1},
    364019: {'classification': ItemClassification.filler,
             'count': 0,
             'name': 'Molecule tank',
             'doom_type': 17,
             'episode': -1,
             'map': -1},
    364200: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'GenEmp Corp. (MAP01) - Keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 1},
    364201: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'GenEmp Corp. (MAP01) - Password',
             'doom_type': 13,
             'episode': 1,
             'map': 1},
    364202: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tunnel Town (MAP02) - Keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 2},
    364203: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tunnel Town (MAP02) - Password',
             'doom_type': 13,
             'episode': 1,
             'map': 2},
    364204: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Lava Annex (MAP03) - Keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 3},
    364205: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Lava Annex (MAP03) - Password',
             'doom_type': 13,
             'episode': 1,
             'map': 3},
    364206: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Cyber Circus (MAP05) - C-key',
             'doom_type': 6,
             'episode': 1,
             'map': 5},
    364207: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Digi-Ota (MAP06) - Password',
             'doom_type': 13,
             'episode': 1,
             'map': 6},
    364208: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Digi-Ota (MAP06) - Keycard',
             'doom_type': 5,
             'episode': 1,
             'map': 6},
    364209: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Great Wall (MAP07) - Password',
             'doom_type': 13,
             'episode': 2,
             'map': 1},
    364210: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hidden Fortress (MAP09) - Blue Z-key',
             'doom_type': 40,
             'episode': 2,
             'map': 3},
    364211: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Notus Us! (MAP11) - Password',
             'doom_type': 13,
             'episode': 2,
             'map': 5},
    364212: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Notus Us! (MAP11) - Keycard',
             'doom_type': 5,
             'episode': 2,
             'map': 5},
    364213: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gothik Gauntlet (MAP12) - Keycard',
             'doom_type': 5,
             'episode': 3,
             'map': 1},
    364214: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gothik Gauntlet (MAP12) - Password',
             'doom_type': 13,
             'episode': 3,
             'map': 1},
    364215: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewers (MAP13) - Blue Z-key',
             'doom_type': 40,
             'episode': 3,
             'map': 2},
    364216: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewers (MAP13) - Red Z-key',
             'doom_type': 38,
             'episode': 3,
             'map': 2},
    364217: {'classification': ItemClassification.progression,
             'count': 1,
             'name': "'Trode Wars (MAP14) - C-key",
             'doom_type': 6,
             'episode': 3,
             'map': 3},
    364218: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15) - Red Z-key',
             'doom_type': 38,
             'episode': 3,
             'map': 4},
    364219: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15) - Blue Z-key',
             'doom_type': 40,
             'episode': 3,
             'map': 4},
    364220: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15) - Yellow Z-key',
             'doom_type': 39,
             'episode': 3,
             'map': 4},
    364221: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Desiccant Room (MAP31) - Keycard',
             'doom_type': 5,
             'episode': 4,
             'map': 1},
    364222: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Bizarro (MAP18) - Blue Z-key',
             'doom_type': 40,
             'episode': 4,
             'map': 4},
    364223: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Intruder Alert! (MAP20) - C-key',
             'doom_type': 6,
             'episode': 4,
             'map': 6},
    364400: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'GenEmp Corp. (MAP01)',
             'doom_type': -1,
             'episode': 1,
             'map': 1},
    364401: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'GenEmp Corp. (MAP01) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 1},
    364402: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'GenEmp Corp. (MAP01) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 1},
    364403: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tunnel Town (MAP02)',
             'doom_type': -1,
             'episode': 1,
             'map': 2},
    364404: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Tunnel Town (MAP02) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 2},
    364405: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Tunnel Town (MAP02) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 2},
    364406: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Lava Annex (MAP03)',
             'doom_type': -1,
             'episode': 1,
             'map': 3},
    364407: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Lava Annex (MAP03) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 3},
    364408: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Lava Annex (MAP03) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 3},
    364409: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Alcatraz (MAP04)',
             'doom_type': -1,
             'episode': 1,
             'map': 4},
    364410: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Alcatraz (MAP04) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 4},
    364411: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Alcatraz (MAP04) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 4},
    364412: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Cyber Circus (MAP05)',
             'doom_type': -1,
             'episode': 1,
             'map': 5},
    364413: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Cyber Circus (MAP05) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 5},
    364414: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Cyber Circus (MAP05) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 5},
    364415: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Digi-Ota (MAP06)',
             'doom_type': -1,
             'episode': 1,
             'map': 6},
    364416: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Digi-Ota (MAP06) - Complete',
             'doom_type': -2,
             'episode': 1,
             'map': 6},
    364417: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Digi-Ota (MAP06) - SI array',
             'doom_type': 2026,
             'episode': 1,
             'map': 6},
    364418: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Great Wall (MAP07)',
             'doom_type': -1,
             'episode': 2,
             'map': 1},
    364419: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Great Wall (MAP07) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 1},
    364420: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'The Great Wall (MAP07) - SI array',
             'doom_type': 2026,
             'episode': 2,
             'map': 1},
    364421: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Garden of Delight (MAP08)',
             'doom_type': -1,
             'episode': 2,
             'map': 2},
    364422: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Garden of Delight (MAP08) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 2},
    364423: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Garden of Delight (MAP08) - SI array',
             'doom_type': 2026,
             'episode': 2,
             'map': 2},
    364424: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hidden Fortress (MAP09)',
             'doom_type': -1,
             'episode': 2,
             'map': 3},
    364425: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Hidden Fortress (MAP09) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 3},
    364426: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Hidden Fortress (MAP09) - SI array',
             'doom_type': 2026,
             'episode': 2,
             'map': 3},
    364427: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Anarchist Dream (MAP10)',
             'doom_type': -1,
             'episode': 2,
             'map': 4},
    364428: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Anarchist Dream (MAP10) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 4},
    364429: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Anarchist Dream (MAP10) - SI array',
             'doom_type': 2026,
             'episode': 2,
             'map': 4},
    364430: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Notus Us! (MAP11)',
             'doom_type': -1,
             'episode': 2,
             'map': 5},
    364431: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Notus Us! (MAP11) - Complete',
             'doom_type': -2,
             'episode': 2,
             'map': 5},
    364432: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Notus Us! (MAP11) - SI array',
             'doom_type': 2026,
             'episode': 2,
             'map': 5},
    364433: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gothik Gauntlet (MAP12)',
             'doom_type': -1,
             'episode': 3,
             'map': 1},
    364434: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Gothik Gauntlet (MAP12) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 1},
    364435: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Gothik Gauntlet (MAP12) - SI array',
             'doom_type': 2026,
             'episode': 3,
             'map': 1},
    364436: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewers (MAP13)',
             'doom_type': -1,
             'episode': 3,
             'map': 2},
    364437: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The Sewers (MAP13) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 2},
    364438: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'The Sewers (MAP13) - SI array',
             'doom_type': 2026,
             'episode': 3,
             'map': 2},
    364439: {'classification': ItemClassification.progression,
             'count': 1,
             'name': "'Trode Wars (MAP14)",
             'doom_type': -1,
             'episode': 3,
             'map': 3},
    364440: {'classification': ItemClassification.progression,
             'count': 1,
             'name': "'Trode Wars (MAP14) - Complete",
             'doom_type': -2,
             'episode': 3,
             'map': 3},
    364441: {'classification': ItemClassification.filler,
             'count': 1,
             'name': "'Trode Wars (MAP14) - SI array",
             'doom_type': 2026,
             'episode': 3,
             'map': 3},
    364442: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15)',
             'doom_type': -1,
             'episode': 3,
             'map': 4},
    364443: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15) - Complete',
             'doom_type': -2,
             'episode': 3,
             'map': 4},
    364444: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Twilight of EnKs (MAP15) - SI array',
             'doom_type': 2026,
             'episode': 3,
             'map': 4},
    364445: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Desiccant Room (MAP31)',
             'doom_type': -1,
             'episode': 4,
             'map': 1},
    364446: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Desiccant Room (MAP31) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 1},
    364447: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Desiccant Room (MAP31) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 1},
    364448: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Protean Cybex (MAP16)',
             'doom_type': -1,
             'episode': 4,
             'map': 2},
    364449: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Protean Cybex (MAP16) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 2},
    364450: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Protean Cybex (MAP16) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 2},
    364451: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'River of Blood (MAP17)',
             'doom_type': -1,
             'episode': 4,
             'map': 3},
    364452: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'River of Blood (MAP17) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 3},
    364453: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'River of Blood (MAP17) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 3},
    364454: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Bizarro (MAP18)',
             'doom_type': -1,
             'episode': 4,
             'map': 4},
    364455: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Bizarro (MAP18) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 4},
    364456: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Bizarro (MAP18) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 4},
    364457: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The War Rooms (MAP19)',
             'doom_type': -1,
             'episode': 4,
             'map': 5},
    364458: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'The War Rooms (MAP19) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 5},
    364459: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'The War Rooms (MAP19) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 5},
    364460: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Intruder Alert! (MAP20)',
             'doom_type': -1,
             'episode': 4,
             'map': 6},
    364461: {'classification': ItemClassification.progression,
             'count': 1,
             'name': 'Intruder Alert! (MAP20) - Complete',
             'doom_type': -2,
             'episode': 4,
             'map': 6},
    364462: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Intruder Alert! (MAP20) - SI array',
             'doom_type': 2026,
             'episode': 4,
             'map': 6},
    364600: {'classification': ItemClassification.useful,
             'count': 0,
             'name': 'Round capacity',
             'doom_type': 65001,
             'episode': -1,
             'map': -1},
    364601: {'classification': ItemClassification.useful,
             'count': 0,
             'name': 'Cartridge capacity',
             'doom_type': 65002,
             'episode': -1,
             'map': -1},
    364602: {'classification': ItemClassification.useful,
             'count': 0,
             'name': 'Molecule capacity',
             'doom_type': 65003,
             'episode': -1,
             'map': -1},
    364603: {'classification': ItemClassification.useful,
             'count': 0,
             'name': 'Torpedo capacity',
             'doom_type': 65004,
             'episode': -1,
             'map': -1},
}


item_name_groups: Dict[str, Set[str]] = {
    'Ammos': {'Case of cartridges', 'Case of rounds', 'Case of torpedoes', 'Molecule tank', },
    'Keys': {"'Trode Wars (MAP14) - C-key", 'Bizarro (MAP18) - Blue Z-key', 'Cyber Circus (MAP05) - C-key', 'Desiccant Room (MAP31) - Keycard', 'Digi-Ota (MAP06) - Keycard', 'Digi-Ota (MAP06) - Password', 'GenEmp Corp. (MAP01) - Keycard', 'GenEmp Corp. (MAP01) - Password', 'Gothik Gauntlet (MAP12) - Keycard', 'Gothik Gauntlet (MAP12) - Password', 'Hidden Fortress (MAP09) - Blue Z-key', 'Intruder Alert! (MAP20) - C-key', 'Lava Annex (MAP03) - Keycard', 'Lava Annex (MAP03) - Password', 'Notus Us! (MAP11) - Keycard', 'Notus Us! (MAP11) - Password', 'The Great Wall (MAP07) - Password', 'The Sewers (MAP13) - Blue Z-key', 'The Sewers (MAP13) - Red Z-key', 'Tunnel Town (MAP02) - Keycard', 'Tunnel Town (MAP02) - Password', 'Twilight of EnKs (MAP15) - Blue Z-key', 'Twilight of EnKs (MAP15) - Red Z-key', 'Twilight of EnKs (MAP15) - Yellow Z-key', },
    'Levels': {"'Trode Wars (MAP14)", 'Alcatraz (MAP04)', 'Anarchist Dream (MAP10)', 'Bizarro (MAP18)', 'Cyber Circus (MAP05)', 'Desiccant Room (MAP31)', 'Digi-Ota (MAP06)', 'Garden of Delight (MAP08)', 'GenEmp Corp. (MAP01)', 'Gothik Gauntlet (MAP12)', 'Hidden Fortress (MAP09)', 'Intruder Alert! (MAP20)', 'Lava Annex (MAP03)', 'Notus Us! (MAP11)', 'Protean Cybex (MAP16)', 'River of Blood (MAP17)', 'The Great Wall (MAP07)', 'The Sewers (MAP13)', 'The War Rooms (MAP19)', 'Tunnel Town (MAP02)', 'Twilight of EnKs (MAP15)', },
    'Powerups': {'007Microtel', 'Body armor', 'Centrophenoxine', 'EnK blinder', 'Force field', 'Kevlar vest', 'Super kevlar vest', },
    'SI arrays': {"'Trode Wars (MAP14) - SI array", 'Alcatraz (MAP04) - SI array', 'Anarchist Dream (MAP10) - SI array', 'Bizarro (MAP18) - SI array', 'Cyber Circus (MAP05) - SI array', 'Desiccant Room (MAP31) - SI array', 'Digi-Ota (MAP06) - SI array', 'Garden of Delight (MAP08) - SI array', 'GenEmp Corp. (MAP01) - SI array', 'Gothik Gauntlet (MAP12) - SI array', 'Hidden Fortress (MAP09) - SI array', 'Intruder Alert! (MAP20) - SI array', 'Lava Annex (MAP03) - SI array', 'Notus Us! (MAP11) - SI array', 'Protean Cybex (MAP16) - SI array', 'River of Blood (MAP17) - SI array', 'The Great Wall (MAP07) - SI array', 'The Sewers (MAP13) - SI array', 'The War Rooms (MAP19) - SI array', 'Tunnel Town (MAP02) - SI array', 'Twilight of EnKs (MAP15) - SI array', },
    'Weapons': {'Cryogun', 'HOIG Reznator', 'Nuker', "Photon 'zooka", 'Stick', 'Tazer', 'Uzi', },
}
