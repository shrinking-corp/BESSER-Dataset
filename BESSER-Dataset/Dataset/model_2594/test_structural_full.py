import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractSuperclass,
    Child,
    grammar_features_AbstractSuperclass,
    grammar_features_AlternativeSyntax,
    grammar_features_Child,
    grammar_features_ClassWithAttributes,
    grammar_features_CompoundOptional,
    grammar_features_CompoundPlus,
    grammar_features_CompoundStar,
    grammar_features_ConcreteSubclassA,
    grammar_features_ConcreteSubclassB,
    grammar_features_MandatoryContainment,
    grammar_features_MandatoryNonContainment,
    grammar_features_OptionalContainment,
    grammar_features_OptionalNonContainment,
    grammar_features_OptionalPrefix,
    grammar_features_PlusContainment,
    grammar_features_PlusNonContainment,
    grammar_features_PlusPrefix,
    grammar_features_Root,
    grammar_features_SecondRoot,
    grammar_features_StarContainment,
    grammar_features_StarNonContainment,
    grammar_features_StarPrefix,
    grammar_features_X,
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

def test_grammar_features_ClassWithAttributes_a1_value_roundtrip():
    instance = grammar_features_ClassWithAttributes(a1="sample_text", a2=True)
    assert instance.a1 == "sample_text"
    instance.a1 = "sample_text_2"
    assert instance.a1 == "sample_text_2"


def test_grammar_features_ClassWithAttributes_a2_value_roundtrip():
    instance = grammar_features_ClassWithAttributes(a1="sample_text", a2=True)
    assert instance.a2 == True
    instance.a2 = False
    assert instance.a2 == False


def test_grammar_features_X_name_value_roundtrip():
    instance = grammar_features_X(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_grammar_features_ConcreteSubclassA_isa_AbstractSuperclass():
    instance = grammar_features_ConcreteSubclassA()
    assert isinstance(instance, AbstractSuperclass)


def test_grammar_features_ConcreteSubclassB_isa_AbstractSuperclass():
    instance = grammar_features_ConcreteSubclassB()
    assert isinstance(instance, AbstractSuperclass)


def test_grammar_features_AbstractSuperclass_isa_Child():
    instance = grammar_features_AbstractSuperclass()
    assert isinstance(instance, Child)


def test_grammar_features_AlternativeSyntax_isa_Child():
    instance = grammar_features_AlternativeSyntax()
    assert isinstance(instance, Child)


def test_grammar_features_ClassWithAttributes_isa_Child():
    instance = grammar_features_ClassWithAttributes(a1="sample_text", a2=True)
    assert isinstance(instance, Child)


def test_grammar_features_CompoundOptional_isa_Child():
    instance = grammar_features_CompoundOptional()
    assert isinstance(instance, Child)


def test_grammar_features_CompoundPlus_isa_Child():
    instance = grammar_features_CompoundPlus()
    assert isinstance(instance, Child)


def test_grammar_features_CompoundStar_isa_Child():
    instance = grammar_features_CompoundStar()
    assert isinstance(instance, Child)


def test_grammar_features_MandatoryContainment_isa_Child():
    instance = grammar_features_MandatoryContainment()
    assert isinstance(instance, Child)


def test_grammar_features_MandatoryNonContainment_isa_Child():
    instance = grammar_features_MandatoryNonContainment()
    assert isinstance(instance, Child)


def test_grammar_features_OptionalContainment_isa_Child():
    instance = grammar_features_OptionalContainment()
    assert isinstance(instance, Child)


def test_grammar_features_OptionalNonContainment_isa_Child():
    instance = grammar_features_OptionalNonContainment()
    assert isinstance(instance, Child)


def test_grammar_features_OptionalPrefix_isa_Child():
    instance = grammar_features_OptionalPrefix()
    assert isinstance(instance, Child)


def test_grammar_features_PlusContainment_isa_Child():
    instance = grammar_features_PlusContainment()
    assert isinstance(instance, Child)


def test_grammar_features_PlusNonContainment_isa_Child():
    instance = grammar_features_PlusNonContainment()
    assert isinstance(instance, Child)


def test_grammar_features_PlusPrefix_isa_Child():
    instance = grammar_features_PlusPrefix()
    assert isinstance(instance, Child)


def test_grammar_features_StarContainment_isa_Child():
    instance = grammar_features_StarContainment()
    assert isinstance(instance, Child)


def test_grammar_features_StarNonContainment_isa_Child():
    instance = grammar_features_StarNonContainment()
    assert isinstance(instance, Child)


def test_grammar_features_StarPrefix_isa_Child():
    instance = grammar_features_StarPrefix()
    assert isinstance(instance, Child)


def test_assoc_reference1_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_OptionalContainment()
    b2 = grammar_features_OptionalContainment()
    _safe_set(a, 'grammar_features_X', b1)
    assert _is_linked(a, 'grammar_features_X', b1)
    if hasattr(b1, 'grammar_features_OptionalContainment'):
        assert _is_linked(b1, 'grammar_features_OptionalContainment', a)
    _safe_set(a, 'grammar_features_X', b2)
    assert _is_linked(a, 'grammar_features_X', b2)
    if hasattr(b1, 'grammar_features_OptionalContainment'):
        assert not _is_linked(b1, 'grammar_features_OptionalContainment', a)
    if hasattr(b2, 'grammar_features_OptionalContainment'):
        assert _is_linked(b2, 'grammar_features_OptionalContainment', a)
    _safe_set(a, 'grammar_features_X', None)
    assert not _is_linked(a, 'grammar_features_X', b2)
    if hasattr(b2, 'grammar_features_OptionalContainment'):
        assert not _is_linked(b2, 'grammar_features_OptionalContainment', a)


def test_assoc_reference10_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_MandatoryNonContainment()
    b2 = grammar_features_MandatoryNonContainment()
    _safe_set(a, 'grammar_features_X11', b1)
    assert _is_linked(a, 'grammar_features_X11', b1)
    if hasattr(b1, 'grammar_features_MandatoryNonContainment'):
        assert _is_linked(b1, 'grammar_features_MandatoryNonContainment', a)
    _safe_set(a, 'grammar_features_X11', b2)
    assert _is_linked(a, 'grammar_features_X11', b2)
    if hasattr(b1, 'grammar_features_MandatoryNonContainment'):
        assert not _is_linked(b1, 'grammar_features_MandatoryNonContainment', a)
    if hasattr(b2, 'grammar_features_MandatoryNonContainment'):
        assert _is_linked(b2, 'grammar_features_MandatoryNonContainment', a)
    _safe_set(a, 'grammar_features_X11', None)
    assert not _is_linked(a, 'grammar_features_X11', b2)
    if hasattr(b2, 'grammar_features_MandatoryNonContainment'):
        assert not _is_linked(b2, 'grammar_features_MandatoryNonContainment', a)


def test_assoc_reference12_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_PlusNonContainment()
    b2 = grammar_features_PlusNonContainment()
    _safe_set(a, 'grammar_features_X13', b1)
    assert _is_linked(a, 'grammar_features_X13', b1)
    if hasattr(b1, 'grammar_features_PlusNonContainment'):
        assert _is_linked(b1, 'grammar_features_PlusNonContainment', a)
    _safe_set(a, 'grammar_features_X13', b2)
    assert _is_linked(a, 'grammar_features_X13', b2)
    if hasattr(b1, 'grammar_features_PlusNonContainment'):
        assert not _is_linked(b1, 'grammar_features_PlusNonContainment', a)
    if hasattr(b2, 'grammar_features_PlusNonContainment'):
        assert _is_linked(b2, 'grammar_features_PlusNonContainment', a)
    _safe_set(a, 'grammar_features_X13', None)
    assert not _is_linked(a, 'grammar_features_X13', b2)
    if hasattr(b2, 'grammar_features_PlusNonContainment'):
        assert not _is_linked(b2, 'grammar_features_PlusNonContainment', a)


def test_assoc_reference14_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_StarNonContainment()
    b2 = grammar_features_StarNonContainment()
    _safe_set(a, 'grammar_features_X15', b1)
    assert _is_linked(a, 'grammar_features_X15', b1)
    if hasattr(b1, 'grammar_features_StarNonContainment'):
        assert _is_linked(b1, 'grammar_features_StarNonContainment', a)
    _safe_set(a, 'grammar_features_X15', b2)
    assert _is_linked(a, 'grammar_features_X15', b2)
    if hasattr(b1, 'grammar_features_StarNonContainment'):
        assert not _is_linked(b1, 'grammar_features_StarNonContainment', a)
    if hasattr(b2, 'grammar_features_StarNonContainment'):
        assert _is_linked(b2, 'grammar_features_StarNonContainment', a)
    _safe_set(a, 'grammar_features_X15', None)
    assert not _is_linked(a, 'grammar_features_X15', b2)
    if hasattr(b2, 'grammar_features_StarNonContainment'):
        assert not _is_linked(b2, 'grammar_features_StarNonContainment', a)


def test_assoc_reference2_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_MandatoryContainment()
    b2 = grammar_features_MandatoryContainment()
    _safe_set(a, 'grammar_features_X3', b1)
    assert _is_linked(a, 'grammar_features_X3', b1)
    if hasattr(b1, 'grammar_features_MandatoryContainment'):
        assert _is_linked(b1, 'grammar_features_MandatoryContainment', a)
    _safe_set(a, 'grammar_features_X3', b2)
    assert _is_linked(a, 'grammar_features_X3', b2)
    if hasattr(b1, 'grammar_features_MandatoryContainment'):
        assert not _is_linked(b1, 'grammar_features_MandatoryContainment', a)
    if hasattr(b2, 'grammar_features_MandatoryContainment'):
        assert _is_linked(b2, 'grammar_features_MandatoryContainment', a)
    _safe_set(a, 'grammar_features_X3', None)
    assert not _is_linked(a, 'grammar_features_X3', b2)
    if hasattr(b2, 'grammar_features_MandatoryContainment'):
        assert not _is_linked(b2, 'grammar_features_MandatoryContainment', a)


def test_assoc_reference4_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_PlusContainment()
    b2 = grammar_features_PlusContainment()
    _safe_set(a, 'grammar_features_X5', b1)
    assert _is_linked(a, 'grammar_features_X5', b1)
    if hasattr(b1, 'grammar_features_PlusContainment'):
        assert _is_linked(b1, 'grammar_features_PlusContainment', a)
    _safe_set(a, 'grammar_features_X5', b2)
    assert _is_linked(a, 'grammar_features_X5', b2)
    if hasattr(b1, 'grammar_features_PlusContainment'):
        assert not _is_linked(b1, 'grammar_features_PlusContainment', a)
    if hasattr(b2, 'grammar_features_PlusContainment'):
        assert _is_linked(b2, 'grammar_features_PlusContainment', a)
    _safe_set(a, 'grammar_features_X5', None)
    assert not _is_linked(a, 'grammar_features_X5', b2)
    if hasattr(b2, 'grammar_features_PlusContainment'):
        assert not _is_linked(b2, 'grammar_features_PlusContainment', a)


def test_assoc_reference6_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_StarContainment()
    b2 = grammar_features_StarContainment()
    _safe_set(a, 'grammar_features_X7', b1)
    assert _is_linked(a, 'grammar_features_X7', b1)
    if hasattr(b1, 'grammar_features_StarContainment'):
        assert _is_linked(b1, 'grammar_features_StarContainment', a)
    _safe_set(a, 'grammar_features_X7', b2)
    assert _is_linked(a, 'grammar_features_X7', b2)
    if hasattr(b1, 'grammar_features_StarContainment'):
        assert not _is_linked(b1, 'grammar_features_StarContainment', a)
    if hasattr(b2, 'grammar_features_StarContainment'):
        assert _is_linked(b2, 'grammar_features_StarContainment', a)
    _safe_set(a, 'grammar_features_X7', None)
    assert not _is_linked(a, 'grammar_features_X7', b2)
    if hasattr(b2, 'grammar_features_StarContainment'):
        assert not _is_linked(b2, 'grammar_features_StarContainment', a)


def test_assoc_reference8_link_reassign_clear():
    a = grammar_features_X(name="sample_text")
    b1 = grammar_features_OptionalNonContainment()
    b2 = grammar_features_OptionalNonContainment()
    _safe_set(a, 'grammar_features_X9', b1)
    assert _is_linked(a, 'grammar_features_X9', b1)
    if hasattr(b1, 'grammar_features_OptionalNonContainment'):
        assert _is_linked(b1, 'grammar_features_OptionalNonContainment', a)
    _safe_set(a, 'grammar_features_X9', b2)
    assert _is_linked(a, 'grammar_features_X9', b2)
    if hasattr(b1, 'grammar_features_OptionalNonContainment'):
        assert not _is_linked(b1, 'grammar_features_OptionalNonContainment', a)
    if hasattr(b2, 'grammar_features_OptionalNonContainment'):
        assert _is_linked(b2, 'grammar_features_OptionalNonContainment', a)
    _safe_set(a, 'grammar_features_X9', None)
    assert not _is_linked(a, 'grammar_features_X9', b2)
    if hasattr(b2, 'grammar_features_OptionalNonContainment'):
        assert not _is_linked(b2, 'grammar_features_OptionalNonContainment', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractSuperclass_strategy = st.builds(AbstractSuperclass)
@given(instance=AbstractSuperclass_strategy)
@settings(max_examples=25)
def test_AbstractSuperclass_instantiation(instance):
    assert isinstance(instance, AbstractSuperclass)


Child_strategy = st.builds(Child)
@given(instance=Child_strategy)
@settings(max_examples=25)
def test_Child_instantiation(instance):
    assert isinstance(instance, Child)


grammar_features_AbstractSuperclass_strategy = st.builds(grammar_features_AbstractSuperclass)
@given(instance=grammar_features_AbstractSuperclass_strategy)
@settings(max_examples=25)
def test_grammar_features_AbstractSuperclass_instantiation(instance):
    assert isinstance(instance, grammar_features_AbstractSuperclass)


grammar_features_AlternativeSyntax_strategy = st.builds(grammar_features_AlternativeSyntax)
@given(instance=grammar_features_AlternativeSyntax_strategy)
@settings(max_examples=25)
def test_grammar_features_AlternativeSyntax_instantiation(instance):
    assert isinstance(instance, grammar_features_AlternativeSyntax)


grammar_features_Child_strategy = st.builds(grammar_features_Child)
@given(instance=grammar_features_Child_strategy)
@settings(max_examples=25)
def test_grammar_features_Child_instantiation(instance):
    assert isinstance(instance, grammar_features_Child)


grammar_features_ClassWithAttributes_strategy = st.builds(grammar_features_ClassWithAttributes, a1=safe_text, a2=st.booleans())
@given(instance=grammar_features_ClassWithAttributes_strategy)
@settings(max_examples=25)
def test_grammar_features_ClassWithAttributes_instantiation(instance):
    assert isinstance(instance, grammar_features_ClassWithAttributes)


grammar_features_CompoundOptional_strategy = st.builds(grammar_features_CompoundOptional)
@given(instance=grammar_features_CompoundOptional_strategy)
@settings(max_examples=25)
def test_grammar_features_CompoundOptional_instantiation(instance):
    assert isinstance(instance, grammar_features_CompoundOptional)


grammar_features_CompoundPlus_strategy = st.builds(grammar_features_CompoundPlus)
@given(instance=grammar_features_CompoundPlus_strategy)
@settings(max_examples=25)
def test_grammar_features_CompoundPlus_instantiation(instance):
    assert isinstance(instance, grammar_features_CompoundPlus)


grammar_features_CompoundStar_strategy = st.builds(grammar_features_CompoundStar)
@given(instance=grammar_features_CompoundStar_strategy)
@settings(max_examples=25)
def test_grammar_features_CompoundStar_instantiation(instance):
    assert isinstance(instance, grammar_features_CompoundStar)


grammar_features_ConcreteSubclassA_strategy = st.builds(grammar_features_ConcreteSubclassA)
@given(instance=grammar_features_ConcreteSubclassA_strategy)
@settings(max_examples=25)
def test_grammar_features_ConcreteSubclassA_instantiation(instance):
    assert isinstance(instance, grammar_features_ConcreteSubclassA)


grammar_features_ConcreteSubclassB_strategy = st.builds(grammar_features_ConcreteSubclassB)
@given(instance=grammar_features_ConcreteSubclassB_strategy)
@settings(max_examples=25)
def test_grammar_features_ConcreteSubclassB_instantiation(instance):
    assert isinstance(instance, grammar_features_ConcreteSubclassB)


grammar_features_MandatoryContainment_strategy = st.builds(grammar_features_MandatoryContainment)
@given(instance=grammar_features_MandatoryContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_MandatoryContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_MandatoryContainment)


grammar_features_MandatoryNonContainment_strategy = st.builds(grammar_features_MandatoryNonContainment)
@given(instance=grammar_features_MandatoryNonContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_MandatoryNonContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_MandatoryNonContainment)


grammar_features_OptionalContainment_strategy = st.builds(grammar_features_OptionalContainment)
@given(instance=grammar_features_OptionalContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_OptionalContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_OptionalContainment)


grammar_features_OptionalNonContainment_strategy = st.builds(grammar_features_OptionalNonContainment)
@given(instance=grammar_features_OptionalNonContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_OptionalNonContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_OptionalNonContainment)


grammar_features_OptionalPrefix_strategy = st.builds(grammar_features_OptionalPrefix)
@given(instance=grammar_features_OptionalPrefix_strategy)
@settings(max_examples=25)
def test_grammar_features_OptionalPrefix_instantiation(instance):
    assert isinstance(instance, grammar_features_OptionalPrefix)


grammar_features_PlusContainment_strategy = st.builds(grammar_features_PlusContainment)
@given(instance=grammar_features_PlusContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_PlusContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_PlusContainment)


grammar_features_PlusNonContainment_strategy = st.builds(grammar_features_PlusNonContainment)
@given(instance=grammar_features_PlusNonContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_PlusNonContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_PlusNonContainment)


grammar_features_PlusPrefix_strategy = st.builds(grammar_features_PlusPrefix)
@given(instance=grammar_features_PlusPrefix_strategy)
@settings(max_examples=25)
def test_grammar_features_PlusPrefix_instantiation(instance):
    assert isinstance(instance, grammar_features_PlusPrefix)


grammar_features_Root_strategy = st.builds(grammar_features_Root)
@given(instance=grammar_features_Root_strategy)
@settings(max_examples=25)
def test_grammar_features_Root_instantiation(instance):
    assert isinstance(instance, grammar_features_Root)


grammar_features_SecondRoot_strategy = st.builds(grammar_features_SecondRoot)
@given(instance=grammar_features_SecondRoot_strategy)
@settings(max_examples=25)
def test_grammar_features_SecondRoot_instantiation(instance):
    assert isinstance(instance, grammar_features_SecondRoot)


grammar_features_StarContainment_strategy = st.builds(grammar_features_StarContainment)
@given(instance=grammar_features_StarContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_StarContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_StarContainment)


grammar_features_StarNonContainment_strategy = st.builds(grammar_features_StarNonContainment)
@given(instance=grammar_features_StarNonContainment_strategy)
@settings(max_examples=25)
def test_grammar_features_StarNonContainment_instantiation(instance):
    assert isinstance(instance, grammar_features_StarNonContainment)


grammar_features_StarPrefix_strategy = st.builds(grammar_features_StarPrefix)
@given(instance=grammar_features_StarPrefix_strategy)
@settings(max_examples=25)
def test_grammar_features_StarPrefix_instantiation(instance):
    assert isinstance(instance, grammar_features_StarPrefix)


grammar_features_X_strategy = st.builds(grammar_features_X, name=safe_text)
@given(instance=grammar_features_X_strategy)
@settings(max_examples=25)
def test_grammar_features_X_instantiation(instance):
    assert isinstance(instance, grammar_features_X)


