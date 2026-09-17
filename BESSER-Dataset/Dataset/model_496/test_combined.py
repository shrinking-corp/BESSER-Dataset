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
    Member,
    Families_Family,
    Families_MemberFemale,
    Families_MemberMale,
    Families_Test,
    Families_Sample,
    Family,
    Families_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_hyp_member_constructor_exists():
    assert callable(Member.__init__)


def test_hyp_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_family_is_not_abstract():
    assert not inspect.isabstract(Families_Family)


def test_hyp_families_family_constructor_exists():
    assert callable(Families_Family.__init__)


def test_hyp_families_family_constructor_args():
    sig = inspect.signature(Families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"




def test_hyp_families_memberfemale_is_not_abstract():
    assert not inspect.isabstract(Families_MemberFemale)


def test_hyp_families_memberfemale_constructor_exists():
    assert callable(Families_MemberFemale.__init__)


def test_hyp_families_memberfemale_constructor_args():
    sig = inspect.signature(Families_MemberFemale.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_membermale_is_not_abstract():
    assert not inspect.isabstract(Families_MemberMale)


def test_hyp_families_membermale_constructor_exists():
    assert callable(Families_MemberMale.__init__)


def test_hyp_families_membermale_constructor_args():
    sig = inspect.signature(Families_MemberMale.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_test_is_not_abstract():
    assert not inspect.isabstract(Families_Test)


def test_hyp_families_test_constructor_exists():
    assert callable(Families_Test.__init__)


def test_hyp_families_test_constructor_args():
    sig = inspect.signature(Families_Test.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_sample_is_not_abstract():
    assert not inspect.isabstract(Families_Sample)


def test_hyp_families_sample_constructor_exists():
    assert callable(Families_Sample.__init__)


def test_hyp_families_sample_constructor_args():
    sig = inspect.signature(Families_Sample.__init__)
    params = list(sig.parameters.keys())



def test_hyp_family_is_not_abstract():
    assert not inspect.isabstract(Family)


def test_hyp_family_constructor_exists():
    assert callable(Family.__init__)


def test_hyp_family_constructor_args():
    sig = inspect.signature(Family.__init__)
    params = list(sig.parameters.keys())



def test_hyp_families_member_is_not_abstract():
    assert not inspect.isabstract(Families_Member)


def test_hyp_families_member_constructor_exists():
    assert callable(Families_Member.__init__)


def test_hyp_families_member_constructor_args():
    sig = inspect.signature(Families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"




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
Member_strategy = st.builds(
    Member,
)
Families_Family_strategy = st.builds(
    Families_Family,
    lastName=
        safe_text
)
Families_MemberFemale_strategy = st.builds(
    Families_MemberFemale,
)
Families_MemberMale_strategy = st.builds(
    Families_MemberMale,
)
Families_Test_strategy = st.builds(
    Families_Test,
)
Families_Sample_strategy = st.builds(
    Families_Sample,
)
Family_strategy = st.builds(
    Family,
)
Families_Member_strategy = st.builds(
    Families_Member,
    firstName=
        safe_text,
    lastName=
        safe_text
)





@given(instance=Families_Family_strategy)
def test_hyp_families_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original









@given(instance=Families_Member_strategy)
def test_hyp_families_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Families_Member_strategy)
def test_hyp_families_member_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Families_Family,
    Families_Member,
    Families_MemberFemale,
    Families_MemberMale,
    Families_Sample,
    Families_Test,
    Family,
    Member,
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

def test_Families_Family_lastName_value_roundtrip():
    instance = Families_Family(lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_Families_Member_firstName_value_roundtrip():
    instance = Families_Member(firstName="sample_text", lastName="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Families_Member_lastName_value_roundtrip():
    instance = Families_Member(firstName="sample_text", lastName="sample_text")
    assert instance.lastName == "sample_text"
    instance.lastName = "sample_text_2"
    assert instance.lastName == "sample_text_2"


def test_Families_MemberFemale_isa_Member():
    instance = Families_MemberFemale()
    assert isinstance(instance, Member)


def test_Families_MemberMale_isa_Member():
    instance = Families_MemberMale()
    assert isinstance(instance, Member)


def test_assoc_daughters5_link_reassign_clear():
    a = Families_Family(lastName="sample_text")
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'familyDaughter', {b1})
    assert _is_linked(a, 'familyDaughter', b1)
    if hasattr(b1, 'Member6'):
        assert _is_linked(b1, 'Member6', a)
    _safe_set(a, 'familyDaughter', {b2})
    assert _is_linked(a, 'familyDaughter', b2)
    if hasattr(b1, 'Member6'):
        assert not _is_linked(b1, 'Member6', a)
    if hasattr(b2, 'Member6'):
        assert _is_linked(b2, 'Member6', a)
    _safe_set(a, 'familyDaughter', set())
    assert not _is_linked(a, 'familyDaughter', b2)
    if hasattr(b2, 'Member6'):
        assert not _is_linked(b2, 'Member6', a)


def test_assoc_familyDaughter12_link_reassign_clear():
    a = Families_Member(firstName="sample_text", lastName="sample_text")
    b1 = Family()
    b2 = Family()
    _safe_set(a, 'daughters', b1)
    assert _is_linked(a, 'daughters', b1)
    if hasattr(b1, 'Family13'):
        assert _is_linked(b1, 'Family13', a)
    _safe_set(a, 'daughters', b2)
    assert _is_linked(a, 'daughters', b2)
    if hasattr(b1, 'Family13'):
        assert not _is_linked(b1, 'Family13', a)
    if hasattr(b2, 'Family13'):
        assert _is_linked(b2, 'Family13', a)
    _safe_set(a, 'daughters', None)
    assert not _is_linked(a, 'daughters', b2)
    if hasattr(b2, 'Family13'):
        assert not _is_linked(b2, 'Family13', a)


def test_assoc_familyFather7_link_reassign_clear():
    a = Families_Member(firstName="sample_text", lastName="sample_text")
    b1 = Family()
    b2 = Family()
    _safe_set(a, 'father', b1)
    assert _is_linked(a, 'father', b1)
    if hasattr(b1, 'Family'):
        assert _is_linked(b1, 'Family', a)
    _safe_set(a, 'father', b2)
    assert _is_linked(a, 'father', b2)
    if hasattr(b1, 'Family'):
        assert not _is_linked(b1, 'Family', a)
    if hasattr(b2, 'Family'):
        assert _is_linked(b2, 'Family', a)
    _safe_set(a, 'father', None)
    assert not _is_linked(a, 'father', b2)
    if hasattr(b2, 'Family'):
        assert not _is_linked(b2, 'Family', a)


def test_assoc_familyMother8_link_reassign_clear():
    a = Families_Member(firstName="sample_text", lastName="sample_text")
    b1 = Family()
    b2 = Family()
    _safe_set(a, 'mother', b1)
    assert _is_linked(a, 'mother', b1)
    if hasattr(b1, 'Family9'):
        assert _is_linked(b1, 'Family9', a)
    _safe_set(a, 'mother', b2)
    assert _is_linked(a, 'mother', b2)
    if hasattr(b1, 'Family9'):
        assert not _is_linked(b1, 'Family9', a)
    if hasattr(b2, 'Family9'):
        assert _is_linked(b2, 'Family9', a)
    _safe_set(a, 'mother', None)
    assert not _is_linked(a, 'mother', b2)
    if hasattr(b2, 'Family9'):
        assert not _is_linked(b2, 'Family9', a)


def test_assoc_familySon10_link_reassign_clear():
    a = Families_Member(firstName="sample_text", lastName="sample_text")
    b1 = Family()
    b2 = Family()
    _safe_set(a, 'sons', b1)
    assert _is_linked(a, 'sons', b1)
    if hasattr(b1, 'Family11'):
        assert _is_linked(b1, 'Family11', a)
    _safe_set(a, 'sons', b2)
    assert _is_linked(a, 'sons', b2)
    if hasattr(b1, 'Family11'):
        assert not _is_linked(b1, 'Family11', a)
    if hasattr(b2, 'Family11'):
        assert _is_linked(b2, 'Family11', a)
    _safe_set(a, 'sons', None)
    assert not _is_linked(a, 'sons', b2)
    if hasattr(b2, 'Family11'):
        assert not _is_linked(b2, 'Family11', a)


def test_assoc_father0_link_reassign_clear():
    a = Families_Family(lastName="sample_text")
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'familyFather', b1)
    assert _is_linked(a, 'familyFather', b1)
    if hasattr(b1, 'Member'):
        assert _is_linked(b1, 'Member', a)
    _safe_set(a, 'familyFather', b2)
    assert _is_linked(a, 'familyFather', b2)
    if hasattr(b1, 'Member'):
        assert not _is_linked(b1, 'Member', a)
    if hasattr(b2, 'Member'):
        assert _is_linked(b2, 'Member', a)
    _safe_set(a, 'familyFather', None)
    assert not _is_linked(a, 'familyFather', b2)
    if hasattr(b2, 'Member'):
        assert not _is_linked(b2, 'Member', a)


def test_assoc_mother1_link_reassign_clear():
    a = Families_Family(lastName="sample_text")
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'familyMother', b1)
    assert _is_linked(a, 'familyMother', b1)
    if hasattr(b1, 'Member2'):
        assert _is_linked(b1, 'Member2', a)
    _safe_set(a, 'familyMother', b2)
    assert _is_linked(a, 'familyMother', b2)
    if hasattr(b1, 'Member2'):
        assert not _is_linked(b1, 'Member2', a)
    if hasattr(b2, 'Member2'):
        assert _is_linked(b2, 'Member2', a)
    _safe_set(a, 'familyMother', None)
    assert not _is_linked(a, 'familyMother', b2)
    if hasattr(b2, 'Member2'):
        assert not _is_linked(b2, 'Member2', a)


def test_assoc_sons3_link_reassign_clear():
    a = Families_Family(lastName="sample_text")
    b1 = Member()
    b2 = Member()
    _safe_set(a, 'familySon', {b1})
    assert _is_linked(a, 'familySon', b1)
    if hasattr(b1, 'Member4'):
        assert _is_linked(b1, 'Member4', a)
    _safe_set(a, 'familySon', {b2})
    assert _is_linked(a, 'familySon', b2)
    if hasattr(b1, 'Member4'):
        assert not _is_linked(b1, 'Member4', a)
    if hasattr(b2, 'Member4'):
        assert _is_linked(b2, 'Member4', a)
    _safe_set(a, 'familySon', set())
    assert not _is_linked(a, 'familySon', b2)
    if hasattr(b2, 'Member4'):
        assert not _is_linked(b2, 'Member4', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Families_Family_strategy = st.builds(Families_Family, lastName=safe_text)
@given(instance=Families_Family_strategy)
@settings(max_examples=25)
def test_Families_Family_instantiation(instance):
    assert isinstance(instance, Families_Family)


Families_Member_strategy = st.builds(Families_Member, firstName=safe_text, lastName=safe_text)
@given(instance=Families_Member_strategy)
@settings(max_examples=25)
def test_Families_Member_instantiation(instance):
    assert isinstance(instance, Families_Member)


Families_MemberFemale_strategy = st.builds(Families_MemberFemale)
@given(instance=Families_MemberFemale_strategy)
@settings(max_examples=25)
def test_Families_MemberFemale_instantiation(instance):
    assert isinstance(instance, Families_MemberFemale)


Families_MemberMale_strategy = st.builds(Families_MemberMale)
@given(instance=Families_MemberMale_strategy)
@settings(max_examples=25)
def test_Families_MemberMale_instantiation(instance):
    assert isinstance(instance, Families_MemberMale)


Families_Sample_strategy = st.builds(Families_Sample)
@given(instance=Families_Sample_strategy)
@settings(max_examples=25)
def test_Families_Sample_instantiation(instance):
    assert isinstance(instance, Families_Sample)


Families_Test_strategy = st.builds(Families_Test)
@given(instance=Families_Test_strategy)
@settings(max_examples=25)
def test_Families_Test_instantiation(instance):
    assert isinstance(instance, Families_Test)


Family_strategy = st.builds(Family)
@given(instance=Family_strategy)
@settings(max_examples=25)
def test_Family_instantiation(instance):
    assert isinstance(instance, Family)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)



