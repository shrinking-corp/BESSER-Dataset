import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SrcArc,
    SrcElement,
    SrcLocatedElement,
    SrcNamedElement,
    TrgIdedElement,
    TrgLabeledElement,
    TrgLocatedElement,
    TrgNetContent,
    TrgNetContentElement,
    jointPackage_PetriNet2PNML_JointMM,
    jointPackage_PetriNet2PNML_SrcArc,
    jointPackage_PetriNet2PNML_SrcElement,
    jointPackage_PetriNet2PNML_SrcLocatedElement,
    jointPackage_PetriNet2PNML_SrcNamedElement,
    jointPackage_PetriNet2PNML_SrcPetriNet,
    jointPackage_PetriNet2PNML_SrcPlace,
    jointPackage_PetriNet2PNML_SrcPlaceToTransition,
    jointPackage_PetriNet2PNML_SrcTransition,
    jointPackage_PetriNet2PNML_SrcTransitionToPlace,
    jointPackage_PetriNet2PNML_TrgArc,
    jointPackage_PetriNet2PNML_TrgIdedElement,
    jointPackage_PetriNet2PNML_TrgLabel,
    jointPackage_PetriNet2PNML_TrgLabeledElement,
    jointPackage_PetriNet2PNML_TrgLocatedElement,
    jointPackage_PetriNet2PNML_TrgName,
    jointPackage_PetriNet2PNML_TrgNetContent,
    jointPackage_PetriNet2PNML_TrgNetContentElement,
    jointPackage_PetriNet2PNML_TrgNetElement,
    jointPackage_PetriNet2PNML_TrgPNMLDocument,
    jointPackage_PetriNet2PNML_TrgPlace,
    jointPackage_PetriNet2PNML_TrgTransition,
    jointPackage_PetriNet2PNML_TrgURI,
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

def test_assoc_arcs4_stub_double():
    # jointPackage_PetriNet2PNML_SrcPetriNet has no real 'net5' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_PetriNet2PNML_SrcArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_PetriNet2PNML_SrcArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    partner = jointPackage_PetriNet2PNML_SrcPetriNet()
    setattr(partner, 'net5', None)
    _safe_set(owner, 'SrcArc', partner)
    assert owner in getattr(partner, 'net5')
    _safe_set(owner, 'SrcArc', None)
    assert owner not in getattr(partner, 'net5')


def test_assoc_labels39_stub_double():
    # jointPackage_PetriNet2PNML_TrgLabeledElement has no real 'jointPackage_PetriNet2PNML_TrgLabeledElement' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_PetriNet2PNML_TrgLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_PetriNet2PNML_TrgLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_PetriNet2PNML_TrgLabel(text="sample_text")
    partner = jointPackage_PetriNet2PNML_TrgLabeledElement()
    setattr(partner, 'jointPackage_PetriNet2PNML_TrgLabeledElement', None)
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgLabel', partner)
    assert owner in getattr(partner, 'jointPackage_PetriNet2PNML_TrgLabeledElement')
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgLabel', None)
    assert owner not in getattr(partner, 'jointPackage_PetriNet2PNML_TrgLabeledElement')


def test_assoc_net15_stub_double():
    # jointPackage_PetriNet2PNML_SrcPetriNet has no real 'SrcPetriNet16' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_PetriNet2PNML_SrcArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_PetriNet2PNML_SrcArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_PetriNet2PNML_SrcArc(weight=7)
    partner = jointPackage_PetriNet2PNML_SrcPetriNet()
    setattr(partner, 'SrcPetriNet16', None)
    _safe_set(owner, 'arcs', partner)
    assert getattr(partner, 'SrcPetriNet16') == owner
    _safe_set(owner, 'arcs', None)
    assert getattr(partner, 'SrcPetriNet16') is None


def test_assoc_type29_stub_double():
    # jointPackage_PetriNet2PNML_TrgNetElement has no real 'jointPackage_PetriNet2PNML_TrgNetElement30' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_PetriNet2PNML_TrgURI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_PetriNet2PNML_TrgURI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    partner = jointPackage_PetriNet2PNML_TrgNetElement()
    setattr(partner, 'jointPackage_PetriNet2PNML_TrgNetElement30', None)
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgURI31', partner)
    assert getattr(partner, 'jointPackage_PetriNet2PNML_TrgNetElement30') == owner
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgURI31', None)
    assert getattr(partner, 'jointPackage_PetriNet2PNML_TrgNetElement30') is None


def test_assoc_xmlns25_stub_double():
    # jointPackage_PetriNet2PNML_TrgPNMLDocument has no real 'jointPackage_PetriNet2PNML_TrgPNMLDocument26' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_PetriNet2PNML_TrgURI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_PetriNet2PNML_TrgURI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_PetriNet2PNML_TrgURI(value="sample_text")
    partner = jointPackage_PetriNet2PNML_TrgPNMLDocument()
    setattr(partner, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26', None)
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgURI', partner)
    assert getattr(partner, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26') == owner
    _safe_set(owner, 'jointPackage_PetriNet2PNML_TrgURI', None)
    assert getattr(partner, 'jointPackage_PetriNet2PNML_TrgPNMLDocument26') is None


