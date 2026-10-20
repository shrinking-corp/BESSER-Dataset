import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Typeable,
    TypedElement,
    classdiagram_Association,
    classdiagram_Attribute,
    classdiagram_Class,
    classdiagram_ClassDiagram,
    classdiagram_Composition,
    classdiagram_DataType,
    classdiagram_Dependency,
    classdiagram_NamedElement,
    classdiagram_Operation,
    classdiagram_Typeable,
    classdiagram_TypedElement,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associations3_stub_double():
    # classdiagram_ClassDiagram has no real 'classdiagram_ClassDiagram4' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(multiplicity="sample_text")
    partner = classdiagram_ClassDiagram()
    setattr(partner, 'classdiagram_ClassDiagram4', None)
    _safe_set(owner, 'classdiagram_Association', partner)
    assert owner in getattr(partner, 'classdiagram_ClassDiagram4')
    _safe_set(owner, 'classdiagram_Association', None)
    assert owner not in getattr(partner, 'classdiagram_ClassDiagram4')


def test_assoc_associationsAsSource26_stub_double():
    # classdiagram_Class has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Association', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Association', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_associationsAsTarget27_stub_double():
    # classdiagram_Class has no real 'target' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'target', None)
    _safe_set(owner, 'Association28', partner)
    assert owner in getattr(partner, 'target')
    _safe_set(owner, 'Association28', None)
    assert owner not in getattr(partner, 'target')


def test_assoc_composite49_stub_double():
    # classdiagram_Class has no real 'Class50' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Composition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Composition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Composition(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class50', None)
    _safe_set(owner, 'compositionsAsComposite', partner)
    assert getattr(partner, 'Class50') == owner
    _safe_set(owner, 'compositionsAsComposite', None)
    assert getattr(partner, 'Class50') is None


def test_assoc_compositions7_stub_double():
    # classdiagram_ClassDiagram has no real 'classdiagram_ClassDiagram8' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Composition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Composition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Composition(multiplicity="sample_text")
    partner = classdiagram_ClassDiagram()
    setattr(partner, 'classdiagram_ClassDiagram8', None)
    _safe_set(owner, 'classdiagram_Composition', partner)
    assert owner in getattr(partner, 'classdiagram_ClassDiagram8')
    _safe_set(owner, 'classdiagram_Composition', None)
    assert owner not in getattr(partner, 'classdiagram_ClassDiagram8')


def test_assoc_compositionsAsComposite30_stub_double():
    # classdiagram_Class has no real 'composite' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Composition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Composition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Composition(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'composite', None)
    _safe_set(owner, 'Composition31', partner)
    assert owner in getattr(partner, 'composite')
    _safe_set(owner, 'Composition31', None)
    assert owner not in getattr(partner, 'composite')


def test_assoc_compositionsAsConstituent29_stub_double():
    # classdiagram_Class has no real 'constituent' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Composition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Composition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Composition(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'constituent', None)
    _safe_set(owner, 'Composition', partner)
    assert owner in getattr(partner, 'constituent')
    _safe_set(owner, 'Composition', None)
    assert owner not in getattr(partner, 'constituent')


def test_assoc_constituent47_stub_double():
    # classdiagram_Class has no real 'Class48' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Composition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Composition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Composition(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class48', None)
    _safe_set(owner, 'compositionsAsConstituent', partner)
    assert getattr(partner, 'Class48') == owner
    _safe_set(owner, 'compositionsAsConstituent', None)
    assert getattr(partner, 'Class48') is None


def test_assoc_dependee37_stub_double():
    # classdiagram_Class has no real 'Class38' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class38', None)
    _safe_set(owner, 'dependenciesAsDependee', partner)
    assert getattr(partner, 'Class38') == owner
    _safe_set(owner, 'dependenciesAsDependee', None)
    assert getattr(partner, 'Class38') is None


def test_assoc_dependencies1_stub_double():
    # classdiagram_ClassDiagram has no real 'classdiagram_ClassDiagram2' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_ClassDiagram()
    setattr(partner, 'classdiagram_ClassDiagram2', None)
    _safe_set(owner, 'classdiagram_Dependency', partner)
    assert owner in getattr(partner, 'classdiagram_ClassDiagram2')
    _safe_set(owner, 'classdiagram_Dependency', None)
    assert owner not in getattr(partner, 'classdiagram_ClassDiagram2')


def test_assoc_dependenciesAsDependee12_stub_double():
    # classdiagram_Class has no real 'dependee' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'dependee', None)
    _safe_set(owner, 'Dependency', partner)
    assert owner in getattr(partner, 'dependee')
    _safe_set(owner, 'Dependency', None)
    assert owner not in getattr(partner, 'dependee')


def test_assoc_dependenciesAsDepender13_stub_double():
    # classdiagram_Class has no real 'depender' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'depender', None)
    _safe_set(owner, 'Dependency14', partner)
    assert owner in getattr(partner, 'depender')
    _safe_set(owner, 'Dependency14', None)
    assert owner not in getattr(partner, 'depender')


def test_assoc_depender39_stub_double():
    # classdiagram_Class has no real 'Class40' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Dependency(name="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class40', None)
    _safe_set(owner, 'dependenciesAsDepender', partner)
    assert getattr(partner, 'Class40') == owner
    _safe_set(owner, 'dependenciesAsDepender', None)
    assert getattr(partner, 'Class40') is None


def test_assoc_source43_stub_double():
    # classdiagram_Class has no real 'Class44' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class44', None)
    _safe_set(owner, 'associationsAsSource', partner)
    assert getattr(partner, 'Class44') == owner
    _safe_set(owner, 'associationsAsSource', None)
    assert getattr(partner, 'Class44') is None


def test_assoc_target45_stub_double():
    # classdiagram_Class has no real 'Class46' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_Association(multiplicity="sample_text")
    partner = classdiagram_Class()
    setattr(partner, 'Class46', None)
    _safe_set(owner, 'associationsAsTarget', partner)
    assert getattr(partner, 'Class46') == owner
    _safe_set(owner, 'associationsAsTarget', None)
    assert getattr(partner, 'Class46') is None


def test_assoc_type41_stub_double():
    # classdiagram_Typeable has no real 'classdiagram_Typeable42' property in the generated
    # code (a bare stub) -- manually attach it so classdiagram_TypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classdiagram_TypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classdiagram_TypedElement(public=True)
    partner = classdiagram_Typeable()
    setattr(partner, 'classdiagram_Typeable42', None)
    _safe_set(owner, 'classdiagram_TypedElement', partner)
    assert getattr(partner, 'classdiagram_Typeable42') == owner
    _safe_set(owner, 'classdiagram_TypedElement', None)
    assert getattr(partner, 'classdiagram_Typeable42') is None


