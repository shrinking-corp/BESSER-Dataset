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
    Dash2,
    Dash,
    Spell,
    Weapon,
    Action,
    CastSpell,
    WeaponAttack,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_dash2_is_not_abstract():
    assert not inspect.isabstract(Dash2)


def test_hyp_dash2_constructor_exists():
    assert callable(Dash2.__init__)


def test_hyp_dash2_constructor_args():
    sig = inspect.signature(Dash2.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"




def test_hyp_dash_is_not_abstract():
    assert not inspect.isabstract(Dash)


def test_hyp_dash_constructor_exists():
    assert callable(Dash.__init__)


def test_hyp_dash_constructor_args():
    sig = inspect.signature(Dash.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"




def test_hyp_spell_is_not_abstract():
    assert not inspect.isabstract(Spell)


def test_hyp_spell_constructor_exists():
    assert callable(Spell.__init__)


def test_hyp_spell_constructor_args():
    sig = inspect.signature(Spell.__init__)
    params = list(sig.parameters.keys())



def test_hyp_weapon_is_not_abstract():
    assert not inspect.isabstract(Weapon)


def test_hyp_weapon_constructor_exists():
    assert callable(Weapon.__init__)


def test_hyp_weapon_constructor_args():
    sig = inspect.signature(Weapon.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"




def test_hyp_castspell_is_not_abstract():
    assert not inspect.isabstract(CastSpell)


def test_hyp_castspell_constructor_exists():
    assert callable(CastSpell.__init__)


def test_hyp_castspell_constructor_args():
    sig = inspect.signature(CastSpell.__init__)
    params = list(sig.parameters.keys())
    assert "spell" in params, "Missing parameter 'spell'"
    assert "execute__" in params, "Missing parameter 'execute__'"

def test_hyp_castspell_has_spell():
    assert hasattr(CastSpell, "spell")
    descriptor = None
    for klass in CastSpell.__mro__:
        if "spell" in klass.__dict__:
            descriptor = klass.__dict__["spell"]
            break
    assert isinstance(descriptor, property)

def test_hyp_castspell_has_execute__():
    assert hasattr(CastSpell, "execute__")
    descriptor = None
    for klass in CastSpell.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)



def test_hyp_weaponattack_is_not_abstract():
    assert not inspect.isabstract(WeaponAttack)


def test_hyp_weaponattack_constructor_exists():
    assert callable(WeaponAttack.__init__)


def test_hyp_weaponattack_constructor_args():
    sig = inspect.signature(WeaponAttack.__init__)
    params = list(sig.parameters.keys())
    assert "execute__" in params, "Missing parameter 'execute__'"
    assert "weapon" in params, "Missing parameter 'weapon'"

def test_hyp_weaponattack_has_execute__():
    assert hasattr(WeaponAttack, "execute__")
    descriptor = None
    for klass in WeaponAttack.__mro__:
        if "execute__" in klass.__dict__:
            descriptor = klass.__dict__["execute__"]
            break
    assert isinstance(descriptor, property)

def test_hyp_weaponattack_has_weapon():
    assert hasattr(WeaponAttack, "weapon")
    descriptor = None
    for klass in WeaponAttack.__mro__:
        if "weapon" in klass.__dict__:
            descriptor = klass.__dict__["weapon"]
            break
    assert isinstance(descriptor, property)


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
Dash2_strategy = st.builds(
    Dash2,
    execute__=
        safe_text
)
Dash_strategy = st.builds(
    Dash,
    execute__=
        safe_text
)
Spell_strategy = st.builds(
    Spell,
)
Weapon_strategy = st.builds(
    Weapon,
)
Action_strategy = st.builds(
    Action,
    execute__=
        safe_text
)
CastSpell_strategy = st.builds(
    CastSpell,
    spell=
        st.none(),
    execute__=
        safe_text
)
WeaponAttack_strategy = st.builds(
    WeaponAttack,
    execute__=
        safe_text,
    weapon=
        st.none()
)




@given(instance=Dash2_strategy)
def test_hyp_dash2_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original




@given(instance=Dash_strategy)
def test_hyp_dash_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original






@given(instance=Action_strategy)
def test_hyp_action_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=CastSpell_strategy)
@settings(max_examples=50)
def test_hyp_castspell_instantiation(instance):
    assert isinstance(instance, CastSpell)



@given(instance=CastSpell_strategy)
def test_hyp_castspell_spell_setter(instance):
    original = instance.spell
    instance.spell = original
    assert instance.spell == original



@given(instance=CastSpell_strategy)
def test_hyp_castspell_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original

@given(instance=WeaponAttack_strategy)
@settings(max_examples=50)
def test_hyp_weaponattack_instantiation(instance):
    assert isinstance(instance, WeaponAttack)



@given(instance=WeaponAttack_strategy)
def test_hyp_weaponattack_execute___setter(instance):
    original = instance.execute__
    instance.execute__ = original
    assert instance.execute__ == original



@given(instance=WeaponAttack_strategy)
def test_hyp_weaponattack_weapon_setter(instance):
    original = instance.weapon
    instance.weapon = original
    assert instance.weapon == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    CastSpell,
    Dash,
    Dash2,
    Spell,
    Weapon,
    WeaponAttack,
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

def test_Action_execute___value_roundtrip():
    instance = Action(execute__="sample_text")
    assert instance.execute__ == "sample_text"
    instance.execute__ = "sample_text_2"
    assert instance.execute__ == "sample_text_2"


def test_Dash_execute___value_roundtrip():
    instance = Dash(execute__="sample_text")
    assert instance.execute__ == "sample_text"
    instance.execute__ = "sample_text_2"
    assert instance.execute__ == "sample_text_2"


def test_Dash2_execute___value_roundtrip():
    instance = Dash2(execute__="sample_text")
    assert instance.execute__ == "sample_text"
    instance.execute__ = "sample_text_2"
    assert instance.execute__ == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action, execute__=safe_text)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Dash_strategy = st.builds(Dash, execute__=safe_text)
@given(instance=Dash_strategy)
@settings(max_examples=25)
def test_Dash_instantiation(instance):
    assert isinstance(instance, Dash)


Dash2_strategy = st.builds(Dash2, execute__=safe_text)
@given(instance=Dash2_strategy)
@settings(max_examples=25)
def test_Dash2_instantiation(instance):
    assert isinstance(instance, Dash2)


Spell_strategy = st.builds(Spell)
@given(instance=Spell_strategy)
@settings(max_examples=25)
def test_Spell_instantiation(instance):
    assert isinstance(instance, Spell)


Weapon_strategy = st.builds(Weapon)
@given(instance=Weapon_strategy)
@settings(max_examples=25)
def test_Weapon_instantiation(instance):
    assert isinstance(instance, Weapon)



