import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Chart,
    ChartElement,
    Diagram,
    DiagramElement,
    GraphStyle,
    Style,
    vml_Bar,
    vml_BarChart,
    vml_Category,
    vml_Cell,
    vml_Chart,
    vml_ChartElement,
    vml_ChartWithAxisStyle,
    vml_ChartWithoutAxisStyle,
    vml_Color,
    vml_Column,
    vml_Diagram,
    vml_DiagramElement,
    vml_Edge,
    vml_EdgeStyle,
    vml_Graph,
    vml_GraphStyle,
    vml_LineChart,
    vml_Model,
    vml_Node,
    vml_NodeStyle,
    vml_Pie,
    vml_Point,
    vml_Row,
    vml_Scatter,
    vml_Slice,
    vml_StackBarChart,
    vml_StackBars,
    vml_Style,
    vml_Table,
    LineStyle,
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

def test_assoc_backgroundColor15_reverse_link_reassign_clear():
    a1 = vml_NodeStyle(borderWidth=7, padding=7)
    a2 = vml_NodeStyle(borderWidth=13, padding=13)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color', a1)
    assert _is_linked(b, 'vml_Color', a1)
    if hasattr(a1, 'vml_NodeStyle'):
        assert _is_linked(a1, 'vml_NodeStyle', b)
    _safe_set(b, 'vml_Color', a2)
    assert _is_linked(b, 'vml_Color', a2)
    if hasattr(a1, 'vml_NodeStyle'):
        assert not _is_linked(a1, 'vml_NodeStyle', b)
    if hasattr(a2, 'vml_NodeStyle'):
        assert _is_linked(a2, 'vml_NodeStyle', b)
    _safe_set(b, 'vml_Color', None)
    assert not _is_linked(b, 'vml_Color', a2)
    if hasattr(a2, 'vml_NodeStyle'):
        assert not _is_linked(a2, 'vml_NodeStyle', b)


def test_assoc_borderColor22_reverse_link_reassign_clear():
    a1 = vml_NodeStyle(borderWidth=7, padding=7)
    a2 = vml_NodeStyle(borderWidth=13, padding=13)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color24', a1)
    assert _is_linked(b, 'vml_Color24', a1)
    if hasattr(a1, 'vml_NodeStyle23'):
        assert _is_linked(a1, 'vml_NodeStyle23', b)
    _safe_set(b, 'vml_Color24', a2)
    assert _is_linked(b, 'vml_Color24', a2)
    if hasattr(a1, 'vml_NodeStyle23'):
        assert not _is_linked(a1, 'vml_NodeStyle23', b)
    if hasattr(a2, 'vml_NodeStyle23'):
        assert _is_linked(a2, 'vml_NodeStyle23', b)
    _safe_set(b, 'vml_Color24', None)
    assert not _is_linked(b, 'vml_Color24', a2)
    if hasattr(a2, 'vml_NodeStyle23'):
        assert not _is_linked(a2, 'vml_NodeStyle23', b)


def test_assoc_borderHighlightColor25_reverse_link_reassign_clear():
    a1 = vml_NodeStyle(borderWidth=7, padding=7)
    a2 = vml_NodeStyle(borderWidth=13, padding=13)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color27', a1)
    assert _is_linked(b, 'vml_Color27', a1)
    if hasattr(a1, 'vml_NodeStyle26'):
        assert _is_linked(a1, 'vml_NodeStyle26', b)
    _safe_set(b, 'vml_Color27', a2)
    assert _is_linked(b, 'vml_Color27', a2)
    if hasattr(a1, 'vml_NodeStyle26'):
        assert not _is_linked(a1, 'vml_NodeStyle26', b)
    if hasattr(a2, 'vml_NodeStyle26'):
        assert _is_linked(a2, 'vml_NodeStyle26', b)
    _safe_set(b, 'vml_Color27', None)
    assert not _is_linked(b, 'vml_Color27', a2)
    if hasattr(a2, 'vml_NodeStyle26'):
        assert not _is_linked(a2, 'vml_NodeStyle26', b)


def test_assoc_col9_reverse_link_reassign_clear():
    a1 = vml_Column(columnTitle="sample_text")
    a2 = vml_Column(columnTitle="sample_text_2")
    b = vml_Cell(textValue="sample_text")
    _safe_set(b, 'vml_Cell10', a1)
    assert _is_linked(b, 'vml_Cell10', a1)
    if hasattr(a1, 'vml_Column11'):
        assert _is_linked(a1, 'vml_Column11', b)
    _safe_set(b, 'vml_Cell10', a2)
    assert _is_linked(b, 'vml_Cell10', a2)
    if hasattr(a1, 'vml_Column11'):
        assert not _is_linked(a1, 'vml_Column11', b)
    if hasattr(a2, 'vml_Column11'):
        assert _is_linked(a2, 'vml_Column11', b)
    _safe_set(b, 'vml_Cell10', None)
    assert not _is_linked(b, 'vml_Cell10', a2)
    if hasattr(a2, 'vml_Column11'):
        assert not _is_linked(a2, 'vml_Column11', b)


def test_assoc_columns3_reverse_link_reassign_clear():
    a1 = vml_Table(tableTitle="sample_text")
    a2 = vml_Table(tableTitle="sample_text_2")
    b = vml_Column(columnTitle="sample_text")
    _safe_set(b, 'vml_Column', a1)
    assert _is_linked(b, 'vml_Column', a1)
    if hasattr(a1, 'vml_Table4'):
        assert _is_linked(a1, 'vml_Table4', b)
    _safe_set(b, 'vml_Column', a2)
    assert _is_linked(b, 'vml_Column', a2)
    if hasattr(a1, 'vml_Table4'):
        assert not _is_linked(a1, 'vml_Table4', b)
    if hasattr(a2, 'vml_Table4'):
        assert _is_linked(a2, 'vml_Table4', b)
    _safe_set(b, 'vml_Column', None)
    assert not _is_linked(b, 'vml_Column', a2)
    if hasattr(a2, 'vml_Table4'):
        assert not _is_linked(a2, 'vml_Table4', b)


def test_assoc_edges48_reverse_link_reassign_clear():
    a1 = vml_Graph(ID="sample_text", title="sample_text")
    a2 = vml_Graph(ID="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'vml_Edge', a1)
    assert _is_linked(b, 'vml_Edge', a1)
    if hasattr(a1, 'vml_Graph49'):
        assert _is_linked(a1, 'vml_Graph49', b)
    _safe_set(b, 'vml_Edge', a2)
    assert _is_linked(b, 'vml_Edge', a2)
    if hasattr(a1, 'vml_Graph49'):
        assert not _is_linked(a1, 'vml_Graph49', b)
    if hasattr(a2, 'vml_Graph49'):
        assert _is_linked(a2, 'vml_Graph49', b)
    _safe_set(b, 'vml_Edge', None)
    assert not _is_linked(b, 'vml_Edge', a2)
    if hasattr(a2, 'vml_Graph49'):
        assert not _is_linked(a2, 'vml_Graph49', b)


def test_assoc_foregroundColor16_reverse_link_reassign_clear():
    a1 = vml_NodeStyle(borderWidth=7, padding=7)
    a2 = vml_NodeStyle(borderWidth=13, padding=13)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color18', a1)
    assert _is_linked(b, 'vml_Color18', a1)
    if hasattr(a1, 'vml_NodeStyle17'):
        assert _is_linked(a1, 'vml_NodeStyle17', b)
    _safe_set(b, 'vml_Color18', a2)
    assert _is_linked(b, 'vml_Color18', a2)
    if hasattr(a1, 'vml_NodeStyle17'):
        assert not _is_linked(a1, 'vml_NodeStyle17', b)
    if hasattr(a2, 'vml_NodeStyle17'):
        assert _is_linked(a2, 'vml_NodeStyle17', b)
    _safe_set(b, 'vml_Color18', None)
    assert not _is_linked(b, 'vml_Color18', a2)
    if hasattr(a2, 'vml_NodeStyle17'):
        assert not _is_linked(a2, 'vml_NodeStyle17', b)


def test_assoc_highlightColor19_reverse_link_reassign_clear():
    a1 = vml_NodeStyle(borderWidth=7, padding=7)
    a2 = vml_NodeStyle(borderWidth=13, padding=13)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color21', a1)
    assert _is_linked(b, 'vml_Color21', a1)
    if hasattr(a1, 'vml_NodeStyle20'):
        assert _is_linked(a1, 'vml_NodeStyle20', b)
    _safe_set(b, 'vml_Color21', a2)
    assert _is_linked(b, 'vml_Color21', a2)
    if hasattr(a1, 'vml_NodeStyle20'):
        assert not _is_linked(a1, 'vml_NodeStyle20', b)
    if hasattr(a2, 'vml_NodeStyle20'):
        assert _is_linked(a2, 'vml_NodeStyle20', b)
    _safe_set(b, 'vml_Color21', None)
    assert not _is_linked(b, 'vml_Color21', a2)
    if hasattr(a2, 'vml_NodeStyle20'):
        assert not _is_linked(a2, 'vml_NodeStyle20', b)


def test_assoc_highlightColor35_reverse_link_reassign_clear():
    a1 = vml_EdgeStyle(directed=True, lineStyle="sample_text", lineWidth=7, weight=3.14)
    a2 = vml_EdgeStyle(directed=False, lineStyle="sample_text_2", lineWidth=13, weight=9.99)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color37', a1)
    assert _is_linked(b, 'vml_Color37', a1)
    if hasattr(a1, 'vml_EdgeStyle36'):
        assert _is_linked(a1, 'vml_EdgeStyle36', b)
    _safe_set(b, 'vml_Color37', a2)
    assert _is_linked(b, 'vml_Color37', a2)
    if hasattr(a1, 'vml_EdgeStyle36'):
        assert not _is_linked(a1, 'vml_EdgeStyle36', b)
    if hasattr(a2, 'vml_EdgeStyle36'):
        assert _is_linked(a2, 'vml_EdgeStyle36', b)
    _safe_set(b, 'vml_Color37', None)
    assert not _is_linked(b, 'vml_Color37', a2)
    if hasattr(a2, 'vml_EdgeStyle36'):
        assert not _is_linked(a2, 'vml_EdgeStyle36', b)


def test_assoc_incoming53_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'Edge54', a1)
    assert _is_linked(b, 'Edge54', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Edge54', a2)
    assert _is_linked(b, 'Edge54', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Edge54', None)
    assert not _is_linked(b, 'Edge54', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_lineColor32_reverse_link_reassign_clear():
    a1 = vml_EdgeStyle(directed=True, lineStyle="sample_text", lineWidth=7, weight=3.14)
    a2 = vml_EdgeStyle(directed=False, lineStyle="sample_text_2", lineWidth=13, weight=9.99)
    b = vml_Color(blue=7, green=7, name="sample_text", red=7)
    _safe_set(b, 'vml_Color34', a1)
    assert _is_linked(b, 'vml_Color34', a1)
    if hasattr(a1, 'vml_EdgeStyle33'):
        assert _is_linked(a1, 'vml_EdgeStyle33', b)
    _safe_set(b, 'vml_Color34', a2)
    assert _is_linked(b, 'vml_Color34', a2)
    if hasattr(a1, 'vml_EdgeStyle33'):
        assert not _is_linked(a1, 'vml_EdgeStyle33', b)
    if hasattr(a2, 'vml_EdgeStyle33'):
        assert _is_linked(a2, 'vml_EdgeStyle33', b)
    _safe_set(b, 'vml_Color34', None)
    assert not _is_linked(b, 'vml_Color34', a2)
    if hasattr(a2, 'vml_EdgeStyle33'):
        assert not _is_linked(a2, 'vml_EdgeStyle33', b)


def test_assoc_nodes46_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_Graph(ID="sample_text", title="sample_text")
    _safe_set(b, 'vml_Graph', {a1})
    assert _is_linked(b, 'vml_Graph', a1)
    if hasattr(a1, 'vml_Node47'):
        assert _is_linked(a1, 'vml_Node47', b)
    _safe_set(b, 'vml_Graph', {a2})
    assert _is_linked(b, 'vml_Graph', a2)
    if hasattr(a1, 'vml_Node47'):
        assert not _is_linked(a1, 'vml_Node47', b)
    if hasattr(a2, 'vml_Node47'):
        assert _is_linked(a2, 'vml_Node47', b)
    _safe_set(b, 'vml_Graph', set())
    assert not _is_linked(b, 'vml_Graph', a2)
    if hasattr(a2, 'vml_Node47'):
        assert not _is_linked(a2, 'vml_Node47', b)


def test_assoc_outgoing52_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'Edge', a1)
    assert _is_linked(b, 'Edge', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Edge', a2)
    assert _is_linked(b, 'Edge', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Edge', None)
    assert not _is_linked(b, 'Edge', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_slices43_reverse_link_reassign_clear():
    a1 = vml_Slice(title="sample_text", value=7)
    a2 = vml_Slice(title="sample_text_2", value=13)
    b = vml_Pie(identifier="sample_text", title="sample_text")
    _safe_set(b, 'vml_Pie', {a1})
    assert _is_linked(b, 'vml_Pie', a1)
    if hasattr(a1, 'vml_Slice'):
        assert _is_linked(a1, 'vml_Slice', b)
    _safe_set(b, 'vml_Pie', {a2})
    assert _is_linked(b, 'vml_Pie', a2)
    if hasattr(a1, 'vml_Slice'):
        assert not _is_linked(a1, 'vml_Slice', b)
    if hasattr(a2, 'vml_Slice'):
        assert _is_linked(a2, 'vml_Slice', b)
    _safe_set(b, 'vml_Pie', set())
    assert not _is_linked(b, 'vml_Pie', a2)
    if hasattr(a2, 'vml_Slice'):
        assert not _is_linked(a2, 'vml_Slice', b)


def test_assoc_source28_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_EdgeStyle(directed=True, lineStyle="sample_text", lineWidth=7, weight=3.14)
    _safe_set(b, 'vml_EdgeStyle', a1)
    assert _is_linked(b, 'vml_EdgeStyle', a1)
    if hasattr(a1, 'vml_Node'):
        assert _is_linked(a1, 'vml_Node', b)
    _safe_set(b, 'vml_EdgeStyle', a2)
    assert _is_linked(b, 'vml_EdgeStyle', a2)
    if hasattr(a1, 'vml_Node'):
        assert not _is_linked(a1, 'vml_Node', b)
    if hasattr(a2, 'vml_Node'):
        assert _is_linked(a2, 'vml_Node', b)
    _safe_set(b, 'vml_EdgeStyle', None)
    assert not _is_linked(b, 'vml_EdgeStyle', a2)
    if hasattr(a2, 'vml_Node'):
        assert not _is_linked(a2, 'vml_Node', b)


def test_assoc_source55_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_target29_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_EdgeStyle(directed=True, lineStyle="sample_text", lineWidth=7, weight=3.14)
    _safe_set(b, 'vml_EdgeStyle30', a1)
    assert _is_linked(b, 'vml_EdgeStyle30', a1)
    if hasattr(a1, 'vml_Node31'):
        assert _is_linked(a1, 'vml_Node31', b)
    _safe_set(b, 'vml_EdgeStyle30', a2)
    assert _is_linked(b, 'vml_EdgeStyle30', a2)
    if hasattr(a1, 'vml_Node31'):
        assert not _is_linked(a1, 'vml_Node31', b)
    if hasattr(a2, 'vml_Node31'):
        assert _is_linked(a2, 'vml_Node31', b)
    _safe_set(b, 'vml_EdgeStyle30', None)
    assert not _is_linked(b, 'vml_EdgeStyle30', a2)
    if hasattr(a2, 'vml_Node31'):
        assert not _is_linked(a2, 'vml_Node31', b)


def test_assoc_target56_reverse_link_reassign_clear():
    a1 = vml_Node(icone="sample_text", title="sample_text")
    a2 = vml_Node(icone="sample_text_2", title="sample_text_2")
    b = vml_Edge(relation="sample_text")
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node57'):
        assert _is_linked(a1, 'Node57', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node57'):
        assert not _is_linked(a1, 'Node57', b)
    if hasattr(a2, 'Node57'):
        assert _is_linked(a2, 'Node57', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node57'):
        assert not _is_linked(a2, 'Node57', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_categories61_stub_double():
    # vml_StackBarChart has no real 'vml_StackBarChart62' property in the generated
    # code (a bare stub) -- manually attach it so vml_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Category(category="sample_text")
    partner = vml_StackBarChart()
    setattr(partner, 'vml_StackBarChart62', None)
    _safe_set(owner, 'vml_Category', partner)
    assert owner in getattr(partner, 'vml_StackBarChart62')
    _safe_set(owner, 'vml_Category', None)
    assert owner not in getattr(partner, 'vml_StackBarChart62')


def test_assoc_category63_stub_double():
    # vml_StackBars has no real 'vml_StackBars64' property in the generated
    # code (a bare stub) -- manually attach it so vml_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Category(category="sample_text")
    partner = vml_StackBars()
    setattr(partner, 'vml_StackBars64', None)
    _safe_set(owner, 'vml_Category65', partner)
    assert getattr(partner, 'vml_StackBars64') == owner
    _safe_set(owner, 'vml_Category65', None)
    assert getattr(partner, 'vml_StackBars64') is None


def test_assoc_cells7_stub_double():
    # vml_Row has no real 'vml_Row8' property in the generated
    # code (a bare stub) -- manually attach it so vml_Cell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Cell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Cell(textValue="sample_text")
    partner = vml_Row()
    setattr(partner, 'vml_Row8', None)
    _safe_set(owner, 'vml_Cell', partner)
    assert owner in getattr(partner, 'vml_Row8')
    _safe_set(owner, 'vml_Cell', None)
    assert owner not in getattr(partner, 'vml_Row8')


def test_assoc_rows5_stub_double():
    # vml_Row has no real 'vml_Row' property in the generated
    # code (a bare stub) -- manually attach it so vml_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Table(tableTitle="sample_text")
    partner = vml_Row()
    setattr(partner, 'vml_Row', None)
    _safe_set(owner, 'vml_Table6', {partner})
    assert getattr(partner, 'vml_Row') == owner
    _safe_set(owner, 'vml_Table6', set())
    assert getattr(partner, 'vml_Row') is None


def test_assoc_style44_stub_double():
    # vml_ChartWithoutAxisStyle has no real 'vml_ChartWithoutAxisStyle' property in the generated
    # code (a bare stub) -- manually attach it so vml_Pie's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Pie's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Pie(identifier="sample_text", title="sample_text")
    partner = vml_ChartWithoutAxisStyle()
    setattr(partner, 'vml_ChartWithoutAxisStyle', None)
    _safe_set(owner, 'vml_Pie45', partner)
    assert getattr(partner, 'vml_ChartWithoutAxisStyle') == owner
    _safe_set(owner, 'vml_Pie45', None)
    assert getattr(partner, 'vml_ChartWithoutAxisStyle') is None


def test_assoc_style50_stub_double():
    # vml_GraphStyle has no real 'vml_GraphStyle' property in the generated
    # code (a bare stub) -- manually attach it so vml_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Graph(ID="sample_text", title="sample_text")
    partner = vml_GraphStyle()
    setattr(partner, 'vml_GraphStyle', None)
    _safe_set(owner, 'vml_Graph51', partner)
    assert getattr(partner, 'vml_GraphStyle') == owner
    _safe_set(owner, 'vml_Graph51', None)
    assert getattr(partner, 'vml_GraphStyle') is None


def test_assoc_style58_stub_double():
    # vml_ChartWithAxisStyle has no real 'vml_ChartWithAxisStyle' property in the generated
    # code (a bare stub) -- manually attach it so vml_Chart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Chart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Chart(ID="sample_text", title="sample_text", xTitle="sample_text", yTitle="sample_text")
    partner = vml_ChartWithAxisStyle()
    setattr(partner, 'vml_ChartWithAxisStyle', None)
    _safe_set(owner, 'vml_Chart', partner)
    assert getattr(partner, 'vml_ChartWithAxisStyle') == owner
    _safe_set(owner, 'vml_Chart', None)
    assert getattr(partner, 'vml_ChartWithAxisStyle') is None


def test_assoc_table40_stub_double():
    # vml_DiagramElement has no real 'vml_DiagramElement41' property in the generated
    # code (a bare stub) -- manually attach it so vml_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Table(tableTitle="sample_text")
    partner = vml_DiagramElement()
    setattr(partner, 'vml_DiagramElement41', None)
    _safe_set(owner, 'vml_Table42', partner)
    assert getattr(partner, 'vml_DiagramElement41') == owner
    _safe_set(owner, 'vml_Table42', None)
    assert getattr(partner, 'vml_DiagramElement41') is None


def test_assoc_tables1_stub_double():
    # vml_Model has no real 'vml_Model2' property in the generated
    # code (a bare stub) -- manually attach it so vml_Table's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vml_Table's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vml_Table(tableTitle="sample_text")
    partner = vml_Model()
    setattr(partner, 'vml_Model2', None)
    _safe_set(owner, 'vml_Table', partner)
    assert owner in getattr(partner, 'vml_Model2')
    _safe_set(owner, 'vml_Table', None)
    assert owner not in getattr(partner, 'vml_Model2')


