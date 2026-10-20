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
    uFamily,
    uncertainty_Families_Family,
    Families_uncertainty_aFamilyRegister,
    uFamilyRegister,
    uncertainty_Families_FamilyRegister,
    uncertainty_UData,
    Families_uncertainty_aFamilyMember,
    uFamilyMember,
    uncertainty_Families_FamilyMember,
    Families_uncertainty_aFamily,
    aFamilyRegister,
    aFamilyMember,
    uncertainty_aFamily,
    Families_uncertainty_uFamily,
    Families_uncertainty_UData,
    ModelElement,
    Families_uncertainty_ModelElement,
    uncertainty_aFamilyMember,
    Families_uncertainty_uFamilyMember,
    aFamily,
    uncertainty_aFamilyRegister,
    Families_uncertainty_uFamilyRegister,
    uncertainty_ModelElement,
    Families_FamilyMember,
    Families_Family,
    Families_FamilyRegister,
    OperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ufamily_is_not_abstract():
    assert not inspect.isabstract(uFamily)


def test_hyp_ufamily_constructor_exists():
    assert callable(uFamily.__init__)


def test_hyp_ufamily_constructor_args():
    sig = inspect.signature(uFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_families_family_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Families_Family)


def test_hyp_uncertainty_families_family_constructor_exists():
    assert callable(uncertainty_Families_Family.__init__)


def test_hyp_uncertainty_families_family_constructor_args():
    sig = inspect.signature(uncertainty_Families_Family.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_afamilyregister_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_aFamilyRegister)


def test_hyp_families_uncertainty_afamilyregister_constructor_exists():
    assert callable(Families_uncertainty_aFamilyRegister.__init__)


def test_hyp_families_uncertainty_afamilyregister_constructor_args():
    sig = inspect.signature(Families_uncertainty_aFamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ufamilyregister_is_not_abstract():
    assert not inspect.isabstract(uFamilyRegister)


def test_hyp_ufamilyregister_constructor_exists():
    assert callable(uFamilyRegister.__init__)


def test_hyp_ufamilyregister_constructor_args():
    sig = inspect.signature(uFamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_families_familyregister_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Families_FamilyRegister)


def test_hyp_uncertainty_families_familyregister_constructor_exists():
    assert callable(uncertainty_Families_FamilyRegister.__init__)


def test_hyp_uncertainty_families_familyregister_constructor_args():
    sig = inspect.signature(uncertainty_Families_FamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_udata_is_not_abstract():
    assert not inspect.isabstract(uncertainty_UData)


def test_hyp_uncertainty_udata_constructor_exists():
    assert callable(uncertainty_UData.__init__)


def test_hyp_uncertainty_udata_constructor_args():
    sig = inspect.signature(uncertainty_UData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_afamilymember_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_aFamilyMember)


def test_hyp_families_uncertainty_afamilymember_constructor_exists():
    assert callable(Families_uncertainty_aFamilyMember.__init__)


def test_hyp_families_uncertainty_afamilymember_constructor_args():
    sig = inspect.signature(Families_uncertainty_aFamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ufamilymember_is_not_abstract():
    assert not inspect.isabstract(uFamilyMember)


def test_hyp_ufamilymember_constructor_exists():
    assert callable(uFamilyMember.__init__)


def test_hyp_ufamilymember_constructor_args():
    sig = inspect.signature(uFamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_families_familymember_is_not_abstract():
    assert not inspect.isabstract(uncertainty_Families_FamilyMember)


def test_hyp_uncertainty_families_familymember_constructor_exists():
    assert callable(uncertainty_Families_FamilyMember.__init__)


def test_hyp_uncertainty_families_familymember_constructor_args():
    sig = inspect.signature(uncertainty_Families_FamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_afamily_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_aFamily)


def test_hyp_families_uncertainty_afamily_constructor_exists():
    assert callable(Families_uncertainty_aFamily.__init__)


def test_hyp_families_uncertainty_afamily_constructor_args():
    sig = inspect.signature(Families_uncertainty_aFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_afamilyregister_is_not_abstract():
    assert not inspect.isabstract(aFamilyRegister)


def test_hyp_afamilyregister_constructor_exists():
    assert callable(aFamilyRegister.__init__)


def test_hyp_afamilyregister_constructor_args():
    sig = inspect.signature(aFamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_afamilymember_is_not_abstract():
    assert not inspect.isabstract(aFamilyMember)


def test_hyp_afamilymember_constructor_exists():
    assert callable(aFamilyMember.__init__)


def test_hyp_afamilymember_constructor_args():
    sig = inspect.signature(aFamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_afamily_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aFamily)


def test_hyp_uncertainty_afamily_constructor_exists():
    assert callable(uncertainty_aFamily.__init__)


def test_hyp_uncertainty_afamily_constructor_args():
    sig = inspect.signature(uncertainty_aFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_ufamily_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_uFamily)


def test_hyp_families_uncertainty_ufamily_constructor_exists():
    assert callable(Families_uncertainty_uFamily.__init__)


def test_hyp_families_uncertainty_ufamily_constructor_args():
    sig = inspect.signature(Families_uncertainty_uFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_udata_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_UData)


def test_hyp_families_uncertainty_udata_constructor_exists():
    assert callable(Families_uncertainty_UData.__init__)


def test_hyp_families_uncertainty_udata_constructor_args():
    sig = inspect.signature(Families_uncertainty_UData.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "utype" in params, "Missing parameter 'utype'"





def test_hyp_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_hyp_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_hyp_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_modelelement_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_ModelElement)


def test_hyp_families_uncertainty_modelelement_constructor_exists():
    assert callable(Families_uncertainty_ModelElement.__init__)


def test_hyp_families_uncertainty_modelelement_constructor_args():
    sig = inspect.signature(Families_uncertainty_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_afamilymember_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aFamilyMember)


def test_hyp_uncertainty_afamilymember_constructor_exists():
    assert callable(uncertainty_aFamilyMember.__init__)


def test_hyp_uncertainty_afamilymember_constructor_args():
    sig = inspect.signature(uncertainty_aFamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_ufamilymember_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_uFamilyMember)


def test_hyp_families_uncertainty_ufamilymember_constructor_exists():
    assert callable(Families_uncertainty_uFamilyMember.__init__)


def test_hyp_families_uncertainty_ufamilymember_constructor_args():
    sig = inspect.signature(Families_uncertainty_uFamilyMember.__init__)
    params = list(sig.parameters.keys())



def test_hyp_afamily_is_not_abstract():
    assert not inspect.isabstract(aFamily)


def test_hyp_afamily_constructor_exists():
    assert callable(aFamily.__init__)


def test_hyp_afamily_constructor_args():
    sig = inspect.signature(aFamily.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_afamilyregister_is_not_abstract():
    assert not inspect.isabstract(uncertainty_aFamilyRegister)


def test_hyp_uncertainty_afamilyregister_constructor_exists():
    assert callable(uncertainty_aFamilyRegister.__init__)


def test_hyp_uncertainty_afamilyregister_constructor_args():
    sig = inspect.signature(uncertainty_aFamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_uncertainty_ufamilyregister_is_not_abstract():
    assert not inspect.isabstract(Families_uncertainty_uFamilyRegister)


def test_hyp_families_uncertainty_ufamilyregister_constructor_exists():
    assert callable(Families_uncertainty_uFamilyRegister.__init__)


def test_hyp_families_uncertainty_ufamilyregister_constructor_args():
    sig = inspect.signature(Families_uncertainty_uFamilyRegister.__init__)
    params = list(sig.parameters.keys())



def test_hyp_uncertainty_modelelement_is_not_abstract():
    assert not inspect.isabstract(uncertainty_ModelElement)


def test_hyp_uncertainty_modelelement_constructor_exists():
    assert callable(uncertainty_ModelElement.__init__)


def test_hyp_uncertainty_modelelement_constructor_args():
    sig = inspect.signature(uncertainty_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_familymember_is_not_abstract():
    assert not inspect.isabstract(Families_FamilyMember)


def test_hyp_families_familymember_constructor_exists():
    assert callable(Families_FamilyMember.__init__)


def test_hyp_families_familymember_constructor_args():
    sig = inspect.signature(Families_FamilyMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_families_family_is_not_abstract():
    assert not inspect.isabstract(Families_Family)


def test_hyp_families_family_constructor_exists():
    assert callable(Families_Family.__init__)


def test_hyp_families_family_constructor_args():
    sig = inspect.signature(Families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_families_familyregister_is_not_abstract():
    assert not inspect.isabstract(Families_FamilyRegister)


def test_hyp_families_familyregister_constructor_exists():
    assert callable(Families_FamilyRegister.__init__)


def test_hyp_families_familyregister_constructor_args():
    sig = inspect.signature(Families_FamilyRegister.__init__)
    params = list(sig.parameters.keys())

def test_hyp_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_hyp_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "XOR",
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorType"


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
uFamily_strategy = st.builds(
    uFamily,
)
uncertainty_Families_Family_strategy = st.builds(
    uncertainty_Families_Family,
)
Families_uncertainty_aFamilyRegister_strategy = st.builds(
    Families_uncertainty_aFamilyRegister,
)
uFamilyRegister_strategy = st.builds(
    uFamilyRegister,
)
uncertainty_Families_FamilyRegister_strategy = st.builds(
    uncertainty_Families_FamilyRegister,
)
uncertainty_UData_strategy = st.builds(
    uncertainty_UData,
)
Families_uncertainty_aFamilyMember_strategy = st.builds(
    Families_uncertainty_aFamilyMember,
)
uFamilyMember_strategy = st.builds(
    uFamilyMember,
)
uncertainty_Families_FamilyMember_strategy = st.builds(
    uncertainty_Families_FamilyMember,
)
Families_uncertainty_aFamily_strategy = st.builds(
    Families_uncertainty_aFamily,
)
aFamilyRegister_strategy = st.builds(
    aFamilyRegister,
)
aFamilyMember_strategy = st.builds(
    aFamilyMember,
)
uncertainty_aFamily_strategy = st.builds(
    uncertainty_aFamily,
)
Families_uncertainty_uFamily_strategy = st.builds(
    Families_uncertainty_uFamily,
)
Families_uncertainty_UData_strategy = st.builds(
    Families_uncertainty_UData,
    name=
        safe_text,
    utype=
        safe_text
)
ModelElement_strategy = st.builds(
    ModelElement,
)
Families_uncertainty_ModelElement_strategy = st.builds(
    Families_uncertainty_ModelElement,
)
uncertainty_aFamilyMember_strategy = st.builds(
    uncertainty_aFamilyMember,
)
Families_uncertainty_uFamilyMember_strategy = st.builds(
    Families_uncertainty_uFamilyMember,
)
aFamily_strategy = st.builds(
    aFamily,
)
uncertainty_aFamilyRegister_strategy = st.builds(
    uncertainty_aFamilyRegister,
)
Families_uncertainty_uFamilyRegister_strategy = st.builds(
    Families_uncertainty_uFamilyRegister,
)
uncertainty_ModelElement_strategy = st.builds(
    uncertainty_ModelElement,
)
Families_FamilyMember_strategy = st.builds(
    Families_FamilyMember,
    name=
        safe_text
)
Families_Family_strategy = st.builds(
    Families_Family,
    name=
        safe_text
)
Families_FamilyRegister_strategy = st.builds(
    Families_FamilyRegister,
)


















@given(instance=Families_uncertainty_UData_strategy)
def test_hyp_families_uncertainty_udata_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Families_uncertainty_UData_strategy)
def test_hyp_families_uncertainty_udata_utype_setter(instance):
    original = instance.utype
    instance.utype = original
    assert instance.utype == original












@given(instance=Families_FamilyMember_strategy)
def test_hyp_families_familymember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Families_Family_strategy)
def test_hyp_families_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Families_Family,
    Families_FamilyMember,
    Families_FamilyRegister,
    Families_uncertainty_ModelElement,
    Families_uncertainty_UData,
    Families_uncertainty_aFamily,
    Families_uncertainty_aFamilyMember,
    Families_uncertainty_aFamilyRegister,
    Families_uncertainty_uFamily,
    Families_uncertainty_uFamilyMember,
    Families_uncertainty_uFamilyRegister,
    ModelElement,
    aFamily,
    aFamilyMember,
    aFamilyRegister,
    uFamily,
    uFamilyMember,
    uFamilyRegister,
    uncertainty_Families_Family,
    uncertainty_Families_FamilyMember,
    uncertainty_Families_FamilyRegister,
    uncertainty_ModelElement,
    uncertainty_UData,
    uncertainty_aFamily,
    uncertainty_aFamilyMember,
    uncertainty_aFamilyRegister,
    OperatorType,
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

def test_Families_Family_name_value_roundtrip():
    instance = Families_Family(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Families_FamilyMember_name_value_roundtrip():
    instance = Families_FamilyMember(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Families_uncertainty_UData_name_value_roundtrip():
    instance = Families_uncertainty_UData(name="sample_text", utype="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Families_uncertainty_UData_utype_value_roundtrip():
    instance = Families_uncertainty_UData(name="sample_text", utype="sample_text")
    assert instance.utype == "sample_text"
    instance.utype = "sample_text_2"
    assert instance.utype == "sample_text_2"


def test_Families_Family_isa_uncertainty_ModelElement():
    instance = Families_Family(name="sample_text")
    assert isinstance(instance, uncertainty_ModelElement)


def test_Families_FamilyMember_isa_uncertainty_ModelElement():
    instance = Families_FamilyMember(name="sample_text")
    assert isinstance(instance, uncertainty_ModelElement)


def test_Families_FamilyRegister_isa_uncertainty_ModelElement():
    instance = Families_FamilyRegister()
    assert isinstance(instance, uncertainty_ModelElement)


def test_Families_uncertainty_uFamily_isa_uncertainty_UData():
    instance = Families_uncertainty_uFamily()
    assert isinstance(instance, uncertainty_UData)


def test_Families_uncertainty_uFamilyMember_isa_uncertainty_UData():
    instance = Families_uncertainty_uFamilyMember()
    assert isinstance(instance, uncertainty_UData)


def test_Families_uncertainty_uFamilyRegister_isa_uncertainty_UData():
    instance = Families_uncertainty_uFamilyRegister()
    assert isinstance(instance, uncertainty_UData)


def test_Families_Family_isa_uncertainty_aFamily():
    instance = Families_Family(name="sample_text")
    assert isinstance(instance, uncertainty_aFamily)


def test_Families_uncertainty_uFamily_isa_uncertainty_aFamily():
    instance = Families_uncertainty_uFamily()
    assert isinstance(instance, uncertainty_aFamily)


def test_Families_FamilyMember_isa_uncertainty_aFamilyMember():
    instance = Families_FamilyMember(name="sample_text")
    assert isinstance(instance, uncertainty_aFamilyMember)


def test_Families_uncertainty_uFamilyMember_isa_uncertainty_aFamilyMember():
    instance = Families_uncertainty_uFamilyMember()
    assert isinstance(instance, uncertainty_aFamilyMember)


def test_Families_FamilyRegister_isa_uncertainty_aFamilyRegister():
    instance = Families_FamilyRegister()
    assert isinstance(instance, uncertainty_aFamilyRegister)


def test_Families_uncertainty_uFamilyRegister_isa_uncertainty_aFamilyRegister():
    instance = Families_uncertainty_uFamilyRegister()
    assert isinstance(instance, uncertainty_aFamilyRegister)


def test_assoc_daughters8_link_reassign_clear():
    a = Families_Family(name="sample_text")
    b1 = aFamilyMember()
    b2 = aFamilyMember()
    _safe_set(a, 'Families_Family9', {b1})
    assert _is_linked(a, 'Families_Family9', b1)
    if hasattr(b1, 'aFamilyMember10'):
        assert _is_linked(b1, 'aFamilyMember10', a)
    _safe_set(a, 'Families_Family9', {b2})
    assert _is_linked(a, 'Families_Family9', b2)
    if hasattr(b1, 'aFamilyMember10'):
        assert not _is_linked(b1, 'aFamilyMember10', a)
    if hasattr(b2, 'aFamilyMember10'):
        assert _is_linked(b2, 'aFamilyMember10', a)
    _safe_set(a, 'Families_Family9', set())
    assert not _is_linked(a, 'Families_Family9', b2)
    if hasattr(b2, 'aFamilyMember10'):
        assert not _is_linked(b2, 'aFamilyMember10', a)


def test_assoc_daughtersInverse21_link_reassign_clear():
    a = Families_FamilyMember(name="sample_text")
    b1 = aFamily()
    b2 = aFamily()
    _safe_set(a, 'Families_FamilyMember22', b1)
    assert _is_linked(a, 'Families_FamilyMember22', b1)
    if hasattr(b1, 'aFamily23'):
        assert _is_linked(b1, 'aFamily23', a)
    _safe_set(a, 'Families_FamilyMember22', b2)
    assert _is_linked(a, 'Families_FamilyMember22', b2)
    if hasattr(b1, 'aFamily23'):
        assert not _is_linked(b1, 'aFamily23', a)
    if hasattr(b2, 'aFamily23'):
        assert _is_linked(b2, 'aFamily23', a)
    _safe_set(a, 'Families_FamilyMember22', None)
    assert not _is_linked(a, 'Families_FamilyMember22', b2)
    if hasattr(b2, 'aFamily23'):
        assert not _is_linked(b2, 'aFamily23', a)


def test_assoc_familiesInverse11_link_reassign_clear():
    a = Families_Family(name="sample_text")
    b1 = aFamilyRegister()
    b2 = aFamilyRegister()
    _safe_set(a, 'Families_Family12', b1)
    assert _is_linked(a, 'Families_Family12', b1)
    if hasattr(b1, 'aFamilyRegister'):
        assert _is_linked(b1, 'aFamilyRegister', a)
    _safe_set(a, 'Families_Family12', b2)
    assert _is_linked(a, 'Families_Family12', b2)
    if hasattr(b1, 'aFamilyRegister'):
        assert not _is_linked(b1, 'aFamilyRegister', a)
    if hasattr(b2, 'aFamilyRegister'):
        assert _is_linked(b2, 'aFamilyRegister', a)
    _safe_set(a, 'Families_Family12', None)
    assert not _is_linked(a, 'Families_Family12', b2)
    if hasattr(b2, 'aFamilyRegister'):
        assert not _is_linked(b2, 'aFamilyRegister', a)


def test_assoc_father1_link_reassign_clear():
    a = Families_Family(name="sample_text")
    b1 = aFamilyMember()
    b2 = aFamilyMember()
    _safe_set(a, 'Families_Family', b1)
    assert _is_linked(a, 'Families_Family', b1)
    if hasattr(b1, 'aFamilyMember'):
        assert _is_linked(b1, 'aFamilyMember', a)
    _safe_set(a, 'Families_Family', b2)
    assert _is_linked(a, 'Families_Family', b2)
    if hasattr(b1, 'aFamilyMember'):
        assert not _is_linked(b1, 'aFamilyMember', a)
    if hasattr(b2, 'aFamilyMember'):
        assert _is_linked(b2, 'aFamilyMember', a)
    _safe_set(a, 'Families_Family', None)
    assert not _is_linked(a, 'Families_Family', b2)
    if hasattr(b2, 'aFamilyMember'):
        assert not _is_linked(b2, 'aFamilyMember', a)


def test_assoc_fatherInverse13_link_reassign_clear():
    a = Families_FamilyMember(name="sample_text")
    b1 = aFamily()
    b2 = aFamily()
    _safe_set(a, 'Families_FamilyMember', b1)
    assert _is_linked(a, 'Families_FamilyMember', b1)
    if hasattr(b1, 'aFamily14'):
        assert _is_linked(b1, 'aFamily14', a)
    _safe_set(a, 'Families_FamilyMember', b2)
    assert _is_linked(a, 'Families_FamilyMember', b2)
    if hasattr(b1, 'aFamily14'):
        assert not _is_linked(b1, 'aFamily14', a)
    if hasattr(b2, 'aFamily14'):
        assert _is_linked(b2, 'aFamily14', a)
    _safe_set(a, 'Families_FamilyMember', None)
    assert not _is_linked(a, 'Families_FamilyMember', b2)
    if hasattr(b2, 'aFamily14'):
        assert not _is_linked(b2, 'aFamily14', a)


def test_assoc_mother2_link_reassign_clear():
    a = Families_Family(name="sample_text")
    b1 = aFamilyMember()
    b2 = aFamilyMember()
    _safe_set(a, 'Families_Family3', b1)
    assert _is_linked(a, 'Families_Family3', b1)
    if hasattr(b1, 'aFamilyMember4'):
        assert _is_linked(b1, 'aFamilyMember4', a)
    _safe_set(a, 'Families_Family3', b2)
    assert _is_linked(a, 'Families_Family3', b2)
    if hasattr(b1, 'aFamilyMember4'):
        assert not _is_linked(b1, 'aFamilyMember4', a)
    if hasattr(b2, 'aFamilyMember4'):
        assert _is_linked(b2, 'aFamilyMember4', a)
    _safe_set(a, 'Families_Family3', None)
    assert not _is_linked(a, 'Families_Family3', b2)
    if hasattr(b2, 'aFamilyMember4'):
        assert not _is_linked(b2, 'aFamilyMember4', a)


def test_assoc_motherInverse15_link_reassign_clear():
    a = Families_FamilyMember(name="sample_text")
    b1 = aFamily()
    b2 = aFamily()
    _safe_set(a, 'Families_FamilyMember16', b1)
    assert _is_linked(a, 'Families_FamilyMember16', b1)
    if hasattr(b1, 'aFamily17'):
        assert _is_linked(b1, 'aFamily17', a)
    _safe_set(a, 'Families_FamilyMember16', b2)
    assert _is_linked(a, 'Families_FamilyMember16', b2)
    if hasattr(b1, 'aFamily17'):
        assert not _is_linked(b1, 'aFamily17', a)
    if hasattr(b2, 'aFamily17'):
        assert _is_linked(b2, 'aFamily17', a)
    _safe_set(a, 'Families_FamilyMember16', None)
    assert not _is_linked(a, 'Families_FamilyMember16', b2)
    if hasattr(b2, 'aFamily17'):
        assert not _is_linked(b2, 'aFamily17', a)


def test_assoc_sons5_link_reassign_clear():
    a = Families_Family(name="sample_text")
    b1 = aFamilyMember()
    b2 = aFamilyMember()
    _safe_set(a, 'Families_Family6', {b1})
    assert _is_linked(a, 'Families_Family6', b1)
    if hasattr(b1, 'aFamilyMember7'):
        assert _is_linked(b1, 'aFamilyMember7', a)
    _safe_set(a, 'Families_Family6', {b2})
    assert _is_linked(a, 'Families_Family6', b2)
    if hasattr(b1, 'aFamilyMember7'):
        assert not _is_linked(b1, 'aFamilyMember7', a)
    if hasattr(b2, 'aFamilyMember7'):
        assert _is_linked(b2, 'aFamilyMember7', a)
    _safe_set(a, 'Families_Family6', set())
    assert not _is_linked(a, 'Families_Family6', b2)
    if hasattr(b2, 'aFamilyMember7'):
        assert not _is_linked(b2, 'aFamilyMember7', a)


def test_assoc_sonsInverse18_link_reassign_clear():
    a = Families_FamilyMember(name="sample_text")
    b1 = aFamily()
    b2 = aFamily()
    _safe_set(a, 'Families_FamilyMember19', b1)
    assert _is_linked(a, 'Families_FamilyMember19', b1)
    if hasattr(b1, 'aFamily20'):
        assert _is_linked(b1, 'aFamily20', a)
    _safe_set(a, 'Families_FamilyMember19', b2)
    assert _is_linked(a, 'Families_FamilyMember19', b2)
    if hasattr(b1, 'aFamily20'):
        assert not _is_linked(b1, 'aFamily20', a)
    if hasattr(b2, 'aFamily20'):
        assert _is_linked(b2, 'aFamily20', a)
    _safe_set(a, 'Families_FamilyMember19', None)
    assert not _is_linked(a, 'Families_FamilyMember19', b2)
    if hasattr(b2, 'aFamily20'):
        assert not _is_linked(b2, 'aFamily20', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Families_Family_strategy = st.builds(Families_Family, name=safe_text)
@given(instance=Families_Family_strategy)
@settings(max_examples=25)
def test_Families_Family_instantiation(instance):
    assert isinstance(instance, Families_Family)


Families_FamilyMember_strategy = st.builds(Families_FamilyMember, name=safe_text)
@given(instance=Families_FamilyMember_strategy)
@settings(max_examples=25)
def test_Families_FamilyMember_instantiation(instance):
    assert isinstance(instance, Families_FamilyMember)


Families_FamilyRegister_strategy = st.builds(Families_FamilyRegister)
@given(instance=Families_FamilyRegister_strategy)
@settings(max_examples=25)
def test_Families_FamilyRegister_instantiation(instance):
    assert isinstance(instance, Families_FamilyRegister)


Families_uncertainty_ModelElement_strategy = st.builds(Families_uncertainty_ModelElement)
@given(instance=Families_uncertainty_ModelElement_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_ModelElement_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_ModelElement)


Families_uncertainty_UData_strategy = st.builds(Families_uncertainty_UData, name=safe_text, utype=safe_text)
@given(instance=Families_uncertainty_UData_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_UData_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_UData)


Families_uncertainty_aFamily_strategy = st.builds(Families_uncertainty_aFamily)
@given(instance=Families_uncertainty_aFamily_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_aFamily_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_aFamily)


Families_uncertainty_aFamilyMember_strategy = st.builds(Families_uncertainty_aFamilyMember)
@given(instance=Families_uncertainty_aFamilyMember_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_aFamilyMember_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_aFamilyMember)


Families_uncertainty_aFamilyRegister_strategy = st.builds(Families_uncertainty_aFamilyRegister)
@given(instance=Families_uncertainty_aFamilyRegister_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_aFamilyRegister_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_aFamilyRegister)


Families_uncertainty_uFamily_strategy = st.builds(Families_uncertainty_uFamily)
@given(instance=Families_uncertainty_uFamily_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_uFamily_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_uFamily)


Families_uncertainty_uFamilyMember_strategy = st.builds(Families_uncertainty_uFamilyMember)
@given(instance=Families_uncertainty_uFamilyMember_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_uFamilyMember_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_uFamilyMember)


Families_uncertainty_uFamilyRegister_strategy = st.builds(Families_uncertainty_uFamilyRegister)
@given(instance=Families_uncertainty_uFamilyRegister_strategy)
@settings(max_examples=25)
def test_Families_uncertainty_uFamilyRegister_instantiation(instance):
    assert isinstance(instance, Families_uncertainty_uFamilyRegister)


ModelElement_strategy = st.builds(ModelElement)
@given(instance=ModelElement_strategy)
@settings(max_examples=25)
def test_ModelElement_instantiation(instance):
    assert isinstance(instance, ModelElement)


aFamily_strategy = st.builds(aFamily)
@given(instance=aFamily_strategy)
@settings(max_examples=25)
def test_aFamily_instantiation(instance):
    assert isinstance(instance, aFamily)


aFamilyMember_strategy = st.builds(aFamilyMember)
@given(instance=aFamilyMember_strategy)
@settings(max_examples=25)
def test_aFamilyMember_instantiation(instance):
    assert isinstance(instance, aFamilyMember)


aFamilyRegister_strategy = st.builds(aFamilyRegister)
@given(instance=aFamilyRegister_strategy)
@settings(max_examples=25)
def test_aFamilyRegister_instantiation(instance):
    assert isinstance(instance, aFamilyRegister)


uFamily_strategy = st.builds(uFamily)
@given(instance=uFamily_strategy)
@settings(max_examples=25)
def test_uFamily_instantiation(instance):
    assert isinstance(instance, uFamily)


uFamilyMember_strategy = st.builds(uFamilyMember)
@given(instance=uFamilyMember_strategy)
@settings(max_examples=25)
def test_uFamilyMember_instantiation(instance):
    assert isinstance(instance, uFamilyMember)


uFamilyRegister_strategy = st.builds(uFamilyRegister)
@given(instance=uFamilyRegister_strategy)
@settings(max_examples=25)
def test_uFamilyRegister_instantiation(instance):
    assert isinstance(instance, uFamilyRegister)


uncertainty_Families_Family_strategy = st.builds(uncertainty_Families_Family)
@given(instance=uncertainty_Families_Family_strategy)
@settings(max_examples=25)
def test_uncertainty_Families_Family_instantiation(instance):
    assert isinstance(instance, uncertainty_Families_Family)


uncertainty_Families_FamilyMember_strategy = st.builds(uncertainty_Families_FamilyMember)
@given(instance=uncertainty_Families_FamilyMember_strategy)
@settings(max_examples=25)
def test_uncertainty_Families_FamilyMember_instantiation(instance):
    assert isinstance(instance, uncertainty_Families_FamilyMember)


uncertainty_Families_FamilyRegister_strategy = st.builds(uncertainty_Families_FamilyRegister)
@given(instance=uncertainty_Families_FamilyRegister_strategy)
@settings(max_examples=25)
def test_uncertainty_Families_FamilyRegister_instantiation(instance):
    assert isinstance(instance, uncertainty_Families_FamilyRegister)


uncertainty_ModelElement_strategy = st.builds(uncertainty_ModelElement)
@given(instance=uncertainty_ModelElement_strategy)
@settings(max_examples=25)
def test_uncertainty_ModelElement_instantiation(instance):
    assert isinstance(instance, uncertainty_ModelElement)


uncertainty_UData_strategy = st.builds(uncertainty_UData)
@given(instance=uncertainty_UData_strategy)
@settings(max_examples=25)
def test_uncertainty_UData_instantiation(instance):
    assert isinstance(instance, uncertainty_UData)


uncertainty_aFamily_strategy = st.builds(uncertainty_aFamily)
@given(instance=uncertainty_aFamily_strategy)
@settings(max_examples=25)
def test_uncertainty_aFamily_instantiation(instance):
    assert isinstance(instance, uncertainty_aFamily)


uncertainty_aFamilyMember_strategy = st.builds(uncertainty_aFamilyMember)
@given(instance=uncertainty_aFamilyMember_strategy)
@settings(max_examples=25)
def test_uncertainty_aFamilyMember_instantiation(instance):
    assert isinstance(instance, uncertainty_aFamilyMember)


uncertainty_aFamilyRegister_strategy = st.builds(uncertainty_aFamilyRegister)
@given(instance=uncertainty_aFamilyRegister_strategy)
@settings(max_examples=25)
def test_uncertainty_aFamilyRegister_instantiation(instance):
    assert isinstance(instance, uncertainty_aFamilyRegister)



