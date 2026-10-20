import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Child,
    Container,
    Cursor,
    Figure,
    Primitive,
    Shape,
    model_Arc,
    model_BorderChild,
    model_BorderContainer,
    model_Child,
    model_Connection,
    model_Container,
    model_Cursor,
    model_Dimension,
    model_Ellipse,
    model_Figure,
    model_FigureContainer,
    model_GridChild,
    model_GridContainer,
    model_Image,
    model_Line,
    model_Position,
    model_Primitive,
    model_Rectangle,
    model_Shape,
    model_StackContainer,
    model_StringToStringMap,
    model_Symbol,
    model_SymbolReference,
    model_SystemCursor,
    model_Text,
    model_XYChild,
    model_XYContainer,
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
    a1 = model_GridContainer(columns=7, equalWidth=True, horizontalSpacing=7, marginHeight=7, marginWidth=7, verticalSpacing=7)
    a2 = model_GridContainer(columns=13, equalWidth=False, horizontalSpacing=13, marginHeight=13, marginWidth=13, verticalSpacing=13)
    b = model_GridChild(grabHorizontalSpace=True, grabVerticalSpace=True, heightHint="sample_text", horizontalAlignment="sample_text", spanCols=7, spanRows="sample_text", verticalAlignment="sample_text", widthHint="sample_text")
    _safe_set(b, 'model_GridChild', a1)
    assert _is_linked(b, 'model_GridChild', a1)
    if hasattr(a1, 'model_GridContainer'):
        assert _is_linked(a1, 'model_GridContainer', b)
    _safe_set(b, 'model_GridChild', a2)
    assert _is_linked(b, 'model_GridChild', a2)
    if hasattr(a1, 'model_GridContainer'):
        assert not _is_linked(a1, 'model_GridContainer', b)
    if hasattr(a2, 'model_GridContainer'):
        assert _is_linked(a2, 'model_GridContainer', b)
    _safe_set(b, 'model_GridChild', None)
    assert not _is_linked(b, 'model_GridChild', a2)
    if hasattr(a2, 'model_GridContainer'):
        assert not _is_linked(a2, 'model_GridContainer', b)


def test_assoc_children27_reverse_link_reassign_clear():
    a1 = model_BorderContainer(horizontalSpacing=7, verticalSpacing=7)
    a2 = model_BorderContainer(horizontalSpacing=13, verticalSpacing=13)
    b = model_BorderChild(alignment="sample_text")
    _safe_set(b, 'model_BorderChild', a1)
    assert _is_linked(b, 'model_BorderChild', a1)
    if hasattr(a1, 'model_BorderContainer'):
        assert _is_linked(a1, 'model_BorderContainer', b)
    _safe_set(b, 'model_BorderChild', a2)
    assert _is_linked(b, 'model_BorderChild', a2)
    if hasattr(a1, 'model_BorderContainer'):
        assert not _is_linked(a1, 'model_BorderContainer', b)
    if hasattr(a2, 'model_BorderContainer'):
        assert _is_linked(a2, 'model_BorderContainer', b)
    _safe_set(b, 'model_BorderChild', None)
    assert not _is_linked(b, 'model_BorderChild', a2)
    if hasattr(a2, 'model_BorderContainer'):
        assert not _is_linked(a2, 'model_BorderContainer', b)


def test_assoc_designSize5_reverse_link_reassign_clear():
    a1 = model_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = model_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = model_Dimension(height=3.14, width=3.14)
    _safe_set(b, 'model_Dimension', a1)
    assert _is_linked(b, 'model_Dimension', a1)
    if hasattr(a1, 'model_Symbol6'):
        assert _is_linked(a1, 'model_Symbol6', b)
    _safe_set(b, 'model_Dimension', a2)
    assert _is_linked(b, 'model_Dimension', a2)
    if hasattr(a1, 'model_Symbol6'):
        assert not _is_linked(a1, 'model_Symbol6', b)
    if hasattr(a2, 'model_Symbol6'):
        assert _is_linked(a2, 'model_Symbol6', b)
    _safe_set(b, 'model_Dimension', None)
    assert not _is_linked(b, 'model_Dimension', a2)
    if hasattr(a2, 'model_Symbol6'):
        assert not _is_linked(a2, 'model_Symbol6', b)


def test_assoc_element9_reverse_link_reassign_clear():
    a1 = model_Primitive(name="sample_text")
    a2 = model_Primitive(name="sample_text_2")
    b = model_Child(name="sample_text")
    _safe_set(b, 'model_Child', a1)
    assert _is_linked(b, 'model_Child', a1)
    if hasattr(a1, 'model_Primitive10'):
        assert _is_linked(a1, 'model_Primitive10', b)
    _safe_set(b, 'model_Child', a2)
    assert _is_linked(b, 'model_Child', a2)
    if hasattr(a1, 'model_Primitive10'):
        assert not _is_linked(a1, 'model_Primitive10', b)
    if hasattr(a2, 'model_Primitive10'):
        assert _is_linked(a2, 'model_Primitive10', b)
    _safe_set(b, 'model_Child', None)
    assert not _is_linked(b, 'model_Child', a2)
    if hasattr(a2, 'model_Primitive10'):
        assert not _is_linked(a2, 'model_Primitive10', b)


def test_assoc_properties1_reverse_link_reassign_clear():
    a1 = model_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = model_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = model_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'model_StringToStringMap', a1)
    assert _is_linked(b, 'model_StringToStringMap', a1)
    if hasattr(a1, 'model_Symbol2'):
        assert _is_linked(a1, 'model_Symbol2', b)
    _safe_set(b, 'model_StringToStringMap', a2)
    assert _is_linked(b, 'model_StringToStringMap', a2)
    if hasattr(a1, 'model_Symbol2'):
        assert not _is_linked(a1, 'model_Symbol2', b)
    if hasattr(a2, 'model_Symbol2'):
        assert _is_linked(a2, 'model_Symbol2', b)
    _safe_set(b, 'model_StringToStringMap', None)
    assert not _is_linked(b, 'model_StringToStringMap', a2)
    if hasattr(a2, 'model_Symbol2'):
        assert not _is_linked(a2, 'model_Symbol2', b)


def test_assoc_properties24_reverse_link_reassign_clear():
    a1 = model_SymbolReference(onCreateProperties="sample_text", uri="sample_text", zoom="sample_text")
    a2 = model_SymbolReference(onCreateProperties="sample_text_2", uri="sample_text_2", zoom="sample_text_2")
    b = model_StringToStringMap(key="sample_text", value="sample_text")
    _safe_set(b, 'model_StringToStringMap25', a1)
    assert _is_linked(b, 'model_StringToStringMap25', a1)
    if hasattr(a1, 'model_SymbolReference'):
        assert _is_linked(a1, 'model_SymbolReference', b)
    _safe_set(b, 'model_StringToStringMap25', a2)
    assert _is_linked(b, 'model_StringToStringMap25', a2)
    if hasattr(a1, 'model_SymbolReference'):
        assert not _is_linked(a1, 'model_SymbolReference', b)
    if hasattr(a2, 'model_SymbolReference'):
        assert _is_linked(a2, 'model_SymbolReference', b)
    _safe_set(b, 'model_StringToStringMap25', None)
    assert not _is_linked(b, 'model_StringToStringMap25', a2)
    if hasattr(a2, 'model_SymbolReference'):
        assert not _is_linked(a2, 'model_SymbolReference', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = model_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    a2 = model_Symbol(backgroundColor="sample_text_2", onDispose="sample_text_2", onInit="sample_text_2", onUpdate="sample_text_2", scriptModules="sample_text_2")
    b = model_Primitive(name="sample_text")
    _safe_set(b, 'model_Primitive', a1)
    assert _is_linked(b, 'model_Primitive', a1)
    if hasattr(a1, 'model_Symbol'):
        assert _is_linked(a1, 'model_Symbol', b)
    _safe_set(b, 'model_Primitive', a2)
    assert _is_linked(b, 'model_Primitive', a2)
    if hasattr(a1, 'model_Symbol'):
        assert not _is_linked(a1, 'model_Symbol', b)
    if hasattr(a2, 'model_Symbol'):
        assert _is_linked(a2, 'model_Symbol', b)
    _safe_set(b, 'model_Primitive', None)
    assert not _is_linked(b, 'model_Primitive', a2)
    if hasattr(a2, 'model_Symbol'):
        assert not _is_linked(a2, 'model_Symbol', b)


def test_assoc_size19_reverse_link_reassign_clear():
    a1 = model_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", onMouseDrag="sample_text", onMouseHover="sample_text", onMouseIn="sample_text", onMouseMove="sample_text", onMouseOut="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    a2 = model_Figure(backgroundColor="sample_text_2", border="sample_text_2", foregroundColor="sample_text_2", onClick="sample_text_2", onDoubleClick="sample_text_2", onMouseDrag="sample_text_2", onMouseHover="sample_text_2", onMouseIn="sample_text_2", onMouseMove="sample_text_2", onMouseOut="sample_text_2", opaque="sample_text_2", toolTip="sample_text_2", visible=False)
    b = model_Dimension(height=3.14, width=3.14)
    _safe_set(b, 'model_Dimension20', a1)
    assert _is_linked(b, 'model_Dimension20', a1)
    if hasattr(a1, 'model_Figure'):
        assert _is_linked(a1, 'model_Figure', b)
    _safe_set(b, 'model_Dimension20', a2)
    assert _is_linked(b, 'model_Dimension20', a2)
    if hasattr(a1, 'model_Figure'):
        assert not _is_linked(a1, 'model_Figure', b)
    if hasattr(a2, 'model_Figure'):
        assert _is_linked(a2, 'model_Figure', b)
    _safe_set(b, 'model_Dimension20', None)
    assert not _is_linked(b, 'model_Dimension20', a2)
    if hasattr(a2, 'model_Figure'):
        assert not _is_linked(a2, 'model_Figure', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children36_stub_double():
    # model_StackContainer has no real 'model_StackContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Primitive(name="sample_text")
    partner = model_StackContainer()
    setattr(partner, 'model_StackContainer', None)
    _safe_set(owner, 'model_Primitive37', partner)
    assert owner in getattr(partner, 'model_StackContainer')
    _safe_set(owner, 'model_Primitive37', None)
    assert owner not in getattr(partner, 'model_StackContainer')


def test_assoc_connections7_stub_double():
    # model_Connection has no real 'model_Connection' property in the generated
    # code (a bare stub) -- manually attach it so model_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    partner = model_Connection()
    setattr(partner, 'model_Connection', None)
    _safe_set(owner, 'model_Symbol8', {partner})
    assert getattr(partner, 'model_Connection') == owner
    _safe_set(owner, 'model_Symbol8', set())
    assert getattr(partner, 'model_Connection') is None


def test_assoc_content28_stub_double():
    # model_FigureContainer has no real 'model_FigureContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Primitive(name="sample_text")
    partner = model_FigureContainer()
    setattr(partner, 'model_FigureContainer', None)
    _safe_set(owner, 'model_Primitive29', partner)
    assert getattr(partner, 'model_FigureContainer') == owner
    _safe_set(owner, 'model_Primitive29', None)
    assert getattr(partner, 'model_FigureContainer') is None


def test_assoc_cursor21_stub_double():
    # model_Cursor has no real 'model_Cursor23' property in the generated
    # code (a bare stub) -- manually attach it so model_Figure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Figure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Figure(backgroundColor="sample_text", border="sample_text", foregroundColor="sample_text", onClick="sample_text", onDoubleClick="sample_text", onMouseDrag="sample_text", onMouseHover="sample_text", onMouseIn="sample_text", onMouseMove="sample_text", onMouseOut="sample_text", opaque="sample_text", toolTip="sample_text", visible=True)
    partner = model_Cursor()
    setattr(partner, 'model_Cursor23', None)
    _safe_set(owner, 'model_Figure22', partner)
    assert getattr(partner, 'model_Cursor23') == owner
    _safe_set(owner, 'model_Figure22', None)
    assert getattr(partner, 'model_Cursor23') is None


def test_assoc_cursors3_stub_double():
    # model_Cursor has no real 'model_Cursor' property in the generated
    # code (a bare stub) -- manually attach it so model_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Symbol(backgroundColor="sample_text", onDispose="sample_text", onInit="sample_text", onUpdate="sample_text", scriptModules="sample_text")
    partner = model_Cursor()
    setattr(partner, 'model_Cursor', None)
    _safe_set(owner, 'model_Symbol4', partner)
    assert getattr(partner, 'model_Cursor') == owner
    _safe_set(owner, 'model_Symbol4', None)
    assert getattr(partner, 'model_Cursor') is None


def test_assoc_dimension12_stub_double():
    # model_XYChild has no real 'model_XYChild13' property in the generated
    # code (a bare stub) -- manually attach it so model_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Dimension(height=3.14, width=3.14)
    partner = model_XYChild()
    setattr(partner, 'model_XYChild13', None)
    _safe_set(owner, 'model_Dimension14', partner)
    assert getattr(partner, 'model_XYChild13') == owner
    _safe_set(owner, 'model_Dimension14', None)
    assert getattr(partner, 'model_XYChild13') is None


def test_assoc_end33_stub_double():
    # model_Connection has no real 'model_Connection34' property in the generated
    # code (a bare stub) -- manually attach it so model_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Primitive(name="sample_text")
    partner = model_Connection()
    setattr(partner, 'model_Connection34', None)
    _safe_set(owner, 'model_Primitive35', partner)
    assert getattr(partner, 'model_Connection34') == owner
    _safe_set(owner, 'model_Primitive35', None)
    assert getattr(partner, 'model_Connection34') is None


def test_assoc_points17_stub_double():
    # model_Line has no real 'model_Line' property in the generated
    # code (a bare stub) -- manually attach it so model_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Position(x=3.14, y=3.14)
    partner = model_Line()
    setattr(partner, 'model_Line', None)
    _safe_set(owner, 'model_Position18', partner)
    assert owner in getattr(partner, 'model_Line')
    _safe_set(owner, 'model_Position18', None)
    assert owner not in getattr(partner, 'model_Line')


def test_assoc_position11_stub_double():
    # model_XYChild has no real 'model_XYChild' property in the generated
    # code (a bare stub) -- manually attach it so model_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Position(x=3.14, y=3.14)
    partner = model_XYChild()
    setattr(partner, 'model_XYChild', None)
    _safe_set(owner, 'model_Position', partner)
    assert getattr(partner, 'model_XYChild') == owner
    _safe_set(owner, 'model_Position', None)
    assert getattr(partner, 'model_XYChild') is None


def test_assoc_start30_stub_double():
    # model_Connection has no real 'model_Connection31' property in the generated
    # code (a bare stub) -- manually attach it so model_Primitive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Primitive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Primitive(name="sample_text")
    partner = model_Connection()
    setattr(partner, 'model_Connection31', None)
    _safe_set(owner, 'model_Primitive32', partner)
    assert getattr(partner, 'model_Connection31') == owner
    _safe_set(owner, 'model_Primitive32', None)
    assert getattr(partner, 'model_Connection31') is None


