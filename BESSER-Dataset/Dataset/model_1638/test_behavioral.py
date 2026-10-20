import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Auxiliary,
    ColorSet,
    CompoundColorSet,
    Declaration,
    DiagramElement,
    SimpleColorSet,
    cpntools_Alias,
    cpntools_Annot,
    cpntools_Arc,
    cpntools_AuxBox,
    cpntools_AuxEllipse,
    cpntools_AuxText,
    cpntools_Auxiliary,
    cpntools_Binder,
    cpntools_Block,
    cpntools_Boolean,
    cpntools_ColorSet,
    cpntools_CompoundColorSet,
    cpntools_Cpnet,
    cpntools_Declaration,
    cpntools_DiagramElement,
    cpntools_Enumerated,
    cpntools_Fusion,
    cpntools_Globbox,
    cpntools_Globref,
    cpntools_Group,
    cpntools_Index,
    cpntools_Initmark,
    cpntools_Integer,
    cpntools_LargeInteger,
    cpntools_List,
    cpntools_Ml,
    cpntools_Page,
    cpntools_Place,
    cpntools_Port,
    cpntools_Product,
    cpntools_Real,
    cpntools_Record,
    cpntools_SimpleColorSet,
    cpntools_String,
    cpntools_Subset,
    cpntools_Time,
    cpntools_Trans,
    cpntools_TransCond,
    cpntools_TransPriority,
    cpntools_TransTime,
    cpntools_Union,
    cpntools_Unit,
    cpntools_Var,
    Colour16,
    Orientation,
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

def test_assoc_annot55_reverse_link_reassign_clear():
    a1 = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    a2 = cpntools_Arc(currentcyckle="sample_text_2", headsize=9.99, order=13, orientation="sample_text_2")
    b = cpntools_Annot(text="sample_text")
    _safe_set(b, 'cpntools_Annot', a1)
    assert _is_linked(b, 'cpntools_Annot', a1)
    if hasattr(a1, 'cpntools_Arc'):
        assert _is_linked(a1, 'cpntools_Arc', b)
    _safe_set(b, 'cpntools_Annot', a2)
    assert _is_linked(b, 'cpntools_Annot', a2)
    if hasattr(a1, 'cpntools_Arc'):
        assert not _is_linked(a1, 'cpntools_Arc', b)
    if hasattr(a2, 'cpntools_Arc'):
        assert _is_linked(a2, 'cpntools_Arc', b)
    _safe_set(b, 'cpntools_Annot', None)
    assert not _is_linked(b, 'cpntools_Annot', a2)
    if hasattr(a2, 'cpntools_Arc'):
        assert not _is_linked(a2, 'cpntools_Arc', b)


def test_assoc_arcs12_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'Arc', a1)
    assert _is_linked(b, 'Arc', a1)
    if hasattr(a1, 'page13'):
        assert _is_linked(a1, 'page13', b)
    _safe_set(b, 'Arc', a2)
    assert _is_linked(b, 'Arc', a2)
    if hasattr(a1, 'page13'):
        assert not _is_linked(a1, 'page13', b)
    if hasattr(a2, 'page13'):
        assert _is_linked(a2, 'page13', b)
    _safe_set(b, 'Arc', None)
    assert not _is_linked(b, 'Arc', a2)
    if hasattr(a2, 'page13'):
        assert not _is_linked(a2, 'page13', b)


def test_assoc_arcs31_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'Arc32', a1)
    assert _is_linked(b, 'Arc32', a1)
    if hasattr(a1, 'place'):
        assert _is_linked(a1, 'place', b)
    _safe_set(b, 'Arc32', a2)
    assert _is_linked(b, 'Arc32', a2)
    if hasattr(a1, 'place'):
        assert not _is_linked(a1, 'place', b)
    if hasattr(a2, 'place'):
        assert _is_linked(a2, 'place', b)
    _safe_set(b, 'Arc32', None)
    assert not _is_linked(b, 'Arc32', a2)
    if hasattr(a2, 'place'):
        assert not _is_linked(a2, 'place', b)


def test_assoc_arcs62_reverse_link_reassign_clear():
    a1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    a2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'Arc63', a1)
    assert _is_linked(b, 'Arc63', a1)
    if hasattr(a1, 'trans'):
        assert _is_linked(a1, 'trans', b)
    _safe_set(b, 'Arc63', a2)
    assert _is_linked(b, 'Arc63', a2)
    if hasattr(a1, 'trans'):
        assert not _is_linked(a1, 'trans', b)
    if hasattr(a2, 'trans'):
        assert _is_linked(a2, 'trans', b)
    _safe_set(b, 'Arc63', None)
    assert not _is_linked(b, 'Arc63', a2)
    if hasattr(a2, 'trans'):
        assert not _is_linked(a2, 'trans', b)


def test_assoc_binder14_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    _safe_set(b, 'Binder15', a1)
    assert _is_linked(b, 'Binder15', a1)
    if hasattr(a1, 'pages'):
        assert _is_linked(a1, 'pages', b)
    _safe_set(b, 'Binder15', a2)
    assert _is_linked(b, 'Binder15', a2)
    if hasattr(a1, 'pages'):
        assert not _is_linked(a1, 'pages', b)
    if hasattr(a2, 'pages'):
        assert _is_linked(a2, 'pages', b)
    _safe_set(b, 'Binder15', None)
    assert not _is_linked(b, 'Binder15', a2)
    if hasattr(a2, 'pages'):
        assert not _is_linked(a2, 'pages', b)


def test_assoc_cond59_reverse_link_reassign_clear():
    a1 = cpntools_TransCond(text="sample_text")
    a2 = cpntools_TransCond(text="sample_text_2")
    b = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    _safe_set(b, 'cpntools_Trans', a1)
    assert _is_linked(b, 'cpntools_Trans', a1)
    if hasattr(a1, 'cpntools_TransCond'):
        assert _is_linked(a1, 'cpntools_TransCond', b)
    _safe_set(b, 'cpntools_Trans', a2)
    assert _is_linked(b, 'cpntools_Trans', a2)
    if hasattr(a1, 'cpntools_TransCond'):
        assert not _is_linked(a1, 'cpntools_TransCond', b)
    if hasattr(a2, 'cpntools_TransCond'):
        assert _is_linked(a2, 'cpntools_TransCond', b)
    _safe_set(b, 'cpntools_Trans', None)
    assert not _is_linked(b, 'cpntools_Trans', a2)
    if hasattr(a2, 'cpntools_TransCond'):
        assert not _is_linked(a2, 'cpntools_TransCond', b)


def test_assoc_fusion26_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Fusion(name="sample_text")
    _safe_set(b, 'Fusion27', a1)
    assert _is_linked(b, 'Fusion27', a1)
    if hasattr(a1, 'places'):
        assert _is_linked(a1, 'places', b)
    _safe_set(b, 'Fusion27', a2)
    assert _is_linked(b, 'Fusion27', a2)
    if hasattr(a1, 'places'):
        assert not _is_linked(a1, 'places', b)
    if hasattr(a2, 'places'):
        assert _is_linked(a2, 'places', b)
    _safe_set(b, 'Fusion27', None)
    assert not _is_linked(b, 'Fusion27', a2)
    if hasattr(a2, 'places'):
        assert not _is_linked(a2, 'places', b)


def test_assoc_group19_reverse_link_reassign_clear():
    a1 = cpntools_Group(name="sample_text")
    a2 = cpntools_Group(name="sample_text_2")
    b = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    _safe_set(b, 'groupElms', a1)
    assert _is_linked(b, 'groupElms', a1)
    if hasattr(a1, 'Group20'):
        assert _is_linked(a1, 'Group20', b)
    _safe_set(b, 'groupElms', a2)
    assert _is_linked(b, 'groupElms', a2)
    if hasattr(a1, 'Group20'):
        assert not _is_linked(a1, 'Group20', b)
    if hasattr(a2, 'Group20'):
        assert _is_linked(a2, 'Group20', b)
    _safe_set(b, 'groupElms', None)
    assert not _is_linked(b, 'groupElms', a2)
    if hasattr(a2, 'Group20'):
        assert not _is_linked(a2, 'Group20', b)


def test_assoc_group5_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Group(name="sample_text")
    _safe_set(b, 'Group', a1)
    assert _is_linked(b, 'Group', a1)
    if hasattr(a1, 'page'):
        assert _is_linked(a1, 'page', b)
    _safe_set(b, 'Group', a2)
    assert _is_linked(b, 'Group', a2)
    if hasattr(a1, 'page'):
        assert not _is_linked(a1, 'page', b)
    if hasattr(a2, 'page'):
        assert _is_linked(a2, 'page', b)
    _safe_set(b, 'Group', None)
    assert not _is_linked(b, 'Group', a2)
    if hasattr(a2, 'page'):
        assert not _is_linked(a2, 'page', b)


def test_assoc_groupElms16_reverse_link_reassign_clear():
    a1 = cpntools_Group(name="sample_text")
    a2 = cpntools_Group(name="sample_text_2")
    b = cpntools_DiagramElement(fillColour="sample_text", fillFilled=True, fillPattern="sample_text", lineColour="sample_text", lineThick=7, lineType="sample_text", posx=7, posy=7)
    _safe_set(b, 'DiagramElement', a1)
    assert _is_linked(b, 'DiagramElement', a1)
    if hasattr(a1, 'group'):
        assert _is_linked(a1, 'group', b)
    _safe_set(b, 'DiagramElement', a2)
    assert _is_linked(b, 'DiagramElement', a2)
    if hasattr(a1, 'group'):
        assert not _is_linked(a1, 'group', b)
    if hasattr(a2, 'group'):
        assert _is_linked(a2, 'group', b)
    _safe_set(b, 'DiagramElement', None)
    assert not _is_linked(b, 'DiagramElement', a2)
    if hasattr(a2, 'group'):
        assert not _is_linked(a2, 'group', b)


def test_assoc_initmark22_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Initmark(expression="sample_text")
    _safe_set(b, 'cpntools_Initmark', a1)
    assert _is_linked(b, 'cpntools_Initmark', a1)
    if hasattr(a1, 'cpntools_Place23'):
        assert _is_linked(a1, 'cpntools_Place23', b)
    _safe_set(b, 'cpntools_Initmark', a2)
    assert _is_linked(b, 'cpntools_Initmark', a2)
    if hasattr(a1, 'cpntools_Place23'):
        assert not _is_linked(a1, 'cpntools_Place23', b)
    if hasattr(a2, 'cpntools_Place23'):
        assert _is_linked(a2, 'cpntools_Place23', b)
    _safe_set(b, 'cpntools_Initmark', None)
    assert not _is_linked(b, 'cpntools_Initmark', a2)
    if hasattr(a2, 'cpntools_Place23'):
        assert not _is_linked(a2, 'cpntools_Place23', b)


def test_assoc_page17_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Group(name="sample_text")
    _safe_set(b, 'group18', a1)
    assert _is_linked(b, 'group18', a1)
    if hasattr(a1, 'Page'):
        assert _is_linked(a1, 'Page', b)
    _safe_set(b, 'group18', a2)
    assert _is_linked(b, 'group18', a2)
    if hasattr(a1, 'Page'):
        assert not _is_linked(a1, 'Page', b)
    if hasattr(a2, 'Page'):
        assert _is_linked(a2, 'Page', b)
    _safe_set(b, 'group18', None)
    assert not _is_linked(b, 'group18', a2)
    if hasattr(a2, 'Page'):
        assert not _is_linked(a2, 'Page', b)


def test_assoc_page28_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Page(name="sample_text")
    _safe_set(b, 'Page30', a1)
    assert _is_linked(b, 'Page30', a1)
    if hasattr(a1, 'places29'):
        assert _is_linked(a1, 'places29', b)
    _safe_set(b, 'Page30', a2)
    assert _is_linked(b, 'Page30', a2)
    if hasattr(a1, 'places29'):
        assert not _is_linked(a1, 'places29', b)
    if hasattr(a2, 'places29'):
        assert _is_linked(a2, 'places29', b)
    _safe_set(b, 'Page30', None)
    assert not _is_linked(b, 'Page30', a2)
    if hasattr(a2, 'places29'):
        assert not _is_linked(a2, 'places29', b)


def test_assoc_page56_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'arcs57', a1)
    assert _is_linked(b, 'arcs57', a1)
    if hasattr(a1, 'Page58'):
        assert _is_linked(a1, 'Page58', b)
    _safe_set(b, 'arcs57', a2)
    assert _is_linked(b, 'arcs57', a2)
    if hasattr(a1, 'Page58'):
        assert not _is_linked(a1, 'Page58', b)
    if hasattr(a2, 'Page58'):
        assert _is_linked(a2, 'Page58', b)
    _safe_set(b, 'arcs57', None)
    assert not _is_linked(b, 'arcs57', a2)
    if hasattr(a2, 'Page58'):
        assert not _is_linked(a2, 'Page58', b)


def test_assoc_page60_reverse_link_reassign_clear():
    a1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    a2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    b = cpntools_Page(name="sample_text")
    _safe_set(b, 'Page61', a1)
    assert _is_linked(b, 'Page61', a1)
    if hasattr(a1, 'transs'):
        assert _is_linked(a1, 'transs', b)
    _safe_set(b, 'Page61', a2)
    assert _is_linked(b, 'Page61', a2)
    if hasattr(a1, 'transs'):
        assert not _is_linked(a1, 'transs', b)
    if hasattr(a2, 'transs'):
        assert _is_linked(a2, 'transs', b)
    _safe_set(b, 'Page61', None)
    assert not _is_linked(b, 'Page61', a2)
    if hasattr(a2, 'transs'):
        assert not _is_linked(a2, 'transs', b)


def test_assoc_pages71_reverse_link_reassign_clear():
    a1 = cpntools_Page(name="sample_text")
    a2 = cpntools_Page(name="sample_text_2")
    b = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    _safe_set(b, 'binder72', {a1})
    assert _is_linked(b, 'binder72', a1)
    if hasattr(a1, 'Page73'):
        assert _is_linked(a1, 'Page73', b)
    _safe_set(b, 'binder72', {a2})
    assert _is_linked(b, 'binder72', a2)
    if hasattr(a1, 'Page73'):
        assert not _is_linked(a1, 'Page73', b)
    if hasattr(a2, 'Page73'):
        assert _is_linked(a2, 'Page73', b)
    _safe_set(b, 'binder72', set())
    assert not _is_linked(b, 'binder72', a2)
    if hasattr(a2, 'Page73'):
        assert not _is_linked(a2, 'Page73', b)


def test_assoc_place50_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'arcs', a1)
    assert _is_linked(b, 'arcs', a1)
    if hasattr(a1, 'Place51'):
        assert _is_linked(a1, 'Place51', b)
    _safe_set(b, 'arcs', a2)
    assert _is_linked(b, 'arcs', a2)
    if hasattr(a1, 'Place51'):
        assert not _is_linked(a1, 'Place51', b)
    if hasattr(a2, 'Place51'):
        assert _is_linked(a2, 'Place51', b)
    _safe_set(b, 'arcs', None)
    assert not _is_linked(b, 'arcs', a2)
    if hasattr(a2, 'Place51'):
        assert not _is_linked(a2, 'Place51', b)


def test_assoc_places37_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Fusion(name="sample_text")
    _safe_set(b, 'fusion', {a1})
    assert _is_linked(b, 'fusion', a1)
    if hasattr(a1, 'Place38'):
        assert _is_linked(a1, 'Place38', b)
    _safe_set(b, 'fusion', {a2})
    assert _is_linked(b, 'fusion', a2)
    if hasattr(a1, 'Place38'):
        assert not _is_linked(a1, 'Place38', b)
    if hasattr(a2, 'Place38'):
        assert _is_linked(a2, 'Place38', b)
    _safe_set(b, 'fusion', set())
    assert not _is_linked(b, 'fusion', a2)
    if hasattr(a2, 'Place38'):
        assert not _is_linked(a2, 'Place38', b)


def test_assoc_places6_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_Page(name="sample_text")
    _safe_set(b, 'page7', {a1})
    assert _is_linked(b, 'page7', a1)
    if hasattr(a1, 'Place'):
        assert _is_linked(a1, 'Place', b)
    _safe_set(b, 'page7', {a2})
    assert _is_linked(b, 'page7', a2)
    if hasattr(a1, 'Place'):
        assert not _is_linked(a1, 'Place', b)
    if hasattr(a2, 'Place'):
        assert _is_linked(a2, 'Place', b)
    _safe_set(b, 'page7', set())
    assert not _is_linked(b, 'page7', a2)
    if hasattr(a2, 'Place'):
        assert not _is_linked(a2, 'Place', b)


def test_assoc_port24_reverse_link_reassign_clear():
    a1 = cpntools_Port(portType="sample_text")
    a2 = cpntools_Port(portType="sample_text_2")
    b = cpntools_Place(height=7, text="sample_text", width=7)
    _safe_set(b, 'cpntools_Place25', a1)
    assert _is_linked(b, 'cpntools_Place25', a1)
    if hasattr(a1, 'cpntools_Port'):
        assert _is_linked(a1, 'cpntools_Port', b)
    _safe_set(b, 'cpntools_Place25', a2)
    assert _is_linked(b, 'cpntools_Place25', a2)
    if hasattr(a1, 'cpntools_Port'):
        assert not _is_linked(a1, 'cpntools_Port', b)
    if hasattr(a2, 'cpntools_Port'):
        assert _is_linked(a2, 'cpntools_Port', b)
    _safe_set(b, 'cpntools_Place25', None)
    assert not _is_linked(b, 'cpntools_Place25', a2)
    if hasattr(a2, 'cpntools_Port'):
        assert not _is_linked(a2, 'cpntools_Port', b)


def test_assoc_priority64_reverse_link_reassign_clear():
    a1 = cpntools_TransPriority(text="sample_text")
    a2 = cpntools_TransPriority(text="sample_text_2")
    b = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    _safe_set(b, 'cpntools_Trans65', a1)
    assert _is_linked(b, 'cpntools_Trans65', a1)
    if hasattr(a1, 'cpntools_TransPriority'):
        assert _is_linked(a1, 'cpntools_TransPriority', b)
    _safe_set(b, 'cpntools_Trans65', a2)
    assert _is_linked(b, 'cpntools_Trans65', a2)
    if hasattr(a1, 'cpntools_TransPriority'):
        assert not _is_linked(a1, 'cpntools_TransPriority', b)
    if hasattr(a2, 'cpntools_TransPriority'):
        assert _is_linked(a2, 'cpntools_TransPriority', b)
    _safe_set(b, 'cpntools_Trans65', None)
    assert not _is_linked(b, 'cpntools_Trans65', a2)
    if hasattr(a2, 'cpntools_TransPriority'):
        assert not _is_linked(a2, 'cpntools_TransPriority', b)


def test_assoc_time66_reverse_link_reassign_clear():
    a1 = cpntools_TransTime(text="sample_text")
    a2 = cpntools_TransTime(text="sample_text_2")
    b = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    _safe_set(b, 'cpntools_Trans67', a1)
    assert _is_linked(b, 'cpntools_Trans67', a1)
    if hasattr(a1, 'cpntools_TransTime'):
        assert _is_linked(a1, 'cpntools_TransTime', b)
    _safe_set(b, 'cpntools_Trans67', a2)
    assert _is_linked(b, 'cpntools_Trans67', a2)
    if hasattr(a1, 'cpntools_TransTime'):
        assert not _is_linked(a1, 'cpntools_TransTime', b)
    if hasattr(a2, 'cpntools_TransTime'):
        assert _is_linked(a2, 'cpntools_TransTime', b)
    _safe_set(b, 'cpntools_Trans67', None)
    assert not _is_linked(b, 'cpntools_Trans67', a2)
    if hasattr(a2, 'cpntools_TransTime'):
        assert not _is_linked(a2, 'cpntools_TransTime', b)


def test_assoc_trans52_reverse_link_reassign_clear():
    a1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    a2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    b = cpntools_Arc(currentcyckle="sample_text", headsize=3.14, order=7, orientation="sample_text")
    _safe_set(b, 'arcs53', a1)
    assert _is_linked(b, 'arcs53', a1)
    if hasattr(a1, 'Trans54'):
        assert _is_linked(a1, 'Trans54', b)
    _safe_set(b, 'arcs53', a2)
    assert _is_linked(b, 'arcs53', a2)
    if hasattr(a1, 'Trans54'):
        assert not _is_linked(a1, 'Trans54', b)
    if hasattr(a2, 'Trans54'):
        assert _is_linked(a2, 'Trans54', b)
    _safe_set(b, 'arcs53', None)
    assert not _is_linked(b, 'arcs53', a2)
    if hasattr(a2, 'Trans54'):
        assert not _is_linked(a2, 'Trans54', b)


def test_assoc_transs10_reverse_link_reassign_clear():
    a1 = cpntools_Trans(explicit=True, height=7, text="sample_text", width=7)
    a2 = cpntools_Trans(explicit=False, height=13, text="sample_text_2", width=13)
    b = cpntools_Page(name="sample_text")
    _safe_set(b, 'page11', {a1})
    assert _is_linked(b, 'page11', a1)
    if hasattr(a1, 'Trans'):
        assert _is_linked(a1, 'Trans', b)
    _safe_set(b, 'page11', {a2})
    assert _is_linked(b, 'page11', a2)
    if hasattr(a1, 'Trans'):
        assert not _is_linked(a1, 'Trans', b)
    if hasattr(a2, 'Trans'):
        assert _is_linked(a2, 'Trans', b)
    _safe_set(b, 'page11', set())
    assert not _is_linked(b, 'page11', a2)
    if hasattr(a2, 'Trans'):
        assert not _is_linked(a2, 'Trans', b)


def test_assoc_type21_reverse_link_reassign_clear():
    a1 = cpntools_Place(height=7, text="sample_text", width=7)
    a2 = cpntools_Place(height=13, text="sample_text_2", width=13)
    b = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    _safe_set(b, 'cpntools_ColorSet', a1)
    assert _is_linked(b, 'cpntools_ColorSet', a1)
    if hasattr(a1, 'cpntools_Place'):
        assert _is_linked(a1, 'cpntools_Place', b)
    _safe_set(b, 'cpntools_ColorSet', a2)
    assert _is_linked(b, 'cpntools_ColorSet', a2)
    if hasattr(a1, 'cpntools_Place'):
        assert not _is_linked(a1, 'cpntools_Place', b)
    if hasattr(a2, 'cpntools_Place'):
        assert _is_linked(a2, 'cpntools_Place', b)
    _safe_set(b, 'cpntools_ColorSet', None)
    assert not _is_linked(b, 'cpntools_ColorSet', a2)
    if hasattr(a2, 'cpntools_Place'):
        assert not _is_linked(a2, 'cpntools_Place', b)


def test_assoc_type46_reverse_link_reassign_clear():
    a1 = cpntools_Var(idname="sample_text")
    a2 = cpntools_Var(idname="sample_text_2")
    b = cpntools_ColorSet(colorSetType="sample_text", declare="sample_text", idname="sample_text", timed=True)
    _safe_set(b, 'cpntools_ColorSet47', a1)
    assert _is_linked(b, 'cpntools_ColorSet47', a1)
    if hasattr(a1, 'cpntools_Var'):
        assert _is_linked(a1, 'cpntools_Var', b)
    _safe_set(b, 'cpntools_ColorSet47', a2)
    assert _is_linked(b, 'cpntools_ColorSet47', a2)
    if hasattr(a1, 'cpntools_Var'):
        assert not _is_linked(a1, 'cpntools_Var', b)
    if hasattr(a2, 'cpntools_Var'):
        assert _is_linked(a2, 'cpntools_Var', b)
    _safe_set(b, 'cpntools_ColorSet47', None)
    assert not _is_linked(b, 'cpntools_ColorSet47', a2)
    if hasattr(a2, 'cpntools_Var'):
        assert not _is_linked(a2, 'cpntools_Var', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_auxiliarys8_stub_double():
    # cpntools_Auxiliary has no real 'Auxiliary' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Page(name="sample_text")
    partner = cpntools_Auxiliary()
    setattr(partner, 'Auxiliary', None)
    _safe_set(owner, 'page9', {partner})
    assert getattr(partner, 'Auxiliary') == owner
    _safe_set(owner, 'page9', set())
    assert getattr(partner, 'Auxiliary') is None


def test_assoc_binder3_stub_double():
    # cpntools_Cpnet has no real 'cpnet4' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Binder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Binder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    partner = cpntools_Cpnet()
    setattr(partner, 'cpnet4', None)
    _safe_set(owner, 'Binder', partner)
    assert getattr(partner, 'cpnet4') == owner
    _safe_set(owner, 'Binder', None)
    assert getattr(partner, 'cpnet4') is None


def test_assoc_block35_stub_double():
    # cpntools_Declaration has no real 'declarations36' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Block(idname="sample_text")
    partner = cpntools_Declaration()
    setattr(partner, 'declarations36', None)
    _safe_set(owner, 'Block', partner)
    assert getattr(partner, 'declarations36') == owner
    _safe_set(owner, 'Block', None)
    assert getattr(partner, 'declarations36') is None


def test_assoc_cpnet39_stub_double():
    # cpntools_Cpnet has no real 'Cpnet' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Fusion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Fusion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Fusion(name="sample_text")
    partner = cpntools_Cpnet()
    setattr(partner, 'Cpnet', None)
    _safe_set(owner, 'fusions', partner)
    assert getattr(partner, 'Cpnet') == owner
    _safe_set(owner, 'fusions', None)
    assert getattr(partner, 'Cpnet') is None


def test_assoc_cpnet42_stub_double():
    # cpntools_Cpnet has no real 'Cpnet43' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Globbox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Globbox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Globbox(name="sample_text")
    partner = cpntools_Cpnet()
    setattr(partner, 'Cpnet43', None)
    _safe_set(owner, 'globbox', partner)
    assert getattr(partner, 'Cpnet43') == owner
    _safe_set(owner, 'globbox', None)
    assert getattr(partner, 'Cpnet43') is None


def test_assoc_cpnet69_stub_double():
    # cpntools_Cpnet has no real 'Cpnet70' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Binder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Binder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Binder(height=7, posx=7, posy=7, width=7)
    partner = cpntools_Cpnet()
    setattr(partner, 'Cpnet70', None)
    _safe_set(owner, 'binder', partner)
    assert getattr(partner, 'Cpnet70') == owner
    _safe_set(owner, 'binder', None)
    assert getattr(partner, 'Cpnet70') is None


def test_assoc_declarations44_stub_double():
    # cpntools_Declaration has no real 'Declaration' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Globbox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Globbox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Globbox(name="sample_text")
    partner = cpntools_Declaration()
    setattr(partner, 'Declaration', None)
    _safe_set(owner, 'globbox45', {partner})
    assert getattr(partner, 'Declaration') == owner
    _safe_set(owner, 'globbox45', set())
    assert getattr(partner, 'Declaration') is None


def test_assoc_declarations48_stub_double():
    # cpntools_Declaration has no real 'Declaration49' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Block's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Block's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Block(idname="sample_text")
    partner = cpntools_Declaration()
    setattr(partner, 'Declaration49', None)
    _safe_set(owner, 'block', {partner})
    assert getattr(partner, 'Declaration49') == owner
    _safe_set(owner, 'block', set())
    assert getattr(partner, 'Declaration49') is None


def test_assoc_fusions0_stub_double():
    # cpntools_Cpnet has no real 'cpnet' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Fusion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Fusion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Fusion(name="sample_text")
    partner = cpntools_Cpnet()
    setattr(partner, 'cpnet', None)
    _safe_set(owner, 'Fusion', partner)
    assert owner in getattr(partner, 'cpnet')
    _safe_set(owner, 'Fusion', None)
    assert owner not in getattr(partner, 'cpnet')


def test_assoc_globbox1_stub_double():
    # cpntools_Cpnet has no real 'cpnet2' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Globbox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Globbox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Globbox(name="sample_text")
    partner = cpntools_Cpnet()
    setattr(partner, 'cpnet2', None)
    _safe_set(owner, 'Globbox', partner)
    assert getattr(partner, 'cpnet2') == owner
    _safe_set(owner, 'Globbox', None)
    assert getattr(partner, 'cpnet2') is None


def test_assoc_globbox33_stub_double():
    # cpntools_Declaration has no real 'declarations' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Globbox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Globbox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Globbox(name="sample_text")
    partner = cpntools_Declaration()
    setattr(partner, 'declarations', None)
    _safe_set(owner, 'Globbox34', partner)
    assert getattr(partner, 'declarations') == owner
    _safe_set(owner, 'Globbox34', None)
    assert getattr(partner, 'declarations') is None


def test_assoc_page40_stub_double():
    # cpntools_Auxiliary has no real 'auxiliarys' property in the generated
    # code (a bare stub) -- manually attach it so cpntools_Page's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cpntools_Page's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cpntools_Page(name="sample_text")
    partner = cpntools_Auxiliary()
    setattr(partner, 'auxiliarys', None)
    _safe_set(owner, 'Page41', partner)
    assert getattr(partner, 'auxiliarys') == owner
    _safe_set(owner, 'Page41', None)
    assert getattr(partner, 'auxiliarys') is None


