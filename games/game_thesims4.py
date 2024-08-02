from ..basic_game import BasicGame


class TheSims4GamePlugin(BasicGame):
    # Plugin
    Name = "The Sims 4 Support Plugin"
    Description = "Adds advanced support for game The Sims 4"
    Author = "Cram42"
    Version = "0.2.0"

    # Game
    GameName = "The Sims 4"
    GameShortName = "thesims4"
    ValidShortNames = ["thesims4", "sims4", "ts4"]
    GameSteamId = 1222670
    GameOriginManifestIds = ["OFB-EAST:109552677"]
    GameOriginWatcherExecutables = ("TS4_x64.exe",)

    # Paths
    GameBinary = "Game/Bin/TS4_x64.exe"
    GameDataPath = "%DOCUMENTS%/Electronic Arts/The Sims 4"
