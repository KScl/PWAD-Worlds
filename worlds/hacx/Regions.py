# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import List
from BaseClasses import TypedDict

class ConnectionDict(TypedDict, total=False):
    target: str
    pro: bool

class RegionDict(TypedDict, total=False):
    name: str
    connects_to_hub: bool
    episode: int
    connections: List[ConnectionDict]


regions:List[RegionDict] = [
    # GenEmp Corp. (MAP01)
    {"name":"GenEmp Corp. (MAP01) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"GenEmp Corp. (MAP01) Keycard","pro":False}]},
    {"name":"GenEmp Corp. (MAP01) Keycard",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"GenEmp Corp. (MAP01) Password","pro":False},
        {"target":"GenEmp Corp. (MAP01) Main","pro":False}]},
    {"name":"GenEmp Corp. (MAP01) Password",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"GenEmp Corp. (MAP01) Keycard","pro":False}]},

    # Tunnel Town (MAP02)
    {"name":"Tunnel Town (MAP02) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Tunnel Town (MAP02) Keycard","pro":False}]},
    {"name":"Tunnel Town (MAP02) Keycard",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Tunnel Town (MAP02) Main","pro":False},
        {"target":"Tunnel Town (MAP02) Password","pro":False}]},
    {"name":"Tunnel Town (MAP02) Password",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Tunnel Town (MAP02) Keycard","pro":False}]},

    # Lava Annex (MAP03)
    {"name":"Lava Annex (MAP03) Opening",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Lava Annex (MAP03) Main","pro":False}]},
    {"name":"Lava Annex (MAP03) Main",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Lava Annex (MAP03) Z Blue","pro":False},
        {"target":"Lava Annex (MAP03) Opening","pro":False}]},
    {"name":"Lava Annex (MAP03) Z Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Lava Annex (MAP03) Z Red","pro":False},
        {"target":"Lava Annex (MAP03) Main","pro":False}]},
    {"name":"Lava Annex (MAP03) Z Red",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Lava Annex (MAP03) Main","pro":False}]},

    # Alcatraz (MAP04)
    {"name":"Alcatraz (MAP04) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[]},

    # Cyber Circus (MAP05)
    {"name":"Cyber Circus (MAP05) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"Cyber Circus (MAP05) Open Exit","pro":True},
        {"target":"Cyber Circus (MAP05) Sigma","pro":False}]},
    {"name":"Cyber Circus (MAP05) Sigma",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Cyber Circus (MAP05) Main","pro":False},
        {"target":"Cyber Circus (MAP05) Open Exit","pro":False}]},
    {"name":"Cyber Circus (MAP05) Open Exit",
     "connects_to_hub":False,
     "episode":1,
     "connections":[]},

    # Digi-Ota (MAP06)
    {"name":"Digi-Ota (MAP06) Main",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Digi-Ota (MAP06) Password","pro":False},
        {"target":"Digi-Ota (MAP06) Start","pro":False}]},
    {"name":"Digi-Ota (MAP06) Password",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Digi-Ota (MAP06) Z Blue","pro":False},
        {"target":"Digi-Ota (MAP06) Main","pro":False}]},
    {"name":"Digi-Ota (MAP06) Z Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Digi-Ota (MAP06) Password","pro":False}]},
    {"name":"Digi-Ota (MAP06) Start",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Digi-Ota (MAP06) Main","pro":False}]},

    # The Great Wall (MAP07)
    {"name":"The Great Wall (MAP07) Opening",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"The Great Wall (MAP07) Main","pro":False}]},
    {"name":"The Great Wall (MAP07) Main",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Great Wall (MAP07) Password","pro":False}]},
    {"name":"The Great Wall (MAP07) Password",
     "connects_to_hub":False,
     "episode":2,
     "connections":[]},

    # Garden of Delight (MAP08)
    {"name":"Garden of Delight (MAP08) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Garden of Delight (MAP08) Garden","pro":False}]},
    {"name":"Garden of Delight (MAP08) Garden",
     "connects_to_hub":False,
     "episode":2,
     "connections":[]},

    # Hidden Fortress (MAP09)
    {"name":"Hidden Fortress (MAP09) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Hidden Fortress (MAP09) Fortress","pro":False}]},
    {"name":"Hidden Fortress (MAP09) Fortress",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Hidden Fortress (MAP09) Z-Blue","pro":False},
        {"target":"Hidden Fortress (MAP09) Main","pro":False}]},
    {"name":"Hidden Fortress (MAP09) Z-Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Hidden Fortress (MAP09) Fortress","pro":False}]},

    # Anarchist Dream (MAP10)
    {"name":"Anarchist Dream (MAP10) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[]},

    # Notus Us! (MAP11)
    {"name":"Notus Us! (MAP11) Main",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Notus Us! (MAP11) Password","pro":False},
        {"target":"Notus Us! (MAP11) Early","pro":False}]},
    {"name":"Notus Us! (MAP11) Password",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Notus Us! (MAP11) Main","pro":False},
        {"target":"Notus Us! (MAP11) Keycard","pro":False}]},
    {"name":"Notus Us! (MAP11) Keycard",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Notus Us! (MAP11) Password","pro":False}]},
    {"name":"Notus Us! (MAP11) Early",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Notus Us! (MAP11) Main","pro":False}]},

    # Gothik Gauntlet (MAP12)
    {"name":"Gothik Gauntlet (MAP12) Start",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Gothik Gauntlet (MAP12) Main","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) Main",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Gothik Gauntlet (MAP12) Start","pro":False},
        {"target":"Gothik Gauntlet (MAP12) West City","pro":False},
        {"target":"Gothik Gauntlet (MAP12) Password","pro":False},
        {"target":"Gothik Gauntlet (MAP12) Lift Jump","pro":True},
        {"target":"Gothik Gauntlet (MAP12) Keycard","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) West City",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Gothik Gauntlet (MAP12) East City","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) East City",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Gothik Gauntlet (MAP12) Main","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) Password",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Gothik Gauntlet (MAP12) Main","pro":False},
        {"target":"Gothik Gauntlet (MAP12) East City","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) Lift Jump",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Gothik Gauntlet (MAP12) Password","pro":False}]},
    {"name":"Gothik Gauntlet (MAP12) Keycard",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Gothik Gauntlet (MAP12) Main","pro":False}]},

    # The Sewers (MAP13)
    {"name":"The Sewers (MAP13) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"The Sewers (MAP13) Z Blue","pro":False}]},
    {"name":"The Sewers (MAP13) Z Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"The Sewers (MAP13) Main","pro":False},
        {"target":"The Sewers (MAP13) Z Red","pro":False}]},
    {"name":"The Sewers (MAP13) Z Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"The Sewers (MAP13) Z Blue","pro":False}]},

    # 'Trode Wars (MAP14)
    {"name":"'Trode Wars (MAP14) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"'Trode Wars (MAP14) Sigma","pro":False}]},
    {"name":"'Trode Wars (MAP14) Sigma",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"'Trode Wars (MAP14) Main","pro":False}]},

    # Twilight of EnKs (MAP15)
    {"name":"Twilight of EnKs (MAP15) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Twilight of EnKs (MAP15) Z Blue","pro":False},
        {"target":"Twilight of EnKs (MAP15) Z Orange","pro":False}]},
    {"name":"Twilight of EnKs (MAP15) Z Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Twilight of EnKs (MAP15) Main","pro":False}]},
    {"name":"Twilight of EnKs (MAP15) Z Orange",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Twilight of EnKs (MAP15) Main","pro":False}]},

    # Desiccant Room (MAP31)
    {"name":"Desiccant Room (MAP31) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Desiccant Room (MAP31) Keycard","pro":False}]},
    {"name":"Desiccant Room (MAP31) Keycard",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Desiccant Room (MAP31) Main","pro":False},
        {"target":"Desiccant Room (MAP31) Outer","pro":False}]},
    {"name":"Desiccant Room (MAP31) Outer",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Desiccant Room (MAP31) Keycard","pro":False}]},

    # Protean Cybex (MAP16)
    {"name":"Protean Cybex (MAP16) From Hub",
     "connects_to_hub":True,
     "episode":4,
     "connections":[
        {"target":"Protean Cybex (MAP16) Main","pro":False},
        {"target":"Protean Cybex (MAP16) Switch Press","pro":True}]},
    {"name":"Protean Cybex (MAP16) Main",
     "connects_to_hub":False,
     "episode":4,
     "connections":[]},
    {"name":"Protean Cybex (MAP16) Switch Press",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Protean Cybex (MAP16) Main","pro":False}]},

    # River of Blood (MAP17)
    {"name":"River of Blood (MAP17) Entry",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"River of Blood (MAP17) Main","pro":False}]},
    {"name":"River of Blood (MAP17) Main",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"River of Blood (MAP17) Entry","pro":False}]},

    # Bizarro (MAP18)
    {"name":"Bizarro (MAP18) Opening",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Bizarro (MAP18) All","pro":False}]},
    {"name":"Bizarro (MAP18) All",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Bizarro (MAP18) Opening","pro":False}]},

    # The War Rooms (MAP19)
    {"name":"The War Rooms (MAP19) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[]},

    # Intruder Alert! (MAP20)
    {"name":"Intruder Alert! (MAP20) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Intruder Alert! (MAP20) Sigma","pro":False}]},
    {"name":"Intruder Alert! (MAP20) Sigma",
     "connects_to_hub":False,
     "episode":4,
     "connections":[]},
]
