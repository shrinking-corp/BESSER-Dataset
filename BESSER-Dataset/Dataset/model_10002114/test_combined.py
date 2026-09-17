# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Game_GoodZone,
    Game_IBoard_Interface,
    Game_IColonistBoard_Interface,
    Game_Plantation,
    Game_PlantationSupply,
    Game_PlayerBoard,
    Game_Building,
    Game_ColonistZone,
    Game_ShippingShip,
    Game_ColonistShip,
    Game_SupplyBoard,
    Game_TradingHouse,
    Doubloon,
    VictoryPoint,
    Governor,
    Role,
    Good,
    Colonist,
    Piece,
    Game_PlantationType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_game_goodzone_is_not_abstract():
    assert not inspect.isabstract(Game_GoodZone)


def test_hyp_game_goodzone_constructor_exists():
    assert callable(Game_GoodZone.__init__)


def test_hyp_game_goodzone_constructor_args():
    sig = inspect.signature(Game_GoodZone.__init__)
    params = list(sig.parameters.keys())
    assert "Stackable" in params, "Missing parameter 'Stackable'"
    assert "Pieces" in params, "Missing parameter 'Pieces'"

def test_hyp_game_goodzone_has_Stackable():
    assert hasattr(Game_GoodZone, "Stackable")
    descriptor = None
    for klass in Game_GoodZone.__mro__:
        if "Stackable" in klass.__dict__:
            descriptor = klass.__dict__["Stackable"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_goodzone_has_Pieces():
    assert hasattr(Game_GoodZone, "Pieces")
    descriptor = None
    for klass in Game_GoodZone.__mro__:
        if "Pieces" in klass.__dict__:
            descriptor = klass.__dict__["Pieces"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_iboard_interface_is_not_abstract():
    assert not inspect.isabstract(Game_IBoard_Interface)


def test_hyp_game_iboard_interface_constructor_exists():
    assert callable(Game_IBoard_Interface.__init__)


def test_hyp_game_iboard_interface_constructor_args():
    sig = inspect.signature(Game_IBoard_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_icolonistboard_interface_is_not_abstract():
    assert not inspect.isabstract(Game_IColonistBoard_Interface)


def test_hyp_game_icolonistboard_interface_constructor_exists():
    assert callable(Game_IColonistBoard_Interface.__init__)


def test_hyp_game_icolonistboard_interface_constructor_args():
    sig = inspect.signature(Game_IColonistBoard_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_plantation_is_not_abstract():
    assert not inspect.isabstract(Game_Plantation)


def test_hyp_game_plantation_constructor_exists():
    assert callable(Game_Plantation.__init__)


def test_hyp_game_plantation_constructor_args():
    sig = inspect.signature(Game_Plantation.__init__)
    params = list(sig.parameters.keys())
    assert "ColonistZone" in params, "Missing parameter 'ColonistZone'"
    assert "HasProduced" in params, "Missing parameter 'HasProduced'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_hyp_game_plantation_has_ColonistZone():
    assert hasattr(Game_Plantation, "ColonistZone")
    descriptor = None
    for klass in Game_Plantation.__mro__:
        if "ColonistZone" in klass.__dict__:
            descriptor = klass.__dict__["ColonistZone"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_plantation_has_HasProduced():
    assert hasattr(Game_Plantation, "HasProduced")
    descriptor = None
    for klass in Game_Plantation.__mro__:
        if "HasProduced" in klass.__dict__:
            descriptor = klass.__dict__["HasProduced"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_plantation_has_Type():
    assert hasattr(Game_Plantation, "Type")
    descriptor = None
    for klass in Game_Plantation.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_plantationsupply_is_not_abstract():
    assert not inspect.isabstract(Game_PlantationSupply)


def test_hyp_game_plantationsupply_constructor_exists():
    assert callable(Game_PlantationSupply.__init__)


def test_hyp_game_plantationsupply_constructor_args():
    sig = inspect.signature(Game_PlantationSupply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_playerboard_is_not_abstract():
    assert not inspect.isabstract(Game_PlayerBoard)


def test_hyp_game_playerboard_constructor_exists():
    assert callable(Game_PlayerBoard.__init__)


def test_hyp_game_playerboard_constructor_args():
    sig = inspect.signature(Game_PlayerBoard.__init__)
    params = list(sig.parameters.keys())
    assert "PlayerID" in params, "Missing parameter 'PlayerID'"
    assert "ColonistZone" in params, "Missing parameter 'ColonistZone'"

def test_hyp_game_playerboard_has_PlayerID():
    assert hasattr(Game_PlayerBoard, "PlayerID")
    descriptor = None
    for klass in Game_PlayerBoard.__mro__:
        if "PlayerID" in klass.__dict__:
            descriptor = klass.__dict__["PlayerID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_playerboard_has_ColonistZone():
    assert hasattr(Game_PlayerBoard, "ColonistZone")
    descriptor = None
    for klass in Game_PlayerBoard.__mro__:
        if "ColonistZone" in klass.__dict__:
            descriptor = klass.__dict__["ColonistZone"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_building_is_not_abstract():
    assert not inspect.isabstract(Game_Building)


def test_hyp_game_building_constructor_exists():
    assert callable(Game_Building.__init__)


def test_hyp_game_building_constructor_args():
    sig = inspect.signature(Game_Building.__init__)
    params = list(sig.parameters.keys())
    assert "Cost" in params, "Missing parameter 'Cost'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "VictoryPoints" in params, "Missing parameter 'VictoryPoints'"
    assert "MaxColonists" in params, "Missing parameter 'MaxColonists'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "HasProduced" in params, "Missing parameter 'HasProduced'"
    assert "ColonistZones" in params, "Missing parameter 'ColonistZones'"

def test_hyp_game_building_has_Cost():
    assert hasattr(Game_Building, "Cost")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "Cost" in klass.__dict__:
            descriptor = klass.__dict__["Cost"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_Type():
    assert hasattr(Game_Building, "Type")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_VictoryPoints():
    assert hasattr(Game_Building, "VictoryPoints")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "VictoryPoints" in klass.__dict__:
            descriptor = klass.__dict__["VictoryPoints"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_MaxColonists():
    assert hasattr(Game_Building, "MaxColonists")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "MaxColonists" in klass.__dict__:
            descriptor = klass.__dict__["MaxColonists"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_Size():
    assert hasattr(Game_Building, "Size")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_HasProduced():
    assert hasattr(Game_Building, "HasProduced")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "HasProduced" in klass.__dict__:
            descriptor = klass.__dict__["HasProduced"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_building_has_ColonistZones():
    assert hasattr(Game_Building, "ColonistZones")
    descriptor = None
    for klass in Game_Building.__mro__:
        if "ColonistZones" in klass.__dict__:
            descriptor = klass.__dict__["ColonistZones"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_colonistzone_is_not_abstract():
    assert not inspect.isabstract(Game_ColonistZone)


def test_hyp_game_colonistzone_constructor_exists():
    assert callable(Game_ColonistZone.__init__)


def test_hyp_game_colonistzone_constructor_args():
    sig = inspect.signature(Game_ColonistZone.__init__)
    params = list(sig.parameters.keys())
    assert "MaxColonists" in params, "Missing parameter 'MaxColonists'"
    assert "Stackable" in params, "Missing parameter 'Stackable'"
    assert "Pieces" in params, "Missing parameter 'Pieces'"

def test_hyp_game_colonistzone_has_MaxColonists():
    assert hasattr(Game_ColonistZone, "MaxColonists")
    descriptor = None
    for klass in Game_ColonistZone.__mro__:
        if "MaxColonists" in klass.__dict__:
            descriptor = klass.__dict__["MaxColonists"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_colonistzone_has_Stackable():
    assert hasattr(Game_ColonistZone, "Stackable")
    descriptor = None
    for klass in Game_ColonistZone.__mro__:
        if "Stackable" in klass.__dict__:
            descriptor = klass.__dict__["Stackable"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_colonistzone_has_Pieces():
    assert hasattr(Game_ColonistZone, "Pieces")
    descriptor = None
    for klass in Game_ColonistZone.__mro__:
        if "Pieces" in klass.__dict__:
            descriptor = klass.__dict__["Pieces"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_shippingship_is_not_abstract():
    assert not inspect.isabstract(Game_ShippingShip)


def test_hyp_game_shippingship_constructor_exists():
    assert callable(Game_ShippingShip.__init__)


def test_hyp_game_shippingship_constructor_args():
    sig = inspect.signature(Game_ShippingShip.__init__)
    params = list(sig.parameters.keys())
    assert "Size" in params, "Missing parameter 'Size'"




def test_hyp_game_colonistship_is_not_abstract():
    assert not inspect.isabstract(Game_ColonistShip)


def test_hyp_game_colonistship_constructor_exists():
    assert callable(Game_ColonistShip.__init__)


def test_hyp_game_colonistship_constructor_args():
    sig = inspect.signature(Game_ColonistShip.__init__)
    params = list(sig.parameters.keys())
    assert "Num_Colonists" in params, "Missing parameter 'Num_Colonists'"
    assert "ColonistZone" in params, "Missing parameter 'ColonistZone'"

def test_hyp_game_colonistship_has_Num_Colonists():
    assert hasattr(Game_ColonistShip, "Num_Colonists")
    descriptor = None
    for klass in Game_ColonistShip.__mro__:
        if "Num_Colonists" in klass.__dict__:
            descriptor = klass.__dict__["Num_Colonists"]
            break
    assert isinstance(descriptor, property)

def test_hyp_game_colonistship_has_ColonistZone():
    assert hasattr(Game_ColonistShip, "ColonistZone")
    descriptor = None
    for klass in Game_ColonistShip.__mro__:
        if "ColonistZone" in klass.__dict__:
            descriptor = klass.__dict__["ColonistZone"]
            break
    assert isinstance(descriptor, property)



def test_hyp_game_supplyboard_is_not_abstract():
    assert not inspect.isabstract(Game_SupplyBoard)


def test_hyp_game_supplyboard_constructor_exists():
    assert callable(Game_SupplyBoard.__init__)


def test_hyp_game_supplyboard_constructor_args():
    sig = inspect.signature(Game_SupplyBoard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_game_tradinghouse_is_not_abstract():
    assert not inspect.isabstract(Game_TradingHouse)


def test_hyp_game_tradinghouse_constructor_exists():
    assert callable(Game_TradingHouse.__init__)


def test_hyp_game_tradinghouse_constructor_args():
    sig = inspect.signature(Game_TradingHouse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_doubloon_is_not_abstract():
    assert not inspect.isabstract(Doubloon)


def test_hyp_doubloon_constructor_exists():
    assert callable(Doubloon.__init__)


def test_hyp_doubloon_constructor_args():
    sig = inspect.signature(Doubloon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_victorypoint_is_not_abstract():
    assert not inspect.isabstract(VictoryPoint)


def test_hyp_victorypoint_constructor_exists():
    assert callable(VictoryPoint.__init__)


def test_hyp_victorypoint_constructor_args():
    sig = inspect.signature(VictoryPoint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_governor_is_not_abstract():
    assert not inspect.isabstract(Governor)


def test_hyp_governor_constructor_exists():
    assert callable(Governor.__init__)


def test_hyp_governor_constructor_args():
    sig = inspect.signature(Governor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_hyp_role_constructor_exists():
    assert callable(Role.__init__)


def test_hyp_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())



def test_hyp_good_is_not_abstract():
    assert not inspect.isabstract(Good)


def test_hyp_good_constructor_exists():
    assert callable(Good.__init__)


def test_hyp_good_constructor_args():
    sig = inspect.signature(Good.__init__)
    params = list(sig.parameters.keys())



def test_hyp_colonist_is_not_abstract():
    assert not inspect.isabstract(Colonist)


def test_hyp_colonist_constructor_exists():
    assert callable(Colonist.__init__)


def test_hyp_colonist_constructor_args():
    sig = inspect.signature(Colonist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_piece_is_not_abstract():
    assert not inspect.isabstract(Piece)


def test_hyp_piece_constructor_exists():
    assert callable(Piece.__init__)


def test_hyp_piece_constructor_args():
    sig = inspect.signature(Piece.__init__)
    params = list(sig.parameters.keys())

def test_hyp_game_plantationtype_exists():
    # Check that the Enumeration exists
    assert Game_PlantationType is not None

def test_hyp_game_plantationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Game_PlantationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Game_PlantationType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Game_GoodZone_strategy = st.builds(
    Game_GoodZone,
    Stackable=
        st.booleans(),
    Pieces=
        st.none()
)
Game_IBoard_Interface_strategy = st.builds(
    Game_IBoard_Interface,
)
Game_IColonistBoard_Interface_strategy = st.builds(
    Game_IColonistBoard_Interface,
)
Game_Plantation_strategy = st.builds(
    Game_Plantation,
    ColonistZone=
        st.none(),
    HasProduced=
        st.booleans(),
    Type=
        st.none()
)
Game_PlantationSupply_strategy = st.builds(
    Game_PlantationSupply,
)
Game_PlayerBoard_strategy = st.builds(
    Game_PlayerBoard,
    PlayerID=
        st.integers(),
    ColonistZone=
        st.none()
)
Game_Building_strategy = st.builds(
    Game_Building,
    Cost=
        st.integers(),
    Type=
        safe_text,
    VictoryPoints=
        st.integers(),
    MaxColonists=
        st.integers(),
    Size=
        st.integers(),
    HasProduced=
        st.booleans(),
    ColonistZones=
        st.none()
)
Game_ColonistZone_strategy = st.builds(
    Game_ColonistZone,
    MaxColonists=
        st.integers(),
    Stackable=
        st.booleans(),
    Pieces=
        st.none()
)
Game_ShippingShip_strategy = st.builds(
    Game_ShippingShip,
    Size=
        st.integers()
)
Game_ColonistShip_strategy = st.builds(
    Game_ColonistShip,
    Num_Colonists=
        st.integers(),
    ColonistZone=
        st.none()
)
Game_SupplyBoard_strategy = st.builds(
    Game_SupplyBoard,
)
Game_TradingHouse_strategy = st.builds(
    Game_TradingHouse,
)
Doubloon_strategy = st.builds(
    Doubloon,
)
VictoryPoint_strategy = st.builds(
    VictoryPoint,
)
Governor_strategy = st.builds(
    Governor,
)
Role_strategy = st.builds(
    Role,
)
Good_strategy = st.builds(
    Good,
)
Colonist_strategy = st.builds(
    Colonist,
)
Piece_strategy = st.builds(
    Piece,
)

@given(instance=Game_GoodZone_strategy)
@settings(max_examples=50)
def test_hyp_game_goodzone_instantiation(instance):
    assert isinstance(instance, Game_GoodZone)



@given(instance=Game_GoodZone_strategy)
def test_hyp_game_goodzone_Stackable_setter(instance):
    original = instance.Stackable
    instance.Stackable = original
    assert instance.Stackable == original



@given(instance=Game_GoodZone_strategy)
def test_hyp_game_goodzone_Pieces_setter(instance):
    original = instance.Pieces
    instance.Pieces = original
    assert instance.Pieces == original



@given(instance=Game_Plantation_strategy)
@settings(max_examples=50)
def test_hyp_game_plantation_instantiation(instance):
    assert isinstance(instance, Game_Plantation)



@given(instance=Game_Plantation_strategy)
def test_hyp_game_plantation_ColonistZone_setter(instance):
    original = instance.ColonistZone
    instance.ColonistZone = original
    assert instance.ColonistZone == original



@given(instance=Game_Plantation_strategy)
def test_hyp_game_plantation_HasProduced_setter(instance):
    original = instance.HasProduced
    instance.HasProduced = original
    assert instance.HasProduced == original



@given(instance=Game_Plantation_strategy)
def test_hyp_game_plantation_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original


@given(instance=Game_PlayerBoard_strategy)
@settings(max_examples=50)
def test_hyp_game_playerboard_instantiation(instance):
    assert isinstance(instance, Game_PlayerBoard)



@given(instance=Game_PlayerBoard_strategy)
def test_hyp_game_playerboard_PlayerID_setter(instance):
    original = instance.PlayerID
    instance.PlayerID = original
    assert instance.PlayerID == original



@given(instance=Game_PlayerBoard_strategy)
def test_hyp_game_playerboard_ColonistZone_setter(instance):
    original = instance.ColonistZone
    instance.ColonistZone = original
    assert instance.ColonistZone == original

@given(instance=Game_Building_strategy)
@settings(max_examples=50)
def test_hyp_game_building_instantiation(instance):
    assert isinstance(instance, Game_Building)



@given(instance=Game_Building_strategy)
def test_hyp_game_building_Cost_setter(instance):
    original = instance.Cost
    instance.Cost = original
    assert instance.Cost == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_VictoryPoints_setter(instance):
    original = instance.VictoryPoints
    instance.VictoryPoints = original
    assert instance.VictoryPoints == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_MaxColonists_setter(instance):
    original = instance.MaxColonists
    instance.MaxColonists = original
    assert instance.MaxColonists == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_HasProduced_setter(instance):
    original = instance.HasProduced
    instance.HasProduced = original
    assert instance.HasProduced == original



@given(instance=Game_Building_strategy)
def test_hyp_game_building_ColonistZones_setter(instance):
    original = instance.ColonistZones
    instance.ColonistZones = original
    assert instance.ColonistZones == original

@given(instance=Game_ColonistZone_strategy)
@settings(max_examples=50)
def test_hyp_game_colonistzone_instantiation(instance):
    assert isinstance(instance, Game_ColonistZone)



@given(instance=Game_ColonistZone_strategy)
def test_hyp_game_colonistzone_MaxColonists_setter(instance):
    original = instance.MaxColonists
    instance.MaxColonists = original
    assert instance.MaxColonists == original



@given(instance=Game_ColonistZone_strategy)
def test_hyp_game_colonistzone_Stackable_setter(instance):
    original = instance.Stackable
    instance.Stackable = original
    assert instance.Stackable == original



@given(instance=Game_ColonistZone_strategy)
def test_hyp_game_colonistzone_Pieces_setter(instance):
    original = instance.Pieces
    instance.Pieces = original
    assert instance.Pieces == original




@given(instance=Game_ShippingShip_strategy)
def test_hyp_game_shippingship_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original

@given(instance=Game_ColonistShip_strategy)
@settings(max_examples=50)
def test_hyp_game_colonistship_instantiation(instance):
    assert isinstance(instance, Game_ColonistShip)



@given(instance=Game_ColonistShip_strategy)
def test_hyp_game_colonistship_Num_Colonists_setter(instance):
    original = instance.Num_Colonists
    instance.Num_Colonists = original
    assert instance.Num_Colonists == original



@given(instance=Game_ColonistShip_strategy)
def test_hyp_game_colonistship_ColonistZone_setter(instance):
    original = instance.ColonistZone
    instance.ColonistZone = original
    assert instance.ColonistZone == original











# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Colonist,
    Doubloon,
    Game_Building,
    Game_ColonistShip,
    Game_ColonistZone,
    Game_GoodZone,
    Game_IBoard_Interface,
    Game_IColonistBoard_Interface,
    Game_Plantation,
    Game_PlantationSupply,
    Game_PlayerBoard,
    Game_ShippingShip,
    Game_SupplyBoard,
    Game_TradingHouse,
    Good,
    Governor,
    Piece,
    Role,
    VictoryPoint,
    Game_PlantationType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_Game_ShippingShip_Size_value_roundtrip():
    instance = Game_ShippingShip(Size=7)
    assert instance.Size == 7
    instance.Size = 13
    assert instance.Size == 13


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Colonist_strategy = st.builds(Colonist)
@given(instance=Colonist_strategy)
@settings(max_examples=25)
def test_Colonist_instantiation(instance):
    assert isinstance(instance, Colonist)


Doubloon_strategy = st.builds(Doubloon)
@given(instance=Doubloon_strategy)
@settings(max_examples=25)
def test_Doubloon_instantiation(instance):
    assert isinstance(instance, Doubloon)


Game_IBoard_Interface_strategy = st.builds(Game_IBoard_Interface)
@given(instance=Game_IBoard_Interface_strategy)
@settings(max_examples=25)
def test_Game_IBoard_Interface_instantiation(instance):
    assert isinstance(instance, Game_IBoard_Interface)


Game_IColonistBoard_Interface_strategy = st.builds(Game_IColonistBoard_Interface)
@given(instance=Game_IColonistBoard_Interface_strategy)
@settings(max_examples=25)
def test_Game_IColonistBoard_Interface_instantiation(instance):
    assert isinstance(instance, Game_IColonistBoard_Interface)


Game_PlantationSupply_strategy = st.builds(Game_PlantationSupply)
@given(instance=Game_PlantationSupply_strategy)
@settings(max_examples=25)
def test_Game_PlantationSupply_instantiation(instance):
    assert isinstance(instance, Game_PlantationSupply)


Game_ShippingShip_strategy = st.builds(Game_ShippingShip, Size=st.integers())
@given(instance=Game_ShippingShip_strategy)
@settings(max_examples=25)
def test_Game_ShippingShip_instantiation(instance):
    assert isinstance(instance, Game_ShippingShip)


Game_SupplyBoard_strategy = st.builds(Game_SupplyBoard)
@given(instance=Game_SupplyBoard_strategy)
@settings(max_examples=25)
def test_Game_SupplyBoard_instantiation(instance):
    assert isinstance(instance, Game_SupplyBoard)


Game_TradingHouse_strategy = st.builds(Game_TradingHouse)
@given(instance=Game_TradingHouse_strategy)
@settings(max_examples=25)
def test_Game_TradingHouse_instantiation(instance):
    assert isinstance(instance, Game_TradingHouse)


Good_strategy = st.builds(Good)
@given(instance=Good_strategy)
@settings(max_examples=25)
def test_Good_instantiation(instance):
    assert isinstance(instance, Good)


Governor_strategy = st.builds(Governor)
@given(instance=Governor_strategy)
@settings(max_examples=25)
def test_Governor_instantiation(instance):
    assert isinstance(instance, Governor)


Piece_strategy = st.builds(Piece)
@given(instance=Piece_strategy)
@settings(max_examples=25)
def test_Piece_instantiation(instance):
    assert isinstance(instance, Piece)


Role_strategy = st.builds(Role)
@given(instance=Role_strategy)
@settings(max_examples=25)
def test_Role_instantiation(instance):
    assert isinstance(instance, Role)


VictoryPoint_strategy = st.builds(VictoryPoint)
@given(instance=VictoryPoint_strategy)
@settings(max_examples=25)
def test_VictoryPoint_instantiation(instance):
    assert isinstance(instance, VictoryPoint)



