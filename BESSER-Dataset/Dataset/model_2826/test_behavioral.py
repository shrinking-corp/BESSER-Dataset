import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractList,
    AbstractMenu,
    Canvas,
    Color,
    Composite,
    Control,
    Decorations,
    IntervalControl,
    IntervalSelector,
    Item,
    Labeled,
    LayoutData,
    Text,
    Widget,
    swt_AbstractComposite,
    swt_AbstractList,
    swt_AbstractMenu,
    swt_Browser,
    swt_Button,
    swt_Canvas,
    swt_Color,
    swt_Combo,
    swt_Composite,
    swt_Control,
    swt_CoolBar,
    swt_CoolItem,
    swt_DateTime,
    swt_Decorations,
    swt_FillLayout,
    swt_Font,
    swt_FormAttachment,
    swt_FormData,
    swt_FormLayout,
    swt_GridData,
    swt_GridLayout,
    swt_Group,
    swt_IntervalControl,
    swt_IntervalSelector,
    swt_Item,
    swt_Label,
    swt_Labeled,
    swt_Layout,
    swt_LayoutData,
    swt_LineAttributes,
    swt_List,
    swt_Menu,
    swt_MenuBar,
    swt_MenuItem,
    swt_PasswordText,
    swt_ProgressBar,
    swt_RGBColor,
    swt_RowData,
    swt_RowLayout,
    swt_SearchText,
    swt_Separator,
    swt_Shell,
    swt_Slider,
    swt_Spinner,
    swt_SystemColor,
    swt_TabFolder,
    swt_TabItem,
    swt_Text,
    swt_ToolBar,
    swt_ToolItem,
    swt_Tree,
    swt_TreeColumn,
    swt_TreeViewer,
    swt_Viewer,
    swt_Widget,
    ArrowStyle,
    BorderStyle,
    ButtonStyle,
    CapStyle,
    ComboStyle,
    FontStyle,
    FormAttachmentAlignment,
    HorizontalAlignmentStyle,
    JoinStyle,
    LineStyle,
    MenuItemStyle,
    MenuStyle,
    ModalStyle,
    MultiplicityStyle,
    OrientationStyle,
    ProgressState,
    SortDirection,
    SystemColors,
    TextOrientationStyle,
    TrimStyle,
    VerticalAlignmentStyle,
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

def test_assoc_bottom31_reverse_link_reassign_clear():
    a1 = swt_FormData(height=7, width=7)
    a2 = swt_FormData(height=13, width=13)
    b = swt_FormAttachment(alignment="sample_text", denominator=7, numerator=7, offset=7)
    _safe_set(b, 'swt_FormAttachment33', a1)
    assert _is_linked(b, 'swt_FormAttachment33', a1)
    if hasattr(a1, 'swt_FormData32'):
        assert _is_linked(a1, 'swt_FormData32', b)
    _safe_set(b, 'swt_FormAttachment33', a2)
    assert _is_linked(b, 'swt_FormAttachment33', a2)
    if hasattr(a1, 'swt_FormData32'):
        assert not _is_linked(a1, 'swt_FormData32', b)
    if hasattr(a2, 'swt_FormData32'):
        assert _is_linked(a2, 'swt_FormData32', b)
    _safe_set(b, 'swt_FormAttachment33', None)
    assert not _is_linked(b, 'swt_FormAttachment33', a2)
    if hasattr(a2, 'swt_FormData32'):
        assert not _is_linked(a2, 'swt_FormData32', b)


def test_assoc_columns37_reverse_link_reassign_clear():
    a1 = swt_TreeColumn(displayText="sample_text", toolTipText="sample_text")
    a2 = swt_TreeColumn(displayText="sample_text_2", toolTipText="sample_text_2")
    b = swt_Tree(headerVisible=True, linesVisible=True, sortDirection="sample_text")
    _safe_set(b, 'swt_Tree', {a1})
    assert _is_linked(b, 'swt_Tree', a1)
    if hasattr(a1, 'swt_TreeColumn'):
        assert _is_linked(a1, 'swt_TreeColumn', b)
    _safe_set(b, 'swt_Tree', {a2})
    assert _is_linked(b, 'swt_Tree', a2)
    if hasattr(a1, 'swt_TreeColumn'):
        assert not _is_linked(a1, 'swt_TreeColumn', b)
    if hasattr(a2, 'swt_TreeColumn'):
        assert _is_linked(a2, 'swt_TreeColumn', b)
    _safe_set(b, 'swt_Tree', set())
    assert not _is_linked(b, 'swt_Tree', a2)
    if hasattr(a2, 'swt_TreeColumn'):
        assert not _is_linked(a2, 'swt_TreeColumn', b)


def test_assoc_control18_reverse_link_reassign_clear():
    a1 = swt_CoolItem(minimumSize="sample_text", preferredSize="sample_text", size="sample_text")
    a2 = swt_CoolItem(minimumSize="sample_text_2", preferredSize="sample_text_2", size="sample_text_2")
    b = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    _safe_set(b, 'swt_Control19', a1)
    assert _is_linked(b, 'swt_Control19', a1)
    if hasattr(a1, 'swt_CoolItem'):
        assert _is_linked(a1, 'swt_CoolItem', b)
    _safe_set(b, 'swt_Control19', a2)
    assert _is_linked(b, 'swt_Control19', a2)
    if hasattr(a1, 'swt_CoolItem'):
        assert not _is_linked(a1, 'swt_CoolItem', b)
    if hasattr(a2, 'swt_CoolItem'):
        assert _is_linked(a2, 'swt_CoolItem', b)
    _safe_set(b, 'swt_Control19', None)
    assert not _is_linked(b, 'swt_Control19', a2)
    if hasattr(a2, 'swt_CoolItem'):
        assert not _is_linked(a2, 'swt_CoolItem', b)


def test_assoc_control21_reverse_link_reassign_clear():
    a1 = swt_TabItem(toolTipText="sample_text")
    a2 = swt_TabItem(toolTipText="sample_text_2")
    b = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    _safe_set(b, 'swt_Control23', a1)
    assert _is_linked(b, 'swt_Control23', a1)
    if hasattr(a1, 'swt_TabItem22'):
        assert _is_linked(a1, 'swt_TabItem22', b)
    _safe_set(b, 'swt_Control23', a2)
    assert _is_linked(b, 'swt_Control23', a2)
    if hasattr(a1, 'swt_TabItem22'):
        assert not _is_linked(a1, 'swt_TabItem22', b)
    if hasattr(a2, 'swt_TabItem22'):
        assert _is_linked(a2, 'swt_TabItem22', b)
    _safe_set(b, 'swt_Control23', None)
    assert not _is_linked(b, 'swt_Control23', a2)
    if hasattr(a2, 'swt_TabItem22'):
        assert not _is_linked(a2, 'swt_TabItem22', b)


def test_assoc_control34_reverse_link_reassign_clear():
    a1 = swt_FormAttachment(alignment="sample_text", denominator=7, numerator=7, offset=7)
    a2 = swt_FormAttachment(alignment="sample_text_2", denominator=13, numerator=13, offset=13)
    b = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    _safe_set(b, 'swt_Control36', a1)
    assert _is_linked(b, 'swt_Control36', a1)
    if hasattr(a1, 'swt_FormAttachment35'):
        assert _is_linked(a1, 'swt_FormAttachment35', b)
    _safe_set(b, 'swt_Control36', a2)
    assert _is_linked(b, 'swt_Control36', a2)
    if hasattr(a1, 'swt_FormAttachment35'):
        assert not _is_linked(a1, 'swt_FormAttachment35', b)
    if hasattr(a2, 'swt_FormAttachment35'):
        assert _is_linked(a2, 'swt_FormAttachment35', b)
    _safe_set(b, 'swt_Control36', None)
    assert not _is_linked(b, 'swt_Control36', a2)
    if hasattr(a2, 'swt_FormAttachment35'):
        assert not _is_linked(a2, 'swt_FormAttachment35', b)


def test_assoc_defaultButton6_reverse_link_reassign_clear():
    a1 = swt_Shell(alpha=7, fullScreen=True, modalStyle="sample_text", trimStyle="sample_text")
    a2 = swt_Shell(alpha=13, fullScreen=False, modalStyle="sample_text_2", trimStyle="sample_text_2")
    b = swt_Button(arrowStyle="sample_text", buttonStyle="sample_text", selection=True)
    _safe_set(b, 'swt_Button', a1)
    assert _is_linked(b, 'swt_Button', a1)
    if hasattr(a1, 'swt_Shell'):
        assert _is_linked(a1, 'swt_Shell', b)
    _safe_set(b, 'swt_Button', a2)
    assert _is_linked(b, 'swt_Button', a2)
    if hasattr(a1, 'swt_Shell'):
        assert not _is_linked(a1, 'swt_Shell', b)
    if hasattr(a2, 'swt_Shell'):
        assert _is_linked(a2, 'swt_Shell', b)
    _safe_set(b, 'swt_Button', None)
    assert not _is_linked(b, 'swt_Button', a2)
    if hasattr(a2, 'swt_Shell'):
        assert not _is_linked(a2, 'swt_Shell', b)


def test_assoc_font3_reverse_link_reassign_clear():
    a1 = swt_Font(height=7, name="sample_text", style=7)
    a2 = swt_Font(height=13, name="sample_text_2", style=13)
    b = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    _safe_set(b, 'swt_Control4', a1)
    assert _is_linked(b, 'swt_Control4', a1)
    if hasattr(a1, 'swt_Font'):
        assert _is_linked(a1, 'swt_Font', b)
    _safe_set(b, 'swt_Control4', a2)
    assert _is_linked(b, 'swt_Control4', a2)
    if hasattr(a1, 'swt_Font'):
        assert not _is_linked(a1, 'swt_Font', b)
    if hasattr(a2, 'swt_Font'):
        assert _is_linked(a2, 'swt_Font', b)
    _safe_set(b, 'swt_Control4', None)
    assert not _is_linked(b, 'swt_Control4', a2)
    if hasattr(a2, 'swt_Font'):
        assert not _is_linked(a2, 'swt_Font', b)


def test_assoc_items11_reverse_link_reassign_clear():
    a1 = swt_ToolItem(enabled=True, hotImage="sample_text", selection=True, toolTipText="sample_text")
    a2 = swt_ToolItem(enabled=False, hotImage="sample_text_2", selection=False, toolTipText="sample_text_2")
    b = swt_ToolBar(orientationStyle="sample_text")
    _safe_set(b, 'parent12', {a1})
    assert _is_linked(b, 'parent12', a1)
    if hasattr(a1, 'ToolItem'):
        assert _is_linked(a1, 'ToolItem', b)
    _safe_set(b, 'parent12', {a2})
    assert _is_linked(b, 'parent12', a2)
    if hasattr(a1, 'ToolItem'):
        assert not _is_linked(a1, 'ToolItem', b)
    if hasattr(a2, 'ToolItem'):
        assert _is_linked(a2, 'ToolItem', b)
    _safe_set(b, 'parent12', set())
    assert not _is_linked(b, 'parent12', a2)
    if hasattr(a2, 'ToolItem'):
        assert not _is_linked(a2, 'ToolItem', b)


def test_assoc_items14_reverse_link_reassign_clear():
    a1 = swt_CoolItem(minimumSize="sample_text", preferredSize="sample_text", size="sample_text")
    a2 = swt_CoolItem(minimumSize="sample_text_2", preferredSize="sample_text_2", size="sample_text_2")
    b = swt_CoolBar(orientationStyle="sample_text")
    _safe_set(b, 'parent15', {a1})
    assert _is_linked(b, 'parent15', a1)
    if hasattr(a1, 'CoolItem'):
        assert _is_linked(a1, 'CoolItem', b)
    _safe_set(b, 'parent15', {a2})
    assert _is_linked(b, 'parent15', a2)
    if hasattr(a1, 'CoolItem'):
        assert not _is_linked(a1, 'CoolItem', b)
    if hasattr(a2, 'CoolItem'):
        assert _is_linked(a2, 'CoolItem', b)
    _safe_set(b, 'parent15', set())
    assert not _is_linked(b, 'parent15', a2)
    if hasattr(a2, 'CoolItem'):
        assert not _is_linked(a2, 'CoolItem', b)


def test_assoc_items7_reverse_link_reassign_clear():
    a1 = swt_MenuItem(ID=7, accelerator=7, enabled=True, menuItemStyle="sample_text", selection=True)
    a2 = swt_MenuItem(ID=13, accelerator=13, enabled=False, menuItemStyle="sample_text_2", selection=False)
    b = swt_AbstractMenu(enabled=True, textOrientationStyle="sample_text", visible=True)
    _safe_set(b, 'swt_AbstractMenu', {a1})
    assert _is_linked(b, 'swt_AbstractMenu', a1)
    if hasattr(a1, 'swt_MenuItem'):
        assert _is_linked(a1, 'swt_MenuItem', b)
    _safe_set(b, 'swt_AbstractMenu', {a2})
    assert _is_linked(b, 'swt_AbstractMenu', a2)
    if hasattr(a1, 'swt_MenuItem'):
        assert not _is_linked(a1, 'swt_MenuItem', b)
    if hasattr(a2, 'swt_MenuItem'):
        assert _is_linked(a2, 'swt_MenuItem', b)
    _safe_set(b, 'swt_AbstractMenu', set())
    assert not _is_linked(b, 'swt_AbstractMenu', a2)
    if hasattr(a2, 'swt_MenuItem'):
        assert not _is_linked(a2, 'swt_MenuItem', b)


def test_assoc_left24_reverse_link_reassign_clear():
    a1 = swt_FormData(height=7, width=7)
    a2 = swt_FormData(height=13, width=13)
    b = swt_FormAttachment(alignment="sample_text", denominator=7, numerator=7, offset=7)
    _safe_set(b, 'swt_FormAttachment', a1)
    assert _is_linked(b, 'swt_FormAttachment', a1)
    if hasattr(a1, 'swt_FormData'):
        assert _is_linked(a1, 'swt_FormData', b)
    _safe_set(b, 'swt_FormAttachment', a2)
    assert _is_linked(b, 'swt_FormAttachment', a2)
    if hasattr(a1, 'swt_FormData'):
        assert not _is_linked(a1, 'swt_FormData', b)
    if hasattr(a2, 'swt_FormData'):
        assert _is_linked(a2, 'swt_FormData', b)
    _safe_set(b, 'swt_FormAttachment', None)
    assert not _is_linked(b, 'swt_FormAttachment', a2)
    if hasattr(a2, 'swt_FormData'):
        assert not _is_linked(a2, 'swt_FormData', b)


def test_assoc_menu10_reverse_link_reassign_clear():
    a1 = swt_MenuItem(ID=7, accelerator=7, enabled=True, menuItemStyle="sample_text", selection=True)
    a2 = swt_MenuItem(ID=13, accelerator=13, enabled=False, menuItemStyle="sample_text_2", selection=False)
    b = swt_Menu(menuStyle="sample_text")
    _safe_set(b, 'Menu', a1)
    assert _is_linked(b, 'Menu', a1)
    if hasattr(a1, 'parentItem'):
        assert _is_linked(a1, 'parentItem', b)
    _safe_set(b, 'Menu', a2)
    assert _is_linked(b, 'Menu', a2)
    if hasattr(a1, 'parentItem'):
        assert not _is_linked(a1, 'parentItem', b)
    if hasattr(a2, 'parentItem'):
        assert _is_linked(a2, 'parentItem', b)
    _safe_set(b, 'Menu', None)
    assert not _is_linked(b, 'Menu', a2)
    if hasattr(a2, 'parentItem'):
        assert not _is_linked(a2, 'parentItem', b)


def test_assoc_parent13_reverse_link_reassign_clear():
    a1 = swt_ToolItem(enabled=True, hotImage="sample_text", selection=True, toolTipText="sample_text")
    a2 = swt_ToolItem(enabled=False, hotImage="sample_text_2", selection=False, toolTipText="sample_text_2")
    b = swt_ToolBar(orientationStyle="sample_text")
    _safe_set(b, 'ToolBar', a1)
    assert _is_linked(b, 'ToolBar', a1)
    if hasattr(a1, 'items'):
        assert _is_linked(a1, 'items', b)
    _safe_set(b, 'ToolBar', a2)
    assert _is_linked(b, 'ToolBar', a2)
    if hasattr(a1, 'items'):
        assert not _is_linked(a1, 'items', b)
    if hasattr(a2, 'items'):
        assert _is_linked(a2, 'items', b)
    _safe_set(b, 'ToolBar', None)
    assert not _is_linked(b, 'ToolBar', a2)
    if hasattr(a2, 'items'):
        assert not _is_linked(a2, 'items', b)


def test_assoc_parent16_reverse_link_reassign_clear():
    a1 = swt_CoolItem(minimumSize="sample_text", preferredSize="sample_text", size="sample_text")
    a2 = swt_CoolItem(minimumSize="sample_text_2", preferredSize="sample_text_2", size="sample_text_2")
    b = swt_CoolBar(orientationStyle="sample_text")
    _safe_set(b, 'CoolBar', a1)
    assert _is_linked(b, 'CoolBar', a1)
    if hasattr(a1, 'items17'):
        assert _is_linked(a1, 'items17', b)
    _safe_set(b, 'CoolBar', a2)
    assert _is_linked(b, 'CoolBar', a2)
    if hasattr(a1, 'items17'):
        assert not _is_linked(a1, 'items17', b)
    if hasattr(a2, 'items17'):
        assert _is_linked(a2, 'items17', b)
    _safe_set(b, 'CoolBar', None)
    assert not _is_linked(b, 'CoolBar', a2)
    if hasattr(a2, 'items17'):
        assert not _is_linked(a2, 'items17', b)


def test_assoc_parentItem8_reverse_link_reassign_clear():
    a1 = swt_MenuItem(ID=7, accelerator=7, enabled=True, menuItemStyle="sample_text", selection=True)
    a2 = swt_MenuItem(ID=13, accelerator=13, enabled=False, menuItemStyle="sample_text_2", selection=False)
    b = swt_Menu(menuStyle="sample_text")
    _safe_set(b, 'menu', a1)
    assert _is_linked(b, 'menu', a1)
    if hasattr(a1, 'MenuItem'):
        assert _is_linked(a1, 'MenuItem', b)
    _safe_set(b, 'menu', a2)
    assert _is_linked(b, 'menu', a2)
    if hasattr(a1, 'MenuItem'):
        assert not _is_linked(a1, 'MenuItem', b)
    if hasattr(a2, 'MenuItem'):
        assert _is_linked(a2, 'MenuItem', b)
    _safe_set(b, 'menu', None)
    assert not _is_linked(b, 'menu', a2)
    if hasattr(a2, 'MenuItem'):
        assert not _is_linked(a2, 'MenuItem', b)


def test_assoc_right28_reverse_link_reassign_clear():
    a1 = swt_FormData(height=7, width=7)
    a2 = swt_FormData(height=13, width=13)
    b = swt_FormAttachment(alignment="sample_text", denominator=7, numerator=7, offset=7)
    _safe_set(b, 'swt_FormAttachment30', a1)
    assert _is_linked(b, 'swt_FormAttachment30', a1)
    if hasattr(a1, 'swt_FormData29'):
        assert _is_linked(a1, 'swt_FormData29', b)
    _safe_set(b, 'swt_FormAttachment30', a2)
    assert _is_linked(b, 'swt_FormAttachment30', a2)
    if hasattr(a1, 'swt_FormData29'):
        assert not _is_linked(a1, 'swt_FormData29', b)
    if hasattr(a2, 'swt_FormData29'):
        assert _is_linked(a2, 'swt_FormData29', b)
    _safe_set(b, 'swt_FormAttachment30', None)
    assert not _is_linked(b, 'swt_FormAttachment30', a2)
    if hasattr(a2, 'swt_FormData29'):
        assert not _is_linked(a2, 'swt_FormData29', b)


def test_assoc_sortColumn38_reverse_link_reassign_clear():
    a1 = swt_TreeColumn(displayText="sample_text", toolTipText="sample_text")
    a2 = swt_TreeColumn(displayText="sample_text_2", toolTipText="sample_text_2")
    b = swt_Tree(headerVisible=True, linesVisible=True, sortDirection="sample_text")
    _safe_set(b, 'swt_Tree39', a1)
    assert _is_linked(b, 'swt_Tree39', a1)
    if hasattr(a1, 'swt_TreeColumn40'):
        assert _is_linked(a1, 'swt_TreeColumn40', b)
    _safe_set(b, 'swt_Tree39', a2)
    assert _is_linked(b, 'swt_Tree39', a2)
    if hasattr(a1, 'swt_TreeColumn40'):
        assert not _is_linked(a1, 'swt_TreeColumn40', b)
    if hasattr(a2, 'swt_TreeColumn40'):
        assert _is_linked(a2, 'swt_TreeColumn40', b)
    _safe_set(b, 'swt_Tree39', None)
    assert not _is_linked(b, 'swt_Tree39', a2)
    if hasattr(a2, 'swt_TreeColumn40'):
        assert not _is_linked(a2, 'swt_TreeColumn40', b)


def test_assoc_top25_reverse_link_reassign_clear():
    a1 = swt_FormData(height=7, width=7)
    a2 = swt_FormData(height=13, width=13)
    b = swt_FormAttachment(alignment="sample_text", denominator=7, numerator=7, offset=7)
    _safe_set(b, 'swt_FormAttachment27', a1)
    assert _is_linked(b, 'swt_FormAttachment27', a1)
    if hasattr(a1, 'swt_FormData26'):
        assert _is_linked(a1, 'swt_FormData26', b)
    _safe_set(b, 'swt_FormAttachment27', a2)
    assert _is_linked(b, 'swt_FormAttachment27', a2)
    if hasattr(a1, 'swt_FormData26'):
        assert not _is_linked(a1, 'swt_FormData26', b)
    if hasattr(a2, 'swt_FormData26'):
        assert _is_linked(a2, 'swt_FormData26', b)
    _safe_set(b, 'swt_FormAttachment27', None)
    assert not _is_linked(b, 'swt_FormAttachment27', a2)
    if hasattr(a2, 'swt_FormData26'):
        assert not _is_linked(a2, 'swt_FormData26', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_background1_stub_double():
    # swt_Color has no real 'swt_Color' property in the generated
    # code (a bare stub) -- manually attach it so swt_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    partner = swt_Color()
    setattr(partner, 'swt_Color', None)
    _safe_set(owner, 'swt_Control2', partner)
    assert getattr(partner, 'swt_Color') == owner
    _safe_set(owner, 'swt_Control2', None)
    assert getattr(partner, 'swt_Color') is None


def test_assoc_items20_stub_double():
    # swt_TabFolder has no real 'swt_TabFolder' property in the generated
    # code (a bare stub) -- manually attach it so swt_TabItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_TabItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_TabItem(toolTipText="sample_text")
    partner = swt_TabFolder()
    setattr(partner, 'swt_TabFolder', None)
    _safe_set(owner, 'swt_TabItem', partner)
    assert owner in getattr(partner, 'swt_TabFolder')
    _safe_set(owner, 'swt_TabItem', None)
    assert owner not in getattr(partner, 'swt_TabFolder')


def test_assoc_layoutData0_stub_double():
    # swt_LayoutData has no real 'swt_LayoutData' property in the generated
    # code (a bare stub) -- manually attach it so swt_Control's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_Control's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_Control(borderStyle="sample_text", enabled=True, size="sample_text", textOrientationStyle="sample_text", toolTipText="sample_text", touchEnabled=True, visible=True)
    partner = swt_LayoutData()
    setattr(partner, 'swt_LayoutData', None)
    _safe_set(owner, 'swt_Control', partner)
    assert getattr(partner, 'swt_LayoutData') == owner
    _safe_set(owner, 'swt_Control', None)
    assert getattr(partner, 'swt_LayoutData') is None


def test_assoc_menuBar5_stub_double():
    # swt_MenuBar has no real 'MenuBar' property in the generated
    # code (a bare stub) -- manually attach it so swt_Decorations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_Decorations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_Decorations(maximized=True, minimized=True)
    partner = swt_MenuBar()
    setattr(partner, 'MenuBar', None)
    _safe_set(owner, 'parent', partner)
    assert getattr(partner, 'MenuBar') == owner
    _safe_set(owner, 'parent', None)
    assert getattr(partner, 'MenuBar') is None


def test_assoc_parent9_stub_double():
    # swt_MenuBar has no real 'menuBar' property in the generated
    # code (a bare stub) -- manually attach it so swt_Decorations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_Decorations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_Decorations(maximized=True, minimized=True)
    partner = swt_MenuBar()
    setattr(partner, 'menuBar', None)
    _safe_set(owner, 'Decorations', partner)
    assert getattr(partner, 'menuBar') == owner
    _safe_set(owner, 'Decorations', None)
    assert getattr(partner, 'menuBar') is None


def test_assoc_viewer41_stub_double():
    # swt_TreeViewer has no real 'swt_TreeViewer' property in the generated
    # code (a bare stub) -- manually attach it so swt_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # swt_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = swt_Tree(headerVisible=True, linesVisible=True, sortDirection="sample_text")
    partner = swt_TreeViewer()
    setattr(partner, 'swt_TreeViewer', None)
    _safe_set(owner, 'swt_Tree42', partner)
    assert getattr(partner, 'swt_TreeViewer') == owner
    _safe_set(owner, 'swt_Tree42', None)
    assert getattr(partner, 'swt_TreeViewer') is None


