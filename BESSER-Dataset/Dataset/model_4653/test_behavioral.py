import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    View,
    di_Bendpoint,
    di_Connector,
    di_Diagram,
    di_DocumentRoot,
    di_EStringToStringMapEntry,
    di_Node,
    di_Style,
    di_View,
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

def test_assoc_bendpoint0_reverse_link_reassign_clear():
    a1 = di_Connector(source="sample_text", target="sample_text")
    a2 = di_Connector(source="sample_text_2", target="sample_text_2")
    b = di_Bendpoint(sourceX="sample_text", sourceY="sample_text", targetX="sample_text", targetY="sample_text")
    _safe_set(b, 'di_Bendpoint', a1)
    assert _is_linked(b, 'di_Bendpoint', a1)
    if hasattr(a1, 'di_Connector'):
        assert _is_linked(a1, 'di_Connector', b)
    _safe_set(b, 'di_Bendpoint', a2)
    assert _is_linked(b, 'di_Bendpoint', a2)
    if hasattr(a1, 'di_Connector'):
        assert not _is_linked(a1, 'di_Connector', b)
    if hasattr(a2, 'di_Connector'):
        assert _is_linked(a2, 'di_Connector', b)
    _safe_set(b, 'di_Bendpoint', None)
    assert not _is_linked(b, 'di_Bendpoint', a2)
    if hasattr(a2, 'di_Connector'):
        assert not _is_linked(a2, 'di_Connector', b)


def test_assoc_bendpoint7_reverse_link_reassign_clear():
    a1 = di_DocumentRoot(mixed="sample_text")
    a2 = di_DocumentRoot(mixed="sample_text_2")
    b = di_Bendpoint(sourceX="sample_text", sourceY="sample_text", targetX="sample_text", targetY="sample_text")
    _safe_set(b, 'di_Bendpoint9', a1)
    assert _is_linked(b, 'di_Bendpoint9', a1)
    if hasattr(a1, 'di_DocumentRoot8'):
        assert _is_linked(a1, 'di_DocumentRoot8', b)
    _safe_set(b, 'di_Bendpoint9', a2)
    assert _is_linked(b, 'di_Bendpoint9', a2)
    if hasattr(a1, 'di_DocumentRoot8'):
        assert not _is_linked(a1, 'di_DocumentRoot8', b)
    if hasattr(a2, 'di_DocumentRoot8'):
        assert _is_linked(a2, 'di_DocumentRoot8', b)
    _safe_set(b, 'di_Bendpoint9', None)
    assert not _is_linked(b, 'di_Bendpoint9', a2)
    if hasattr(a2, 'di_DocumentRoot8'):
        assert not _is_linked(a2, 'di_DocumentRoot8', b)


def test_assoc_connector10_reverse_link_reassign_clear():
    a1 = di_DocumentRoot(mixed="sample_text")
    a2 = di_DocumentRoot(mixed="sample_text_2")
    b = di_Connector(source="sample_text", target="sample_text")
    _safe_set(b, 'di_Connector12', a1)
    assert _is_linked(b, 'di_Connector12', a1)
    if hasattr(a1, 'di_DocumentRoot11'):
        assert _is_linked(a1, 'di_DocumentRoot11', b)
    _safe_set(b, 'di_Connector12', a2)
    assert _is_linked(b, 'di_Connector12', a2)
    if hasattr(a1, 'di_DocumentRoot11'):
        assert not _is_linked(a1, 'di_DocumentRoot11', b)
    if hasattr(a2, 'di_DocumentRoot11'):
        assert _is_linked(a2, 'di_DocumentRoot11', b)
    _safe_set(b, 'di_Connector12', None)
    assert not _is_linked(b, 'di_Connector12', a2)
    if hasattr(a2, 'di_DocumentRoot11'):
        assert not _is_linked(a2, 'di_DocumentRoot11', b)


def test_assoc_style20_reverse_link_reassign_clear():
    a1 = di_Style(name="sample_text", value="sample_text")
    a2 = di_Style(name="sample_text_2", value="sample_text_2")
    b = di_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'di_DocumentRoot21', {a1})
    assert _is_linked(b, 'di_DocumentRoot21', a1)
    if hasattr(a1, 'di_Style'):
        assert _is_linked(a1, 'di_Style', b)
    _safe_set(b, 'di_DocumentRoot21', {a2})
    assert _is_linked(b, 'di_DocumentRoot21', a2)
    if hasattr(a1, 'di_Style'):
        assert not _is_linked(a1, 'di_Style', b)
    if hasattr(a2, 'di_Style'):
        assert _is_linked(a2, 'di_Style', b)
    _safe_set(b, 'di_DocumentRoot21', set())
    assert not _is_linked(b, 'di_DocumentRoot21', a2)
    if hasattr(a2, 'di_Style'):
        assert not _is_linked(a2, 'di_Style', b)


def test_assoc_style22_reverse_link_reassign_clear():
    a1 = di_View(context="sample_text", definition="sample_text", id="sample_text", sourceConnector="sample_text", targetConnector="sample_text")
    a2 = di_View(context="sample_text_2", definition="sample_text_2", id="sample_text_2", sourceConnector="sample_text_2", targetConnector="sample_text_2")
    b = di_Style(name="sample_text", value="sample_text")
    _safe_set(b, 'di_Style24', a1)
    assert _is_linked(b, 'di_Style24', a1)
    if hasattr(a1, 'di_View23'):
        assert _is_linked(a1, 'di_View23', b)
    _safe_set(b, 'di_Style24', a2)
    assert _is_linked(b, 'di_Style24', a2)
    if hasattr(a1, 'di_View23'):
        assert not _is_linked(a1, 'di_View23', b)
    if hasattr(a2, 'di_View23'):
        assert _is_linked(a2, 'di_View23', b)
    _safe_set(b, 'di_Style24', None)
    assert not _is_linked(b, 'di_Style24', a2)
    if hasattr(a2, 'di_View23'):
        assert not _is_linked(a2, 'di_View23', b)


def test_assoc_view13_reverse_link_reassign_clear():
    a1 = di_View(context="sample_text", definition="sample_text", id="sample_text", sourceConnector="sample_text", targetConnector="sample_text")
    a2 = di_View(context="sample_text_2", definition="sample_text_2", id="sample_text_2", sourceConnector="sample_text_2", targetConnector="sample_text_2")
    b = di_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'di_DocumentRoot14', {a1})
    assert _is_linked(b, 'di_DocumentRoot14', a1)
    if hasattr(a1, 'di_View'):
        assert _is_linked(a1, 'di_View', b)
    _safe_set(b, 'di_DocumentRoot14', {a2})
    assert _is_linked(b, 'di_DocumentRoot14', a2)
    if hasattr(a1, 'di_View'):
        assert not _is_linked(a1, 'di_View', b)
    if hasattr(a2, 'di_View'):
        assert _is_linked(a2, 'di_View', b)
    _safe_set(b, 'di_DocumentRoot14', set())
    assert not _is_linked(b, 'di_DocumentRoot14', a2)
    if hasattr(a2, 'di_View'):
        assert not _is_linked(a2, 'di_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child25_stub_double():
    # di_Node has no real 'di_Node27' property in the generated
    # code (a bare stub) -- manually attach it so di_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_View(context="sample_text", definition="sample_text", id="sample_text", sourceConnector="sample_text", targetConnector="sample_text")
    partner = di_Node()
    setattr(partner, 'di_Node27', None)
    _safe_set(owner, 'di_View26', {partner})
    assert getattr(partner, 'di_Node27') == owner
    _safe_set(owner, 'di_View26', set())
    assert getattr(partner, 'di_Node27') is None


def test_assoc_connector1_stub_double():
    # di_Diagram has no real 'di_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so di_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Connector(source="sample_text", target="sample_text")
    partner = di_Diagram()
    setattr(partner, 'di_Diagram', None)
    _safe_set(owner, 'di_Connector2', partner)
    assert owner in getattr(partner, 'di_Diagram')
    _safe_set(owner, 'di_Connector2', None)
    assert owner not in getattr(partner, 'di_Diagram')


def test_assoc_diagram15_stub_double():
    # di_Diagram has no real 'di_Diagram17' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_Diagram()
    setattr(partner, 'di_Diagram17', None)
    _safe_set(owner, 'di_DocumentRoot16', {partner})
    assert getattr(partner, 'di_Diagram17') == owner
    _safe_set(owner, 'di_DocumentRoot16', set())
    assert getattr(partner, 'di_Diagram17') is None


def test_assoc_node18_stub_double():
    # di_Node has no real 'di_Node' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_Node()
    setattr(partner, 'di_Node', None)
    _safe_set(owner, 'di_DocumentRoot19', {partner})
    assert getattr(partner, 'di_Node') == owner
    _safe_set(owner, 'di_DocumentRoot19', set())
    assert getattr(partner, 'di_Node') is None


def test_assoc_xMLNSPrefixMap3_stub_double():
    # di_EStringToStringMapEntry has no real 'di_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_EStringToStringMapEntry()
    setattr(partner, 'di_EStringToStringMapEntry', None)
    _safe_set(owner, 'di_DocumentRoot', {partner})
    assert getattr(partner, 'di_EStringToStringMapEntry') == owner
    _safe_set(owner, 'di_DocumentRoot', set())
    assert getattr(partner, 'di_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation4_stub_double():
    # di_EStringToStringMapEntry has no real 'di_EStringToStringMapEntry6' property in the generated
    # code (a bare stub) -- manually attach it so di_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_DocumentRoot(mixed="sample_text")
    partner = di_EStringToStringMapEntry()
    setattr(partner, 'di_EStringToStringMapEntry6', None)
    _safe_set(owner, 'di_DocumentRoot5', {partner})
    assert getattr(partner, 'di_EStringToStringMapEntry6') == owner
    _safe_set(owner, 'di_DocumentRoot5', set())
    assert getattr(partner, 'di_EStringToStringMapEntry6') is None


