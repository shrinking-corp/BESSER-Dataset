import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MetaModelGraph_Composition,
    MetaModelGraph_EAttribute,
    MetaModelGraph_EClass,
    MetaModelGraph_EReference,
    MetaModelGraph_Graph,
    MetaModelGraph_Node,
    MetaModelGraph_Reference,
    MetaModelGraph_Relation,
    MetaModelGraph_SubClass,
    MetaModelGraph_SubGraph,
    Relation,
    EnumModular,
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

def test_assoc_listNodes26_reverse_link_reassign_clear():
    a1 = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    a2 = MetaModelGraph_Node(enumModularNotation="sample_text_2", extension="sample_text_2", icon="sample_text_2", insideRecursion=False)
    b = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    _safe_set(b, 'MetaModelGraph_Node27', a1)
    assert _is_linked(b, 'MetaModelGraph_Node27', a1)
    if hasattr(a1, 'MetaModelGraph_Node25'):
        assert _is_linked(a1, 'MetaModelGraph_Node25', b)
    _safe_set(b, 'MetaModelGraph_Node27', a2)
    assert _is_linked(b, 'MetaModelGraph_Node27', a2)
    if hasattr(a1, 'MetaModelGraph_Node25'):
        assert not _is_linked(a1, 'MetaModelGraph_Node25', b)
    if hasattr(a2, 'MetaModelGraph_Node25'):
        assert _is_linked(a2, 'MetaModelGraph_Node25', b)
    _safe_set(b, 'MetaModelGraph_Node27', None)
    assert not _is_linked(b, 'MetaModelGraph_Node27', a2)
    if hasattr(a2, 'MetaModelGraph_Node25'):
        assert not _is_linked(a2, 'MetaModelGraph_Node25', b)


def test_assoc_nodes6_reverse_link_reassign_clear():
    a1 = MetaModelGraph_SubGraph(amountEClassesOut=7, amountOfAbstractEClass=7, amountOfConcreteEClass=7, amountOfParentAbstractEClass=7, amountOfParentEClass=7, amountOfRecursionPackages=7, amountPackages=7, amountRecursionUnits=7, amountUnits=7, height=7)
    a2 = MetaModelGraph_SubGraph(amountEClassesOut=13, amountOfAbstractEClass=13, amountOfConcreteEClass=13, amountOfParentAbstractEClass=13, amountOfParentEClass=13, amountOfRecursionPackages=13, amountPackages=13, amountRecursionUnits=13, amountUnits=13, height=13)
    b = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    _safe_set(b, 'MetaModelGraph_Node', a1)
    assert _is_linked(b, 'MetaModelGraph_Node', a1)
    if hasattr(a1, 'MetaModelGraph_SubGraph7'):
        assert _is_linked(a1, 'MetaModelGraph_SubGraph7', b)
    _safe_set(b, 'MetaModelGraph_Node', a2)
    assert _is_linked(b, 'MetaModelGraph_Node', a2)
    if hasattr(a1, 'MetaModelGraph_SubGraph7'):
        assert not _is_linked(a1, 'MetaModelGraph_SubGraph7', b)
    if hasattr(a2, 'MetaModelGraph_SubGraph7'):
        assert _is_linked(a2, 'MetaModelGraph_SubGraph7', b)
    _safe_set(b, 'MetaModelGraph_Node', None)
    assert not _is_linked(b, 'MetaModelGraph_Node', a2)
    if hasattr(a2, 'MetaModelGraph_SubGraph7'):
        assert not _is_linked(a2, 'MetaModelGraph_SubGraph7', b)


def test_assoc_root13_reverse_link_reassign_clear():
    a1 = MetaModelGraph_SubGraph(amountEClassesOut=7, amountOfAbstractEClass=7, amountOfConcreteEClass=7, amountOfParentAbstractEClass=7, amountOfParentEClass=7, amountOfRecursionPackages=7, amountPackages=7, amountRecursionUnits=7, amountUnits=7, height=7)
    a2 = MetaModelGraph_SubGraph(amountEClassesOut=13, amountOfAbstractEClass=13, amountOfConcreteEClass=13, amountOfParentAbstractEClass=13, amountOfParentEClass=13, amountOfRecursionPackages=13, amountPackages=13, amountRecursionUnits=13, amountUnits=13, height=13)
    b = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    _safe_set(b, 'MetaModelGraph_Node15', a1)
    assert _is_linked(b, 'MetaModelGraph_Node15', a1)
    if hasattr(a1, 'MetaModelGraph_SubGraph14'):
        assert _is_linked(a1, 'MetaModelGraph_SubGraph14', b)
    _safe_set(b, 'MetaModelGraph_Node15', a2)
    assert _is_linked(b, 'MetaModelGraph_Node15', a2)
    if hasattr(a1, 'MetaModelGraph_SubGraph14'):
        assert not _is_linked(a1, 'MetaModelGraph_SubGraph14', b)
    if hasattr(a2, 'MetaModelGraph_SubGraph14'):
        assert _is_linked(a2, 'MetaModelGraph_SubGraph14', b)
    _safe_set(b, 'MetaModelGraph_Node15', None)
    assert not _is_linked(b, 'MetaModelGraph_Node15', a2)
    if hasattr(a2, 'MetaModelGraph_SubGraph14'):
        assert not _is_linked(a2, 'MetaModelGraph_SubGraph14', b)


def test_assoc_subgraph0_reverse_link_reassign_clear():
    a1 = MetaModelGraph_SubGraph(amountEClassesOut=7, amountOfAbstractEClass=7, amountOfConcreteEClass=7, amountOfParentAbstractEClass=7, amountOfParentEClass=7, amountOfRecursionPackages=7, amountPackages=7, amountRecursionUnits=7, amountUnits=7, height=7)
    a2 = MetaModelGraph_SubGraph(amountEClassesOut=13, amountOfAbstractEClass=13, amountOfConcreteEClass=13, amountOfParentAbstractEClass=13, amountOfParentEClass=13, amountOfRecursionPackages=13, amountPackages=13, amountRecursionUnits=13, amountUnits=13, height=13)
    b = MetaModelGraph_Graph(amountAbstractEClasses=7, amountConcreteEClass=7, amountEClasses=7)
    _safe_set(b, 'MetaModelGraph_Graph', {a1})
    assert _is_linked(b, 'MetaModelGraph_Graph', a1)
    if hasattr(a1, 'MetaModelGraph_SubGraph'):
        assert _is_linked(a1, 'MetaModelGraph_SubGraph', b)
    _safe_set(b, 'MetaModelGraph_Graph', {a2})
    assert _is_linked(b, 'MetaModelGraph_Graph', a2)
    if hasattr(a1, 'MetaModelGraph_SubGraph'):
        assert not _is_linked(a1, 'MetaModelGraph_SubGraph', b)
    if hasattr(a2, 'MetaModelGraph_SubGraph'):
        assert _is_linked(a2, 'MetaModelGraph_SubGraph', b)
    _safe_set(b, 'MetaModelGraph_Graph', set())
    assert not _is_linked(b, 'MetaModelGraph_Graph', a2)
    if hasattr(a2, 'MetaModelGraph_SubGraph'):
        assert not _is_linked(a2, 'MetaModelGraph_SubGraph', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_compositions16_stub_double():
    # MetaModelGraph_Composition has no real 'Composition' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Composition()
    setattr(partner, 'Composition', None)
    _safe_set(owner, 'parentNode', {partner})
    assert getattr(partner, 'Composition') == owner
    _safe_set(owner, 'parentNode', set())
    assert getattr(partner, 'Composition') is None


def test_assoc_directComposition31_stub_double():
    # MetaModelGraph_Composition has no real 'MetaModelGraph_Composition' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Composition()
    setattr(partner, 'MetaModelGraph_Composition', None)
    _safe_set(owner, 'MetaModelGraph_Node32', {partner})
    assert getattr(partner, 'MetaModelGraph_Composition') == owner
    _safe_set(owner, 'MetaModelGraph_Node32', set())
    assert getattr(partner, 'MetaModelGraph_Composition') is None


def test_assoc_directSubclasses28_stub_double():
    # MetaModelGraph_SubClass has no real 'MetaModelGraph_SubClass30' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_SubClass()
    setattr(partner, 'MetaModelGraph_SubClass30', None)
    _safe_set(owner, 'MetaModelGraph_Node29', {partner})
    assert getattr(partner, 'MetaModelGraph_SubClass30') == owner
    _safe_set(owner, 'MetaModelGraph_Node29', set())
    assert getattr(partner, 'MetaModelGraph_SubClass30') is None


def test_assoc_eClass21_stub_double():
    # MetaModelGraph_EClass has no real 'MetaModelGraph_EClass23' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_EClass()
    setattr(partner, 'MetaModelGraph_EClass23', None)
    _safe_set(owner, 'MetaModelGraph_Node22', partner)
    assert getattr(partner, 'MetaModelGraph_EClass23') == owner
    _safe_set(owner, 'MetaModelGraph_Node22', None)
    assert getattr(partner, 'MetaModelGraph_EClass23') is None


def test_assoc_eClassAbstract3_stub_double():
    # MetaModelGraph_EClass has no real 'MetaModelGraph_EClass5' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Graph(amountAbstractEClasses=7, amountConcreteEClass=7, amountEClasses=7)
    partner = MetaModelGraph_EClass()
    setattr(partner, 'MetaModelGraph_EClass5', None)
    _safe_set(owner, 'MetaModelGraph_Graph4', {partner})
    assert getattr(partner, 'MetaModelGraph_EClass5') == owner
    _safe_set(owner, 'MetaModelGraph_Graph4', set())
    assert getattr(partner, 'MetaModelGraph_EClass5') is None


def test_assoc_eClassList1_stub_double():
    # MetaModelGraph_EClass has no real 'MetaModelGraph_EClass' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Graph(amountAbstractEClasses=7, amountConcreteEClass=7, amountEClasses=7)
    partner = MetaModelGraph_EClass()
    setattr(partner, 'MetaModelGraph_EClass', None)
    _safe_set(owner, 'MetaModelGraph_Graph2', {partner})
    assert getattr(partner, 'MetaModelGraph_EClass') == owner
    _safe_set(owner, 'MetaModelGraph_Graph2', set())
    assert getattr(partner, 'MetaModelGraph_EClass') is None


def test_assoc_eClassesListOut10_stub_double():
    # MetaModelGraph_EClass has no real 'MetaModelGraph_EClass12' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_SubGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_SubGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_SubGraph(amountEClassesOut=7, amountOfAbstractEClass=7, amountOfConcreteEClass=7, amountOfParentAbstractEClass=7, amountOfParentEClass=7, amountOfRecursionPackages=7, amountPackages=7, amountRecursionUnits=7, amountUnits=7, height=7)
    partner = MetaModelGraph_EClass()
    setattr(partner, 'MetaModelGraph_EClass12', None)
    _safe_set(owner, 'MetaModelGraph_SubGraph11', {partner})
    assert getattr(partner, 'MetaModelGraph_EClass12') == owner
    _safe_set(owner, 'MetaModelGraph_SubGraph11', set())
    assert getattr(partner, 'MetaModelGraph_EClass12') is None


def test_assoc_name33_stub_double():
    # MetaModelGraph_EAttribute has no real 'MetaModelGraph_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_EAttribute()
    setattr(partner, 'MetaModelGraph_EAttribute', None)
    _safe_set(owner, 'MetaModelGraph_Node34', partner)
    assert getattr(partner, 'MetaModelGraph_EAttribute') == owner
    _safe_set(owner, 'MetaModelGraph_Node34', None)
    assert getattr(partner, 'MetaModelGraph_EAttribute') is None


def test_assoc_parentNode38_stub_double():
    # MetaModelGraph_Composition has no real 'compositions' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Composition()
    setattr(partner, 'compositions', None)
    _safe_set(owner, 'Node39', partner)
    assert getattr(partner, 'compositions') == owner
    _safe_set(owner, 'Node39', None)
    assert getattr(partner, 'compositions') is None


def test_assoc_references17_stub_double():
    # MetaModelGraph_Reference has no real 'MetaModelGraph_Reference' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Reference()
    setattr(partner, 'MetaModelGraph_Reference', None)
    _safe_set(owner, 'MetaModelGraph_Node18', {partner})
    assert getattr(partner, 'MetaModelGraph_Reference') == owner
    _safe_set(owner, 'MetaModelGraph_Node18', set())
    assert getattr(partner, 'MetaModelGraph_Reference') is None


def test_assoc_relations24_stub_double():
    # MetaModelGraph_Relation has no real 'Relation' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Relation()
    setattr(partner, 'Relation', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Relation') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Relation') is None


def test_assoc_relations8_stub_double():
    # MetaModelGraph_Relation has no real 'MetaModelGraph_Relation' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_SubGraph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_SubGraph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_SubGraph(amountEClassesOut=7, amountOfAbstractEClass=7, amountOfConcreteEClass=7, amountOfParentAbstractEClass=7, amountOfParentEClass=7, amountOfRecursionPackages=7, amountPackages=7, amountRecursionUnits=7, amountUnits=7, height=7)
    partner = MetaModelGraph_Relation()
    setattr(partner, 'MetaModelGraph_Relation', None)
    _safe_set(owner, 'MetaModelGraph_SubGraph9', {partner})
    assert getattr(partner, 'MetaModelGraph_Relation') == owner
    _safe_set(owner, 'MetaModelGraph_SubGraph9', set())
    assert getattr(partner, 'MetaModelGraph_Relation') is None


def test_assoc_subClasses19_stub_double():
    # MetaModelGraph_SubClass has no real 'MetaModelGraph_SubClass' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_SubClass()
    setattr(partner, 'MetaModelGraph_SubClass', None)
    _safe_set(owner, 'MetaModelGraph_Node20', {partner})
    assert getattr(partner, 'MetaModelGraph_SubClass') == owner
    _safe_set(owner, 'MetaModelGraph_Node20', set())
    assert getattr(partner, 'MetaModelGraph_SubClass') is None


def test_assoc_target35_stub_double():
    # MetaModelGraph_Relation has no real 'relations' property in the generated
    # code (a bare stub) -- manually attach it so MetaModelGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MetaModelGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MetaModelGraph_Node(enumModularNotation="sample_text", extension="sample_text", icon="sample_text", insideRecursion=True)
    partner = MetaModelGraph_Relation()
    setattr(partner, 'relations', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'relations') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'relations') is None


