import pytest
import util_ships


def test_normal_case():
    assert util_ships.ship_file_name("Enterprise", "anaconda") == "Enterprise"
    assert util_ships.ship_file_name("Voyager", "asp") == "Voyager"
    assert util_ships.ship_file_name("Rocinante", "diamondback") == "Rocinante"
    assert util_ships.ship_file_name("", "cutter") == "Imperial Cutter"


def test_edge_cases():
    assert util_ships.ship_file_name("Enterprise*", "anaconda") == "Enterprise_"
    assert util_ships.ship_file_name("Voyager<", "asp") == "Voyager_"
    assert util_ships.ship_file_name("Rocinante?", "diamondback") == "Rocinante_"
    assert util_ships.ship_file_name("File:name", "cutter") == "File_name"
    assert util_ships.ship_file_name("Name/with/slash", "anaconda") == "slash"


def test_reserved_names():
    # Windows reserved filenames like CON, PRN, AUX, NUL, COM1, LPT1, etc.
    reserved_names = ["CON", "PRN", "AUX", "NUL", "COM1", "LPT1"]
    for reserved in reserved_names:
        assert util_ships.ship_file_name(reserved, "cutter") == reserved + "_"


def test_mapping():
    assert util_ships.ship_file_name("", "adder") == "Adder"
    assert util_ships.ship_file_name("", "anaconda") == "Anaconda"
    assert util_ships.ship_file_name("", "asp") == "Asp Explorer"
    assert util_ships.ship_file_name("", "belugaliner") == "Beluga Liner"
    assert util_ships.ship_file_name("", "cobramkiii") == "Cobra MkIII"
    assert util_ships.ship_file_name("", "clipper") == "Panther Clipper"
    assert util_ships.ship_file_name("", "federation_corvette") == "Federal Corvette"
    assert util_ships.ship_file_name("", "krait_mkii") == "Krait MkII"
    assert util_ships.ship_file_name("", "mamba") == "Mamba"
    assert util_ships.ship_file_name("", "typex") == "Alliance Chieftain"
    assert util_ships.ship_file_name("", "viper") == "Viper MkIII"
    assert util_ships.ship_file_name("", "vulture") == "Vulture"
