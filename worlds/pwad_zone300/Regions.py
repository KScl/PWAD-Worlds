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
    # The Spaceport (MAP01)
    {"name":"The Spaceport (MAP01) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[]},

    # Control Facility (MAP02)
    {"name":"Control Facility (MAP02) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Control Facility (MAP02) Yellow","pro":False}]},
    {"name":"Control Facility (MAP02) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Control Facility (MAP02) Main","pro":False},
        {"target":"Control Facility (MAP02) Red","pro":False},
        {"target":"Control Facility (MAP02) Blue","pro":False}]},
    {"name":"Control Facility (MAP02) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[]},
    {"name":"Control Facility (MAP02) Red",
     "connects_to_hub":False,
     "episode":1,
     "connections":[]},

    # The Alleyway (MAP03)
    {"name":"The Alleyway (MAP03) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"The Alleyway (MAP03) Blue","pro":False}]},
    {"name":"The Alleyway (MAP03) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[]},

    # Canyon Hub (MAP04)
    {"name":"Canyon Hub (MAP04) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Canyon Hub (MAP04) Yellow","pro":False}]},
    {"name":"Canyon Hub (MAP04) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Canyon Hub (MAP04) Main","pro":False}]},

    # Skybase 300 (MAP05)
    {"name":"Skybase 300 (MAP05) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Skybase 300 (MAP05) Blue","pro":False}]},
    {"name":"Skybase 300 (MAP05) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Skybase 300 (MAP05) Yellow","pro":False},
        {"target":"Skybase 300 (MAP05) Main","pro":False}]},
    {"name":"Skybase 300 (MAP05) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Skybase 300 (MAP05) Blue","pro":False}]},

    # Whispering Corridor (MAP06)
    {"name":"Whispering Corridor (MAP06) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Whispering Corridor (MAP06) Blue","pro":False}]},
    {"name":"Whispering Corridor (MAP06) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Whispering Corridor (MAP06) Main","pro":False}]},

    # Heavyweight (MAP07)
    {"name":"Heavyweight (MAP07) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[]},

    # Waste Disposal Plant (MAP08)
    {"name":"Waste Disposal Plant (MAP08) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Waste Disposal Plant (MAP08) Red","pro":False}]},
    {"name":"Waste Disposal Plant (MAP08) Red",
     "connects_to_hub":False,
     "episode":1,
     "connections":[
        {"target":"Waste Disposal Plant (MAP08) Blue","pro":False},
        {"target":"Waste Disposal Plant (MAP08) Main","pro":False}]},
    {"name":"Waste Disposal Plant (MAP08) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Waste Disposal Plant (MAP08) Red","pro":False}]},

    # Nuclear Power Station (MAP09)
    {"name":"Nuclear Power Station (MAP09) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[
        {"target":"Nuclear Power Station (MAP09) Red","pro":False},
        {"target":"Nuclear Power Station (MAP09) Blue","pro":False},
        {"target":"Nuclear Power Station (MAP09) Yellow","pro":False}]},
    {"name":"Nuclear Power Station (MAP09) Yellow",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Nuclear Power Station (MAP09) Main","pro":False}]},
    {"name":"Nuclear Power Station (MAP09) Red",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Nuclear Power Station (MAP09) Main","pro":False}]},
    {"name":"Nuclear Power Station (MAP09) Blue",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Nuclear Power Station (MAP09) Main","pro":False}]},

    # Cargo Bay (MAP10)
    {"name":"Cargo Bay (MAP10) Main",
     "connects_to_hub":True,
     "episode":1,
     "connections":[{"target":"Cargo Bay (MAP10) Red","pro":False}]},
    {"name":"Cargo Bay (MAP10) Red",
     "connects_to_hub":False,
     "episode":1,
     "connections":[{"target":"Cargo Bay (MAP10) Main","pro":False}]},

    # Simbattle (MAP11)
    {"name":"Simbattle (MAP11) Start",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Simbattle (MAP11) Main","pro":False}]},
    {"name":"Simbattle (MAP11) Main",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Simbattle (MAP11) Blue","pro":False},
        {"target":"Simbattle (MAP11) Red","pro":False},
        {"target":"Simbattle (MAP11) Yellow","pro":False}]},
    {"name":"Simbattle (MAP11) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Simbattle (MAP11) Main","pro":False}]},
    {"name":"Simbattle (MAP11) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Simbattle (MAP11) Main","pro":False},
        {"target":"Simbattle (MAP11) Blue","pro":False}]},
    {"name":"Simbattle (MAP11) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Simbattle (MAP11) Main","pro":False},
        {"target":"Simbattle (MAP11) Red","pro":False}]},

    # Villa of Pain (MAP12)
    {"name":"Villa of Pain (MAP12) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Villa of Pain (MAP12) Yellow","pro":False}]},
    {"name":"Villa of Pain (MAP12) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Villa of Pain (MAP12) Main","pro":False},
        {"target":"Villa of Pain (MAP12) Red","pro":False}]},
    {"name":"Villa of Pain (MAP12) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Villa of Pain (MAP12) Yellow","pro":False}]},

    # Dark Crypt (MAP13)
    {"name":"Dark Crypt (MAP13) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"Dark Crypt (MAP13) Blue","pro":False},
        {"target":"Dark Crypt (MAP13) Yellow","pro":False}]},
    {"name":"Dark Crypt (MAP13) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Dark Crypt (MAP13) Main","pro":False}]},
    {"name":"Dark Crypt (MAP13) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Dark Crypt (MAP13) Main","pro":False}]},

    # The Circle (MAP14)
    {"name":"The Circle (MAP14) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Circle (MAP14) Red","pro":False},
        {"target":"The Circle (MAP14) Yellow","pro":False}]},
    {"name":"The Circle (MAP14) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Circle (MAP14) Main","pro":False}]},
    {"name":"The Circle (MAP14) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Circle (MAP14) Main","pro":False}]},

    # Trouble Town (MAP15)
    {"name":"Trouble Town (MAP15) Start",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Trouble Town (MAP15) Main","pro":False}]},
    {"name":"Trouble Town (MAP15) Main",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Trouble Town (MAP15) All Keys","pro":False},
        {"target":"Trouble Town (MAP15) Start","pro":False}]},
    {"name":"Trouble Town (MAP15) All Keys",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Trouble Town (MAP15) Main","pro":False}]},

    # Bruiser Fortress (MAP16)
    {"name":"Bruiser Fortress (MAP16) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[{"target":"Bruiser Fortress (MAP16) Yellow","pro":False}]},
    {"name":"Bruiser Fortress (MAP16) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Bruiser Fortress (MAP16) Main","pro":False}]},

    # Constriction (MAP17)
    {"name":"Constriction (MAP17) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"Constriction (MAP17) Red","pro":False},
        {"target":"Constriction (MAP17) Blue","pro":False}]},
    {"name":"Constriction (MAP17) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Constriction (MAP17) Main","pro":False}]},
    {"name":"Constriction (MAP17) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Constriction (MAP17) Main","pro":False}]},

    # Zombie Hideout (MAP18)
    {"name":"Zombie Hideout (MAP18) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"Zombie Hideout (MAP18) Blue","pro":False},
        {"target":"Zombie Hideout (MAP18) Yellow","pro":False}]},
    {"name":"Zombie Hideout (MAP18) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Zombie Hideout (MAP18) Main","pro":False}]},
    {"name":"Zombie Hideout (MAP18) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Zombie Hideout (MAP18) Main","pro":False}]},

    # The Invasion (MAP19)
    {"name":"The Invasion (MAP19) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"The Invasion (MAP19) Yellow","pro":False},
        {"target":"The Invasion (MAP19) Red","pro":False}]},
    {"name":"The Invasion (MAP19) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Invasion (MAP19) Main","pro":False}]},
    {"name":"The Invasion (MAP19) Yellow",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"The Invasion (MAP19) Main","pro":False}]},

    # Death Row (MAP20)
    {"name":"Death Row (MAP20) Main",
     "connects_to_hub":True,
     "episode":2,
     "connections":[
        {"target":"Death Row (MAP20) Blue","pro":False},
        {"target":"Death Row (MAP20) Red","pro":False},
        {"target":"Death Row (MAP20) Blue Ledge","pro":True}]},
    {"name":"Death Row (MAP20) Blue",
     "connects_to_hub":False,
     "episode":2,
     "connections":[
        {"target":"Death Row (MAP20) Main","pro":False},
        {"target":"Death Row (MAP20) Blue Ledge","pro":False}]},
    {"name":"Death Row (MAP20) Red",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Death Row (MAP20) Main","pro":False}]},
    {"name":"Death Row (MAP20) Blue Ledge",
     "connects_to_hub":False,
     "episode":2,
     "connections":[{"target":"Death Row (MAP20) Main","pro":False}]},

    # Blood Lust (MAP21)
    {"name":"Blood Lust (MAP21) Start",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Blood Lust (MAP21) Main","pro":False},
        {"target":"Blood Lust (MAP21) Red","pro":False}]},
    {"name":"Blood Lust (MAP21) Main",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Blood Lust (MAP21) Start","pro":False}]},
    {"name":"Blood Lust (MAP21) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Blood Lust (MAP21) Start","pro":False},
        {"target":"Blood Lust (MAP21) Red Exit","pro":False}]},
    {"name":"Blood Lust (MAP21) Red Exit",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Blood Lust (MAP21) Red","pro":False}]},

    # Firestorm Tomb (MAP22)
    {"name":"Firestorm Tomb (MAP22) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Firestorm Tomb (MAP22) Red","pro":False},
        {"target":"Firestorm Tomb (MAP22) Yellow","pro":False}]},
    {"name":"Firestorm Tomb (MAP22) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Firestorm Tomb (MAP22) Main","pro":False}]},
    {"name":"Firestorm Tomb (MAP22) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Firestorm Tomb (MAP22) Main","pro":False}]},

    # Dungeon of Inferno (MAP23)
    {"name":"Dungeon of Inferno (MAP23) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Dungeon of Inferno (MAP23) Red","pro":False},
        {"target":"Dungeon of Inferno (MAP23) Blue","pro":False}]},
    {"name":"Dungeon of Inferno (MAP23) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Dungeon of Inferno (MAP23) Main","pro":False}]},
    {"name":"Dungeon of Inferno (MAP23) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Dungeon of Inferno (MAP23) Main","pro":False}]},

    # Cavern of the Evil Spirit (MAP24)
    {"name":"Cavern of the Evil Spirit (MAP24) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Cavern of the Evil Spirit (MAP24) Blue","pro":False}]},
    {"name":"Cavern of the Evil Spirit (MAP24) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Cavern of the Evil Spirit (MAP24) Main","pro":False},
        {"target":"Cavern of the Evil Spirit (MAP24) Red","pro":False}]},
    {"name":"Cavern of the Evil Spirit (MAP24) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Cavern of the Evil Spirit (MAP24) Blue","pro":False}]},

    # Hellucination (MAP25)
    {"name":"Hellucination (MAP25) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Hellucination (MAP25) Yellow","pro":False},
        {"target":"Hellucination (MAP25) Red","pro":False},
        {"target":"Hellucination (MAP25) Blue","pro":False}]},
    {"name":"Hellucination (MAP25) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Hellucination (MAP25) Main","pro":False}]},
    {"name":"Hellucination (MAP25) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Hellucination (MAP25) Main","pro":False}]},
    {"name":"Hellucination (MAP25) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Hellucination (MAP25) Main","pro":False}]},

    # Valley of Brimstone (MAP26)
    {"name":"Valley of Brimstone (MAP26) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Valley of Brimstone (MAP26) Yellow","pro":False}]},
    {"name":"Valley of Brimstone (MAP26) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Valley of Brimstone (MAP26) Main","pro":False}]},

    # Dissect (MAP27)
    {"name":"Dissect (MAP27) Start",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Dissect (MAP27) Main","pro":False}]},
    {"name":"Dissect (MAP27) Main",
     "connects_to_hub":False,
     "episode":3,
     "connections":[
        {"target":"Dissect (MAP27) Start","pro":False},
        {"target":"Dissect (MAP27) Red","pro":False}]},
    {"name":"Dissect (MAP27) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Dissect (MAP27) Main","pro":False}]},

    # Unholy Demise (MAP28)
    {"name":"Unholy Demise (MAP28) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[
        {"target":"Unholy Demise (MAP28) Yellow","pro":False},
        {"target":"Unholy Demise (MAP28) Red","pro":False}]},
    {"name":"Unholy Demise (MAP28) Red",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Unholy Demise (MAP28) Main","pro":False}]},
    {"name":"Unholy Demise (MAP28) Yellow",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Unholy Demise (MAP28) Main","pro":False}]},

    # Den of Torture (MAP29)
    {"name":"Den of Torture (MAP29) Main",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Den of Torture (MAP29) Blue","pro":False}]},
    {"name":"Den of Torture (MAP29) Blue",
     "connects_to_hub":False,
     "episode":3,
     "connections":[{"target":"Den of Torture (MAP29) Main","pro":False}]},

    # Eternal Core (MAP30)
    {"name":"Eternal Core (MAP30) Safe Area",
     "connects_to_hub":True,
     "episode":3,
     "connections":[{"target":"Eternal Core (MAP30) Main","pro":False}]},
    {"name":"Eternal Core (MAP30) Main",
     "connects_to_hub":False,
     "episode":3,
     "connections":[]},

    # Creepy (MAP31)
    {"name":"Creepy (MAP31) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Creepy (MAP31) All Keys","pro":False}]},
    {"name":"Creepy (MAP31) All Keys",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Creepy (MAP31) Main","pro":False}]},

    # Condemnation (MAP32)
    {"name":"Condemnation (MAP32) Main",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Condemnation (MAP32) Blue","pro":False}]},
    {"name":"Condemnation (MAP32) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Condemnation (MAP32) Yellow","pro":False}]},
    {"name":"Condemnation (MAP32) Yellow",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Condemnation (MAP32) Red","pro":False}]},
    {"name":"Condemnation (MAP32) Red",
     "connects_to_hub":False,
     "episode":4,
     "connections":[]},

    # Zerstorung (MAP33)
    {"name":"Zerstorung (MAP33) Start",
     "connects_to_hub":True,
     "episode":4,
     "connections":[{"target":"Zerstorung (MAP33) Main","pro":False}]},
    {"name":"Zerstorung (MAP33) Main",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Zerstorung (MAP33) Start","pro":False},
        {"target":"Zerstorung (MAP33) Blue","pro":False}]},
    {"name":"Zerstorung (MAP33) Blue",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Zerstorung (MAP33) Main","pro":False},
        {"target":"Zerstorung (MAP33) Bosses","pro":False}]},
    {"name":"Zerstorung (MAP33) Bosses",
     "connects_to_hub":False,
     "episode":4,
     "connections":[
        {"target":"Zerstorung (MAP33) All Keys","pro":False},
        {"target":"Zerstorung (MAP33) Blue","pro":False}]},
    {"name":"Zerstorung (MAP33) All Keys",
     "connects_to_hub":False,
     "episode":4,
     "connections":[{"target":"Zerstorung (MAP33) Bosses","pro":False}]},
]
