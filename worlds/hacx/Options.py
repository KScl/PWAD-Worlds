import typing

from Options import Visibility, PerGameCommonOptions, Range, Choice, Toggle, DeathLink, DefaultOnToggle, StartInventoryPool
from dataclasses import dataclass


class Difficulty(Choice):
    """
    Choose the difficulty option. Those match HacX's difficulty options.
    baby (Please don't shoot!) double ammos, half damage, less monsters or strength.
    easy (Arrgh, I need health!) less monsters or strength.
    medium (Let's rip them apart!) Default.
    hard (I am immortal) More monsters or strength.
    insanity (Insanity!) Monsters attack more rapidly and respawn.
    """
    display_name = "Difficulty"
    option_baby = 0
    option_easy = 1
    option_medium = 2
    option_hard = 3
    option_insanity = 4
    default = 2


class RandomMonsters(Choice):
    """
    Choose how monsters are randomized.
    vanilla: No randomization
    shuffle: Monsters are shuffled within the level
    random_balanced: Monsters are completely randomized, but balanced based on existing ratio in the level. (Small monsters vs medium vs big)
    random_chaotic: Monsters are completely randomized, but balanced based on existing ratio in the entire game.

    This option is untested for HacX. Use it at your own risk.
    """
    display_name = "Random Monsters"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    option_random_chaotic = 3
    default = 0


class RandomPickups(Choice):
    """
    Choose how pickups are randomized.
    vanilla: No randomization
    shuffle: Pickups are shuffled within the level
    random_balanced: Pickups are completely randomized, but balanced based on existing ratio in the level. (Small pickups vs Big)
    """
    display_name = "Random Pickups"
    option_vanilla = 0
    option_shuffle = 1
    option_random_balanced = 2
    default = 1


class RandomMusic(Choice):
    """
    Level musics will be randomized.
    vanilla: No randomization
    shuffle_selected: Selected episodes' levels will be shuffled
    shuffle_game: All the music will be shuffled
    """
    display_name = "Random Music"
    option_vanilla = 0
    option_shuffle_selected = 1
    option_shuffle_game = 2
    default = 0
    

class FlipLevels(Choice):
    """
    Flip levels on one axis.
    vanilla: No flipping
    flipped: All levels are flipped
    random: Random levels are flipped
    """
    display_name = "Flip Levels"
    option_vanilla = 0
    option_flipped = 1
    option_randomly_flipped = 2
    default = 0


class AllowDeathLogic(Toggle):
    """Some locations require a timed puzzle that can only be tried once.
    After which, if the player failed to get it, the location cannot be checked anymore.
    By default, no progression items are placed here. There is a way, hovewer, to still get them:
    Get killed in the current map. The map will reset, you can now attempt the puzzle again."""
    display_name = "Allow Death Logic"

    
class Pro(Toggle):
    """Include difficult tricks into rules. Mostly employed by speed runners.
    i.e.: Leaps across to a locked area, trigger a switch behind a window at the right angle, etc."""
    display_name = "Pro HacX"


class StartWithSIArrays(Toggle):
    """Give the player all SI Array items from the start."""
    display_name = "Start With SI Arrays"


class ResetLevelOnDeath(DefaultOnToggle):
    """When dying, levels are reset and monsters respawned. But inventory and checks are kept.
    Turning this setting off is considered easy mode. Good for new players that don't know the levels well."""
    display_name = "Reset level on death"


class Episode1(DefaultOnToggle):
    """Episode 1 (MAP01 - MAP06)
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 1"


class Episode2(DefaultOnToggle):
    """Episode 2 (MAP07 - MAP11).
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 2"


class Episode3(DefaultOnToggle):
    """Episode 3 (MAP12 - MAP15).
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 3"


class Episode4(Toggle):
    """Episode 4 (MAP31 - MAP20).
    If none of the episodes are chosen, Episode 1 will be chosen by default."""
    display_name = "Episode 4"




class SplitValise(Toggle):
    """Split the Valise into four individual items, each one increasing ammo capacity for one type of weapon only."""
    display_name = "Split Valise"


class ValiseCount(Range):
    """How many Valises will be available.
    If Split Valises is set, this will be the number of each capacity upgrade available."""
    display_name = "Valise Count"
    range_start = 0
    range_end = 10
    default = 1


class MaxAmmoRounds(Range):
    """Set the starting ammo capacity for rounds."""
    display_name = "Max Ammo - Rounds"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 100
    range_end = 999
    default = 100


class MaxAmmoCartridges(Range):
    """Set the starting ammo capacity for cartridges."""
    display_name = "Max Ammo - Cartridges"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 50
    range_end = 999
    default = 50


class MaxAmmoTorpedoes(Range):
    """Set the starting ammo capacity for torpedoes."""
    display_name = "Max Ammo - Torpedoes"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 50
    range_end = 999
    default = 50


class MaxAmmoMolecules(Range):
    """Set the starting ammo capacity for molecules."""
    display_name = "Max Ammo - Molecules"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 300
    range_end = 999
    default = 300


class AddedAmmoRounds(Range):
    """Set the amount of round capacity added when collecting a backpack or capacity upgrade."""
    display_name = "Added Ammo - Rounds"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 10
    range_end = 999
    default = 100


class AddedAmmoCartridges(Range):
    """Set the amount of cartridge capacity added when collecting a backpack or capacity upgrade."""
    display_name = "Added Ammo - Cartridges"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 5
    range_end = 999
    default = 50


class AddedAmmoTorpedoes(Range):
    """Set the amount of torpedo capacity added when collecting a backpack or capacity upgrade."""
    display_name = "Added Ammo - Torpedoes"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 5
    range_end = 999
    default = 50


class AddedAmmoMolecules(Range):
    """Set the amount of molecule capacity added when collecting a backpack or capacity upgrade."""
    display_name = "Added Ammo - Molecules"
    visibility = Visibility.all ^ Visibility.spoiler
    range_start = 30
    range_end = 999
    default = 300


@dataclass
class HacXOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    difficulty: Difficulty
    random_monsters: RandomMonsters
    random_pickups: RandomPickups
    random_music: RandomMusic
    flip_levels: FlipLevels
    allow_death_logic: AllowDeathLogic
    pro: Pro
    start_with_si_arrays: StartWithSIArrays
    death_link: DeathLink
    reset_level_on_death: ResetLevelOnDeath
    episode1: Episode1
    episode2: Episode2
    episode3: Episode3
    episode4: Episode4

    split_valise: SplitValise
    valise_count: ValiseCount
    max_ammo_rounds: MaxAmmoRounds
    max_ammo_cartridges: MaxAmmoCartridges
    max_ammo_torpedoes: MaxAmmoTorpedoes
    max_ammo_molecules: MaxAmmoMolecules
    added_ammo_rounds: AddedAmmoRounds
    added_ammo_cartridges: AddedAmmoCartridges
    added_ammo_torpedoes: AddedAmmoTorpedoes
    added_ammo_molecules: AddedAmmoMolecules
