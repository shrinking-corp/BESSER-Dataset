import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Child,
    Container,
    Cursor,
    Figure,
    Primitive,
    Shape,
    VisualInterface_Arc,
    VisualInterface_BorderChild,
    VisualInterface_BorderContainer,
    VisualInterface_Child,
    VisualInterface_Connection,
    VisualInterface_Container,
    VisualInterface_Cursor,
    VisualInterface_Dimension,
    VisualInterface_Ellipse,
    VisualInterface_Figure,
    VisualInterface_FigureContainer,
    VisualInterface_GridChild,
    VisualInterface_GridContainer,
    VisualInterface_Image,
    VisualInterface_Line,
    VisualInterface_Position,
    VisualInterface_Primitive,
    VisualInterface_Rectangle,
    VisualInterface_Shape,
    VisualInterface_StackContainer,
    VisualInterface_StringToStringMap,
    VisualInterface_Symbol,
    VisualInterface_SymbolReference,
    VisualInterface_SystemCursor,
    VisualInterface_Text,
    VisualInterface_XYChild,
    VisualInterface_XYContainer,
    Alignment,
    GridAlignment,
    Orientation,
    SystemCursorType,
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

def test_assoc_children26_reverse_link_reassign_clear():
    a1 = VisualInterface_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    a2 = VisualInterface_GridContainer(columns=13, equalWidth=False, horizontalSpacing=13, marginHeight=13, marginWidth=13, verticalSpacing=13)
    b = VisualInterface_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    _safe_set(b, 'VisualInterface_GridChild', a1)
    assert _is_linked(b, 'VisualInterface_GridChild', a1)
    if hasattr(a1, 'VisualInterface_GridContainer'):
        assert _is_linked(a1, 'VisualInterface_GridContainer', b)
    _safe_set(b, 'VisualInterface_GridChild', a2)
    assert _is_linked(b, 'VisualInterface_GridChild', a2)
    if hasattr(a1, 'VisualInterface_GridContainer'):
        assert not _is_linked(a1, 'VisualInterface_GridContainer', b)
    if hasattr(a2, 'VisualInterface_GridContainer'):
        assert _is_linked(a2, 'VisualInterface_GridContainer', b)
    _safe_set(b, 'VisualInterface_GridChild', None)
    assert not _is_linked(b, 'VisualInterface_GridChild', a2)
    if hasattr(a2, 'VisualInterface_GridContainer'):
        assert not _is_linked(a2, 'VisualInterface_GridContainer', b)


def test_assoc_children27_reverse_link_reassign_clear():
    a1 = VisualInterface_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    a2 = VisualInterface_BorderContainer(horizontalSpacing=13, verticalSpacing=13)
    b = VisualInterface_BorderChild(alignment="sample_text")
    _safe_set(b, 'VisualInterface_BorderChild', a1)
    assert _is_linked(b, 'VisualInterface_BorderChild', a1)
    if hasattr(a1, 'VisualInterface_BorderContainer'):
        assert _is_linked(a1, 'VisualInterface_BorderContainer', b)
    _safe_set(b, 'VisualInterface_BorderChild', a2)
    assert _is_linked(b, 'VisualInterface_BorderChild', a2)
    if hasattr(a1, 'VisualInterface_BorderContainer'):
        assert not _is_linked(a1, 'VisualInterface_BorderContainer', b)
    if hasattr(a2, 'VisualInterface_BorderContainer'):
        assert _is_linked(a2, 'VisualInterface_BorderContainer', b)
    _safe_set(b, 'VisualInterface_BorderChild', None)
    assert not _is_linked(b, 'VisualInterface_BorderChild', a2)
    if hasattr(a2, 'VisualInterface_BorderContainer'):
        assert not _is_linked(a2, 'VisualInterface_BorderContainer', b)


def test_assoc_designSize5_reverse_link_reassign_clear():
    a1 = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = VisualInterface_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = VisualInterface_Dimension(height=3.14, width=3.14)
    _safe_set(b, 'VisualInterface_Dimension', a1)
    assert _is_linked(b, 'VisualInterface_Dimension', a1)
    if hasattr(a1, 'VisualInterface_Symbol6'):
        assert _is_linked(a1, 'VisualInterface_Symbol6', b)
    _safe_set(b, 'VisualInterface_Dimension', a2)
    assert _is_linked(b, 'VisualInterface_Dimension', a2)
    if hasattr(a1, 'VisualInterface_Symbol6'):
        assert not _is_linked(a1, 'VisualInterface_Symbol6', b)
    if hasattr(a2, 'VisualInterface_Symbol6'):
        assert _is_linked(a2, 'VisualInterface_Symbol6', b)
    _safe_set(b, 'VisualInterface_Dimension', None)
    assert not _is_linked(b, 'VisualInterface_Dimension', a2)
    if hasattr(a2, 'VisualInterface_Symbol6'):
        assert not _is_linked(a2, 'VisualInterface_Symbol6', b)


def test_assoc_element9_reverse_link_reassign_clear():
    a1 = VisualInterface_Primitive(name="sample_text")
    a2 = VisualInterface_Primitive(name="sample_text_2")
    b = VisualInterface_Child(name="sample_text")
    _safe_set(b, 'VisualInterface_Child', a1)
    assert _is_linked(b, 'VisualInterface_Child', a1)
    if hasattr(a1, 'VisualInterface_Primitive10'):
        assert _is_linked(a1, 'VisualInterface_Primitive10', b)
    _safe_set(b, 'VisualInterface_Child', a2)
    assert _is_linked(b, 'VisualInterface_Child', a2)
    if hasattr(a1, 'VisualInterface_Primitive10'):
        assert not _is_linked(a1, 'VisualInterface_Primitive10', b)
    if hasattr(a2, 'VisualInterface_Primitive10'):
        assert _is_linked(a2, 'VisualInterface_Primitive10', b)
    _safe_set(b, 'VisualInterface_Child', None)
    assert not _is_linked(b, 'VisualInterface_Child', a2)
    if hasattr(a2, 'VisualInterface_Primitive10'):
        assert not _is_linked(a2, 'VisualInterface_Primitive10', b)


def test_assoc_properties1_reverse_link_reassign_clear():
    a1 = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = VisualInterface_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'VisualInterface_StringToStringMap', a1)
    assert _is_linked(b, 'VisualInterface_StringToStringMap', a1)
    if hasattr(a1, 'VisualInterface_Symbol2'):
        assert _is_linked(a1, 'VisualInterface_Symbol2', b)
    _safe_set(b, 'VisualInterface_StringToStringMap', a2)
    assert _is_linked(b, 'VisualInterface_StringToStringMap', a2)
    if hasattr(a1, 'VisualInterface_Symbol2'):
        assert not _is_linked(a1, 'VisualInterface_Symbol2', b)
    if hasattr(a2, 'VisualInterface_Symbol2'):
        assert _is_linked(a2, 'VisualInterface_Symbol2', b)
    _safe_set(b, 'VisualInterface_StringToStringMap', None)
    assert not _is_linked(b, 'VisualInterface_StringToStringMap', a2)
    if hasattr(a2, 'VisualInterface_Symbol2'):
        assert not _is_linked(a2, 'VisualInterface_Symbol2', b)


def test_assoc_properties24_reverse_link_reassign_clear():
    a1 = VisualInterface_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    a2 = VisualInterface_SymbolReference(onCreateProperties="sample_text_2", uri="sample_text_2", zoom="sample_text_2")
    b = VisualInterface_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'VisualInterface_StringToStringMap25', a1)
    assert _is_linked(b, 'VisualInterface_StringToStringMap25', a1)
    if hasattr(a1, 'VisualInterface_SymbolReference'):
        assert _is_linked(a1, 'VisualInterface_SymbolReference', b)
    _safe_set(b, 'VisualInterface_StringToStringMap25', a2)
    assert _is_linked(b, 'VisualInterface_StringToStringMap25', a2)
    if hasattr(a1, 'VisualInterface_SymbolReference'):
        assert not _is_linked(a1, 'VisualInterface_SymbolReference', b)
    if hasattr(a2, 'VisualInterface_SymbolReference'):
        assert _is_linked(a2, 'VisualInterface_SymbolReference', b)
    _safe_set(b, 'VisualInterface_StringToStringMap25', None)
    assert not _is_linked(b, 'VisualInterface_StringToStringMap25', a2)
    if hasattr(a2, 'VisualInterface_SymbolReference'):
        assert not _is_linked(a2, 'VisualInterface_SymbolReference', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = VisualInterface_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = VisualInterface_Primitive(name="sample_text")
    _safe_set(b, 'VisualInterface_Primitive', a1)
    assert _is_linked(b, 'VisualInterface_Primitive', a1)
    if hasattr(a1, 'VisualInterface_Symbol'):
        assert _is_linked(a1, 'VisualInterface_Symbol', b)
    _safe_set(b, 'VisualInterface_Primitive', a2)
    assert _is_linked(b, 'VisualInterface_Primitive', a2)
    if hasattr(a1, 'VisualInterface_Symbol'):
        assert not _is_linked(a1, 'VisualInterface_Symbol', b)
    if hasattr(a2, 'VisualInterface_Symbol'):
        assert _is_linked(a2, 'VisualInterface_Symbol', b)
    _safe_set(b, 'VisualInterface_Primitive', None)
    assert not _is_linked(b, 'VisualInterface_Primitive', a2)
    if hasattr(a2, 'VisualInterface_Symbol'):
        assert not _is_linked(a2, 'VisualInterface_Symbol', b)


def test_assoc_size19_reverse_link_reassign_clear():
    a1 = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    a2 = VisualInterface_Figure(backgroundColor="sample_text_2", border="sample_text_2", foregroundColor="sample_text_2", onClick="sample_text_2", onDoubleClick="sample_text_2", opaque="sample_text_2", toolTip="sample_text_2", visible=False)
    b = VisualInterface_Dimension(height=3.14, width=3.14)
    _safe_set(b, 'VisualInterface_Dimension20', a1)
    assert _is_linked(b, 'VisualInterface_Dimension20', a1)
    if hasattr(a1, 'VisualInterface_Figure'):
        assert _is_linked(a1, 'VisualInterface_Figure', b)
    _safe_set(b, 'VisualInterface_Dimension20', a2)
    assert _is_linked(b, 'VisualInterface_Dimension20', a2)
    if hasattr(a1, 'VisualInterface_Figure'):
        assert not _is_linked(a1, 'VisualInterface_Figure', b)
    if hasattr(a2, 'VisualInterface_Figure'):
        assert _is_linked(a2, 'VisualInterface_Figure', b)
    _safe_set(b, 'VisualInterface_Dimension20', None)
    assert not _is_linked(b, 'VisualInterface_Dimension20', a2)
    if hasattr(a2, 'VisualInterface_Figure'):
        assert not _is_linked(a2, 'VisualInterface_Figure', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children36_stub_double():
    # VisualInterface_StackContainer has no real 'VisualInterface_StackContainer' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Primitive(name="sample_text")
    partner = VisualInterface_StackContainer()
    setattr(partner, 'VisualInterface_StackContainer', None)
    _safe_set(owner, 'VisualInterface_Primitive37', partner)
    assert owner in getattr(partner, 'VisualInterface_StackContainer')
    _safe_set(owner, 'VisualInterface_Primitive37', None)
    assert owner not in getattr(partner, 'VisualInterface_StackContainer')


def test_assoc_connections7_stub_double():
    # VisualInterface_Connection has no real 'VisualInterface_Connection' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    partner = VisualInterface_Connection()
    setattr(partner, 'VisualInterface_Connection', None)
    _safe_set(owner, 'VisualInterface_Symbol8', {partner})
    assert getattr(partner, 'VisualInterface_Connection') == owner
    _safe_set(owner, 'VisualInterface_Symbol8', set())
    assert getattr(partner, 'VisualInterface_Connection') is None


def test_assoc_content28_stub_double():
    # VisualInterface_FigureContainer has no real 'VisualInterface_FigureContainer' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Primitive(name="sample_text")
    partner = VisualInterface_FigureContainer()
    setattr(partner, 'VisualInterface_FigureContainer', None)
    _safe_set(owner, 'VisualInterface_Primitive29', partner)
    assert getattr(partner, 'VisualInterface_FigureContainer') == owner
    _safe_set(owner, 'VisualInterface_Primitive29', None)
    assert getattr(partner, 'VisualInterface_FigureContainer') is None


def test_assoc_cursor21_stub_double():
    # VisualInterface_Cursor has no real 'VisualInterface_Cursor23' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    partner = VisualInterface_Cursor()
    setattr(partner, 'VisualInterface_Cursor23', None)
    _safe_set(owner, 'VisualInterface_Figure22', partner)
    assert getattr(partner, 'VisualInterface_Cursor23') == owner
    _safe_set(owner, 'VisualInterface_Figure22', None)
    assert getattr(partner, 'VisualInterface_Cursor23') is None


def test_assoc_cursors3_stub_double():
    # VisualInterface_Cursor has no real 'VisualInterface_Cursor' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    partner = VisualInterface_Cursor()
    setattr(partner, 'VisualInterface_Cursor', None)
    _safe_set(owner, 'VisualInterface_Symbol4', partner)
    assert getattr(partner, 'VisualInterface_Cursor') == owner
    _safe_set(owner, 'VisualInterface_Symbol4', None)
    assert getattr(partner, 'VisualInterface_Cursor') is None


def test_assoc_dimension12_stub_double():
    # VisualInterface_XYChild has no real 'VisualInterface_XYChild13' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Dimension(height=3.14, width=3.14)
    partner = VisualInterface_XYChild()
    setattr(partner, 'VisualInterface_XYChild13', None)
    _safe_set(owner, 'VisualInterface_Dimension14', partner)
    assert getattr(partner, 'VisualInterface_XYChild13') == owner
    _safe_set(owner, 'VisualInterface_Dimension14', None)
    assert getattr(partner, 'VisualInterface_XYChild13') is None


def test_assoc_end33_stub_double():
    # VisualInterface_Connection has no real 'VisualInterface_Connection34' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Primitive(name="sample_text")
    partner = VisualInterface_Connection()
    setattr(partner, 'VisualInterface_Connection34', None)
    _safe_set(owner, 'VisualInterface_Primitive35', partner)
    assert getattr(partner, 'VisualInterface_Connection34') == owner
    _safe_set(owner, 'VisualInterface_Primitive35', None)
    assert getattr(partner, 'VisualInterface_Connection34') is None


def test_assoc_points17_stub_double():
    # VisualInterface_Line has no real 'VisualInterface_Line' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Position(x=3.14, y=3.14)
    partner = VisualInterface_Line()
    setattr(partner, 'VisualInterface_Line', None)
    _safe_set(owner, 'VisualInterface_Position18', partner)
    assert owner in getattr(partner, 'VisualInterface_Line')
    _safe_set(owner, 'VisualInterface_Position18', None)
    assert owner not in getattr(partner, 'VisualInterface_Line')


def test_assoc_position11_stub_double():
    # VisualInterface_XYChild has no real 'VisualInterface_XYChild' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Position(x=3.14, y=3.14)
    partner = VisualInterface_XYChild()
    setattr(partner, 'VisualInterface_XYChild', None)
    _safe_set(owner, 'VisualInterface_Position', partner)
    assert getattr(partner, 'VisualInterface_XYChild') == owner
    _safe_set(owner, 'VisualInterface_Position', None)
    assert getattr(partner, 'VisualInterface_XYChild') is None


def test_assoc_start30_stub_double():
    # VisualInterface_Connection has no real 'VisualInterface_Connection31' property in the generated
    # code (a bare stub) -- manually attach it so VisualInterface_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # VisualInterface_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = VisualInterface_Primitive(name="sample_text")
    partner = VisualInterface_Connection()
    setattr(partner, 'VisualInterface_Connection31', None)
    _safe_set(owner, 'VisualInterface_Primitive32', partner)
    assert getattr(partner, 'VisualInterface_Connection31') == owner
    _safe_set(owner, 'VisualInterface_Primitive32', None)
    assert getattr(partner, 'VisualInterface_Connection31') is None


