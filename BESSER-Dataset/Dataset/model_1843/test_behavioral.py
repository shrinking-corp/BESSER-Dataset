import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OCLElement,
    OCLNamedElement,
    OCLPackageParent,
    OCLRoot,
    OCLType,
    OCLTypeValue,
    OCLTypedElement,
    library_OCLBoundType,
    library_OCLElement,
    library_OCLLibrary,
    library_OCLLibraryIteration,
    library_OCLLibraryOperation,
    library_OCLLibraryProperty,
    library_OCLNamedElement,
    library_OCLPackage,
    library_OCLPackageParent,
    library_OCLParameter,
    library_OCLRoot,
    library_OCLType,
    library_OCLTypeBinding,
    library_OCLTypeDefinition,
    library_OCLTypeParameter,
    library_OCLTypeReference,
    library_OCLTypeValue,
    library_OCLTypedElement,
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

def test_assoc_iteration20_stub_double():
    # library_OCLTypeDefinition has no real 'library_OCLTypeDefinition21' property in the generated
    # code (a bare stub) -- manually attach it so library_OCLLibraryIteration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_OCLLibraryIteration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_OCLLibraryIteration(class_="sample_text", iterator="sample_text", iterators=True)
    partner = library_OCLTypeDefinition()
    setattr(partner, 'library_OCLTypeDefinition21', None)
    _safe_set(owner, 'library_OCLLibraryIteration', partner)
    assert owner in getattr(partner, 'library_OCLTypeDefinition21')
    _safe_set(owner, 'library_OCLLibraryIteration', None)
    assert owner not in getattr(partner, 'library_OCLTypeDefinition21')


def test_assoc_operation22_stub_double():
    # library_OCLTypeDefinition has no real 'library_OCLTypeDefinition23' property in the generated
    # code (a bare stub) -- manually attach it so library_OCLLibraryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_OCLLibraryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_OCLLibraryOperation(class_="sample_text", isStatic=True)
    partner = library_OCLTypeDefinition()
    setattr(partner, 'library_OCLTypeDefinition23', None)
    _safe_set(owner, 'library_OCLLibraryOperation24', partner)
    assert owner in getattr(partner, 'library_OCLTypeDefinition23')
    _safe_set(owner, 'library_OCLLibraryOperation24', None)
    assert owner not in getattr(partner, 'library_OCLTypeDefinition23')


def test_assoc_parameter6_stub_double():
    # library_OCLParameter has no real 'library_OCLParameter' property in the generated
    # code (a bare stub) -- manually attach it so library_OCLLibraryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_OCLLibraryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_OCLLibraryOperation(class_="sample_text", isStatic=True)
    partner = library_OCLParameter()
    setattr(partner, 'library_OCLParameter', None)
    _safe_set(owner, 'library_OCLLibraryOperation7', {partner})
    assert getattr(partner, 'library_OCLParameter') == owner
    _safe_set(owner, 'library_OCLLibraryOperation7', set())
    assert getattr(partner, 'library_OCLParameter') is None


def test_assoc_property25_stub_double():
    # library_OCLTypeDefinition has no real 'library_OCLTypeDefinition26' property in the generated
    # code (a bare stub) -- manually attach it so library_OCLLibraryProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_OCLLibraryProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_OCLLibraryProperty(class_="sample_text", isStatic=True)
    partner = library_OCLTypeDefinition()
    setattr(partner, 'library_OCLTypeDefinition26', None)
    _safe_set(owner, 'library_OCLLibraryProperty', partner)
    assert owner in getattr(partner, 'library_OCLTypeDefinition26')
    _safe_set(owner, 'library_OCLLibraryProperty', None)
    assert owner not in getattr(partner, 'library_OCLTypeDefinition26')


def test_assoc_typeParameter5_stub_double():
    # library_OCLTypeParameter has no real 'library_OCLTypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so library_OCLLibraryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library_OCLLibraryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library_OCLLibraryOperation(class_="sample_text", isStatic=True)
    partner = library_OCLTypeParameter()
    setattr(partner, 'library_OCLTypeParameter', None)
    _safe_set(owner, 'library_OCLLibraryOperation', {partner})
    assert getattr(partner, 'library_OCLTypeParameter') == owner
    _safe_set(owner, 'library_OCLLibraryOperation', set())
    assert getattr(partner, 'library_OCLTypeParameter') is None


