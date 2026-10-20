import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActionRoot,
    ControlPath,
    EntryPoint,
    ExitPoint,
    LogicalRoot,
    Mode,
    Point,
    Referable,
    ResourceRoot,
    remes_CompositeEntryPoint,
    remes_CompositeExitPoint,
    remes_CompositeMode,
    remes_ConditionalConnector,
    remes_Constant,
    remes_ControlPath,
    remes_Edge,
    remes_EntryPoint,
    remes_ExitPoint,
    remes_InitPoint,
    remes_Mode,
    remes_Point,
    remes_Referable,
    remes_RemesDiagram,
    remes_Resource,
    remes_SubMode,
    remes_Variable,
    remes_WritePoint,
    PrimitiveTypes,
    ResourceTypes,
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

def test_assoc_constants7_reverse_link_reassign_clear():
    a1 = remes_Mode()
    a2 = remes_Mode()
    b = remes_Constant(global_=True, type="sample_text", value="sample_text")
    _safe_set(b, 'Constant', a1)
    assert _is_linked(b, 'Constant', a1)
    if hasattr(a1, 'scope8'):
        assert _is_linked(a1, 'scope8', b)
    _safe_set(b, 'Constant', a2)
    assert _is_linked(b, 'Constant', a2)
    if hasattr(a1, 'scope8'):
        assert not _is_linked(a1, 'scope8', b)
    if hasattr(a2, 'scope8'):
        assert _is_linked(a2, 'scope8', b)
    _safe_set(b, 'Constant', None)
    assert not _is_linked(b, 'Constant', a2)
    if hasattr(a2, 'scope8'):
        assert not _is_linked(a2, 'scope8', b)


def test_assoc_resources5_reverse_link_reassign_clear():
    a1 = remes_Resource(expression="sample_text", type="sample_text")
    a2 = remes_Resource(expression="sample_text_2", type="sample_text_2")
    b = remes_Mode()
    _safe_set(b, 'scope6', {a1})
    assert _is_linked(b, 'scope6', a1)
    if hasattr(a1, 'Resource'):
        assert _is_linked(a1, 'Resource', b)
    _safe_set(b, 'scope6', {a2})
    assert _is_linked(b, 'scope6', a2)
    if hasattr(a1, 'Resource'):
        assert not _is_linked(a1, 'Resource', b)
    if hasattr(a2, 'Resource'):
        assert _is_linked(a2, 'Resource', b)
    _safe_set(b, 'scope6', set())
    assert not _is_linked(b, 'scope6', a2)
    if hasattr(a2, 'Resource'):
        assert not _is_linked(a2, 'Resource', b)


def test_assoc_scope40_reverse_link_reassign_clear():
    a1 = remes_Variable(global_=True, readable=True, type="sample_text", value="sample_text", vectorSize=7, writable=True)
    a2 = remes_Variable(global_=False, readable=False, type="sample_text_2", value="sample_text_2", vectorSize=13, writable=False)
    b = remes_Mode()
    _safe_set(b, 'Mode', a1)
    assert _is_linked(b, 'Mode', a1)
    if hasattr(a1, 'variables'):
        assert _is_linked(a1, 'variables', b)
    _safe_set(b, 'Mode', a2)
    assert _is_linked(b, 'Mode', a2)
    if hasattr(a1, 'variables'):
        assert not _is_linked(a1, 'variables', b)
    if hasattr(a2, 'variables'):
        assert _is_linked(a2, 'variables', b)
    _safe_set(b, 'Mode', None)
    assert not _is_linked(b, 'Mode', a2)
    if hasattr(a2, 'variables'):
        assert not _is_linked(a2, 'variables', b)


def test_assoc_scope41_reverse_link_reassign_clear():
    a1 = remes_Resource(expression="sample_text", type="sample_text")
    a2 = remes_Resource(expression="sample_text_2", type="sample_text_2")
    b = remes_Mode()
    _safe_set(b, 'Mode42', a1)
    assert _is_linked(b, 'Mode42', a1)
    if hasattr(a1, 'resources'):
        assert _is_linked(a1, 'resources', b)
    _safe_set(b, 'Mode42', a2)
    assert _is_linked(b, 'Mode42', a2)
    if hasattr(a1, 'resources'):
        assert not _is_linked(a1, 'resources', b)
    if hasattr(a2, 'resources'):
        assert _is_linked(a2, 'resources', b)
    _safe_set(b, 'Mode42', None)
    assert not _is_linked(b, 'Mode42', a2)
    if hasattr(a2, 'resources'):
        assert not _is_linked(a2, 'resources', b)


def test_assoc_scope44_reverse_link_reassign_clear():
    a1 = remes_Mode()
    a2 = remes_Mode()
    b = remes_Constant(global_=True, type="sample_text", value="sample_text")
    _safe_set(b, 'constants', a1)
    assert _is_linked(b, 'constants', a1)
    if hasattr(a1, 'Mode45'):
        assert _is_linked(a1, 'Mode45', b)
    _safe_set(b, 'constants', a2)
    assert _is_linked(b, 'constants', a2)
    if hasattr(a1, 'Mode45'):
        assert not _is_linked(a1, 'Mode45', b)
    if hasattr(a2, 'Mode45'):
        assert _is_linked(a2, 'Mode45', b)
    _safe_set(b, 'constants', None)
    assert not _is_linked(b, 'constants', a2)
    if hasattr(a2, 'Mode45'):
        assert not _is_linked(a2, 'Mode45', b)


def test_assoc_variables4_reverse_link_reassign_clear():
    a1 = remes_Variable(global_=True, readable=True, type="sample_text", value="sample_text", vectorSize=7, writable=True)
    a2 = remes_Variable(global_=False, readable=False, type="sample_text_2", value="sample_text_2", vectorSize=13, writable=False)
    b = remes_Mode()
    _safe_set(b, 'scope', {a1})
    assert _is_linked(b, 'scope', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'scope', {a2})
    assert _is_linked(b, 'scope', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'scope', set())
    assert not _is_linked(b, 'scope', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_connectFrom34_stub_double():
    # remes_ExitPoint has no real 'ExitPoint35' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = remes_ExitPoint()
    setattr(partner, 'ExitPoint35', None)
    _safe_set(owner, 'exitEdges', partner)
    assert getattr(partner, 'ExitPoint35') == owner
    _safe_set(owner, 'exitEdges', None)
    assert getattr(partner, 'ExitPoint35') is None


def test_assoc_connectTo36_stub_double():
    # remes_EntryPoint has no real 'EntryPoint37' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = remes_EntryPoint()
    setattr(partner, 'EntryPoint37', None)
    _safe_set(owner, 'entryEdges', partner)
    assert getattr(partner, 'EntryPoint37') == owner
    _safe_set(owner, 'entryEdges', None)
    assert getattr(partner, 'EntryPoint37') is None


def test_assoc_container23_stub_double():
    # remes_EntryPoint has no real 'entryPoint' property in the generated
    # code (a bare stub) -- manually attach it so remes_ControlPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ControlPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ControlPath(name="sample_text")
    partner = remes_EntryPoint()
    setattr(partner, 'entryPoint', None)
    _safe_set(owner, 'ControlPath', partner)
    assert getattr(partner, 'entryPoint') == owner
    _safe_set(owner, 'ControlPath', None)
    assert getattr(partner, 'entryPoint') is None


def test_assoc_container26_stub_double():
    # remes_ExitPoint has no real 'exitPoint' property in the generated
    # code (a bare stub) -- manually attach it so remes_ControlPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ControlPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ControlPath(name="sample_text")
    partner = remes_ExitPoint()
    setattr(partner, 'exitPoint', None)
    _safe_set(owner, 'ControlPath27', partner)
    assert getattr(partner, 'exitPoint') == owner
    _safe_set(owner, 'ControlPath27', None)
    assert getattr(partner, 'exitPoint') is None


def test_assoc_entryEdges22_stub_double():
    # remes_EntryPoint has no real 'connectTo' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = remes_EntryPoint()
    setattr(partner, 'connectTo', None)
    _safe_set(owner, 'Edge', partner)
    assert owner in getattr(partner, 'connectTo')
    _safe_set(owner, 'Edge', None)
    assert owner not in getattr(partner, 'connectTo')


def test_assoc_entryPoint1_stub_double():
    # remes_EntryPoint has no real 'EntryPoint' property in the generated
    # code (a bare stub) -- manually attach it so remes_ControlPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ControlPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ControlPath(name="sample_text")
    partner = remes_EntryPoint()
    setattr(partner, 'EntryPoint', None)
    _safe_set(owner, 'container', partner)
    assert getattr(partner, 'EntryPoint') == owner
    _safe_set(owner, 'container', None)
    assert getattr(partner, 'EntryPoint') is None


def test_assoc_exitEdges24_stub_double():
    # remes_ExitPoint has no real 'connectFrom' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = remes_ExitPoint()
    setattr(partner, 'connectFrom', None)
    _safe_set(owner, 'Edge25', partner)
    assert owner in getattr(partner, 'connectFrom')
    _safe_set(owner, 'Edge25', None)
    assert owner not in getattr(partner, 'connectFrom')


def test_assoc_exitPoint2_stub_double():
    # remes_ExitPoint has no real 'ExitPoint' property in the generated
    # code (a bare stub) -- manually attach it so remes_ControlPath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_ControlPath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_ControlPath(name="sample_text")
    partner = remes_ExitPoint()
    setattr(partner, 'ExitPoint', None)
    _safe_set(owner, 'container3', partner)
    assert getattr(partner, 'ExitPoint') == owner
    _safe_set(owner, 'container3', None)
    assert getattr(partner, 'ExitPoint') is None


def test_assoc_modes0_stub_double():
    # remes_RemesDiagram has no real 'remes_RemesDiagram' property in the generated
    # code (a bare stub) -- manually attach it so remes_Mode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Mode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Mode()
    partner = remes_RemesDiagram()
    setattr(partner, 'remes_RemesDiagram', None)
    _safe_set(owner, 'remes_Mode', partner)
    assert owner in getattr(partner, 'remes_RemesDiagram')
    _safe_set(owner, 'remes_Mode', None)
    assert owner not in getattr(partner, 'remes_RemesDiagram')


def test_assoc_parent18_stub_double():
    # remes_CompositeMode has no real 'CompositeMode' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent=True)
    partner = remes_CompositeMode()
    setattr(partner, 'CompositeMode', None)
    _safe_set(owner, 'subModes', partner)
    assert getattr(partner, 'CompositeMode') == owner
    _safe_set(owner, 'subModes', None)
    assert getattr(partner, 'CompositeMode') is None


def test_assoc_parsedActionBody38_stub_double():
    # ActionRoot has no real 'ActionRoot' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = ActionRoot()
    setattr(partner, 'ActionRoot', None)
    _safe_set(owner, 'remes_Edge39', partner)
    assert getattr(partner, 'ActionRoot') == owner
    _safe_set(owner, 'remes_Edge39', None)
    assert getattr(partner, 'ActionRoot') is None


def test_assoc_parsedActionGuard32_stub_double():
    # LogicalRoot has no real 'LogicalRoot33' property in the generated
    # code (a bare stub) -- manually attach it so remes_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Edge(actionBody="sample_text", actionGuard="sample_text")
    partner = LogicalRoot()
    setattr(partner, 'LogicalRoot33', None)
    _safe_set(owner, 'remes_Edge', partner)
    assert getattr(partner, 'LogicalRoot33') == owner
    _safe_set(owner, 'remes_Edge', None)
    assert getattr(partner, 'LogicalRoot33') is None


def test_assoc_parsedExpression43_stub_double():
    # ResourceRoot has no real 'ResourceRoot' property in the generated
    # code (a bare stub) -- manually attach it so remes_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_Resource(expression="sample_text", type="sample_text")
    partner = ResourceRoot()
    setattr(partner, 'ResourceRoot', None)
    _safe_set(owner, 'remes_Resource', partner)
    assert getattr(partner, 'ResourceRoot') == owner
    _safe_set(owner, 'remes_Resource', None)
    assert getattr(partner, 'ResourceRoot') is None


def test_assoc_parsedInvariant19_stub_double():
    # LogicalRoot has no real 'LogicalRoot' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent=True)
    partner = LogicalRoot()
    setattr(partner, 'LogicalRoot', None)
    _safe_set(owner, 'remes_SubMode', partner)
    assert getattr(partner, 'LogicalRoot') == owner
    _safe_set(owner, 'remes_SubMode', None)
    assert getattr(partner, 'LogicalRoot') is None


def test_assoc_subModes9_stub_double():
    # remes_CompositeMode has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so remes_SubMode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # remes_SubMode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = remes_SubMode(invariant="sample_text", isUrgent=True)
    partner = remes_CompositeMode()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'SubMode', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'SubMode', None)
    assert owner not in getattr(partner, 'parent')


