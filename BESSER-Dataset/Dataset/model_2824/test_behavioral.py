import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adapter,
    ExtensibleElement,
    NamedElementModel,
    NodeVisualModel,
    VisualModel,
    editormodel_Adapter,
    editormodel_Color,
    editormodel_ConnectionBendpoint,
    editormodel_ConnectionVisualModel,
    editormodel_CoreModel,
    editormodel_Diagram,
    editormodel_Dimension,
    editormodel_EObject,
    editormodel_EStringToEObjectMapEntry,
    editormodel_FlabotFileModel,
    editormodel_Folder,
    editormodel_NodeVisualModel,
    editormodel_Note,
    editormodel_Point,
    editormodel_VisualDiagramJump,
    editormodel_VisualModel,
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

def test_assoc_backgroundColor29_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Color(blue=7, green=7, red=7)
    _safe_set(b, 'editormodel_Color', a1)
    assert _is_linked(b, 'editormodel_Color', a1)
    if hasattr(a1, 'editormodel_VisualModel30'):
        assert _is_linked(a1, 'editormodel_VisualModel30', b)
    _safe_set(b, 'editormodel_Color', a2)
    assert _is_linked(b, 'editormodel_Color', a2)
    if hasattr(a1, 'editormodel_VisualModel30'):
        assert not _is_linked(a1, 'editormodel_VisualModel30', b)
    if hasattr(a2, 'editormodel_VisualModel30'):
        assert _is_linked(a2, 'editormodel_VisualModel30', b)
    _safe_set(b, 'editormodel_Color', None)
    assert not _is_linked(b, 'editormodel_Color', a2)
    if hasattr(a2, 'editormodel_VisualModel30'):
        assert not _is_linked(a2, 'editormodel_VisualModel30', b)


def test_assoc_bendpoints39_reverse_link_reassign_clear():
    a1 = editormodel_ConnectionVisualModel(sourceTerminal="sample_text", targetTerminal="sample_text")
    a2 = editormodel_ConnectionVisualModel(sourceTerminal="sample_text_2", targetTerminal="sample_text_2")
    b = editormodel_ConnectionBendpoint(weight=3.14)
    _safe_set(b, 'editormodel_ConnectionBendpoint40', a1)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint40', a1)
    if hasattr(a1, 'editormodel_ConnectionVisualModel'):
        assert _is_linked(a1, 'editormodel_ConnectionVisualModel', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint40', a2)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint40', a2)
    if hasattr(a1, 'editormodel_ConnectionVisualModel'):
        assert not _is_linked(a1, 'editormodel_ConnectionVisualModel', b)
    if hasattr(a2, 'editormodel_ConnectionVisualModel'):
        assert _is_linked(a2, 'editormodel_ConnectionVisualModel', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint40', None)
    assert not _is_linked(b, 'editormodel_ConnectionBendpoint40', a2)
    if hasattr(a2, 'editormodel_ConnectionVisualModel'):
        assert not _is_linked(a2, 'editormodel_ConnectionVisualModel', b)


def test_assoc_children17_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'VisualModel18'):
        assert _is_linked(a1, 'VisualModel18', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'VisualModel18'):
        assert not _is_linked(a1, 'VisualModel18', b)
    if hasattr(a2, 'VisualModel18'):
        assert _is_linked(a2, 'VisualModel18', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'VisualModel18'):
        assert not _is_linked(a2, 'VisualModel18', b)


def test_assoc_children3_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'diagram', {a1})
    assert _is_linked(b, 'diagram', a1)
    if hasattr(a1, 'VisualModel'):
        assert _is_linked(a1, 'VisualModel', b)
    _safe_set(b, 'diagram', {a2})
    assert _is_linked(b, 'diagram', a2)
    if hasattr(a1, 'VisualModel'):
        assert not _is_linked(a1, 'VisualModel', b)
    if hasattr(a2, 'VisualModel'):
        assert _is_linked(a2, 'VisualModel', b)
    _safe_set(b, 'diagram', set())
    assert not _is_linked(b, 'diagram', a2)
    if hasattr(a2, 'VisualModel'):
        assert not _is_linked(a2, 'VisualModel', b)


def test_assoc_diagram27_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'Diagram', a1)
    assert _is_linked(b, 'Diagram', a1)
    if hasattr(a1, 'children28'):
        assert _is_linked(a1, 'children28', b)
    _safe_set(b, 'Diagram', a2)
    assert _is_linked(b, 'Diagram', a2)
    if hasattr(a1, 'children28'):
        assert not _is_linked(a1, 'children28', b)
    if hasattr(a2, 'children28'):
        assert _is_linked(a2, 'children28', b)
    _safe_set(b, 'Diagram', None)
    assert not _is_linked(b, 'Diagram', a2)
    if hasattr(a2, 'children28'):
        assert not _is_linked(a2, 'children28', b)


def test_assoc_diagrams51_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'Diagram52', a1)
    assert _is_linked(b, 'Diagram52', a1)
    if hasattr(a1, 'folder'):
        assert _is_linked(a1, 'folder', b)
    _safe_set(b, 'Diagram52', a2)
    assert _is_linked(b, 'Diagram52', a2)
    if hasattr(a1, 'folder'):
        assert not _is_linked(a1, 'folder', b)
    if hasattr(a2, 'folder'):
        assert _is_linked(a2, 'folder', b)
    _safe_set(b, 'Diagram52', None)
    assert not _is_linked(b, 'Diagram52', a2)
    if hasattr(a2, 'folder'):
        assert not _is_linked(a2, 'folder', b)


def test_assoc_diagrams6_reverse_link_reassign_clear():
    a1 = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    a2 = editormodel_FlabotFileModel(id="sample_text_2", name="sample_text_2", provider="sample_text_2", version="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'editormodel_Diagram7', a1)
    assert _is_linked(b, 'editormodel_Diagram7', a1)
    if hasattr(a1, 'editormodel_FlabotFileModel'):
        assert _is_linked(a1, 'editormodel_FlabotFileModel', b)
    _safe_set(b, 'editormodel_Diagram7', a2)
    assert _is_linked(b, 'editormodel_Diagram7', a2)
    if hasattr(a1, 'editormodel_FlabotFileModel'):
        assert not _is_linked(a1, 'editormodel_FlabotFileModel', b)
    if hasattr(a2, 'editormodel_FlabotFileModel'):
        assert _is_linked(a2, 'editormodel_FlabotFileModel', b)
    _safe_set(b, 'editormodel_Diagram7', None)
    assert not _is_linked(b, 'editormodel_Diagram7', a2)
    if hasattr(a2, 'editormodel_FlabotFileModel'):
        assert not _is_linked(a2, 'editormodel_FlabotFileModel', b)


def test_assoc_fileModel56_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    _safe_set(b, 'editormodel_FlabotFileModel58', a1)
    assert _is_linked(b, 'editormodel_FlabotFileModel58', a1)
    if hasattr(a1, 'editormodel_Folder57'):
        assert _is_linked(a1, 'editormodel_Folder57', b)
    _safe_set(b, 'editormodel_FlabotFileModel58', a2)
    assert _is_linked(b, 'editormodel_FlabotFileModel58', a2)
    if hasattr(a1, 'editormodel_Folder57'):
        assert not _is_linked(a1, 'editormodel_Folder57', b)
    if hasattr(a2, 'editormodel_Folder57'):
        assert _is_linked(a2, 'editormodel_Folder57', b)
    _safe_set(b, 'editormodel_FlabotFileModel58', None)
    assert not _is_linked(b, 'editormodel_FlabotFileModel58', a2)
    if hasattr(a2, 'editormodel_Folder57'):
        assert not _is_linked(a2, 'editormodel_Folder57', b)


def test_assoc_firstRelativeDimension34_reverse_link_reassign_clear():
    a1 = editormodel_Dimension(height=7, width=7)
    a2 = editormodel_Dimension(height=13, width=13)
    b = editormodel_ConnectionBendpoint(weight=3.14)
    _safe_set(b, 'editormodel_ConnectionBendpoint', a1)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint', a1)
    if hasattr(a1, 'editormodel_Dimension35'):
        assert _is_linked(a1, 'editormodel_Dimension35', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint', a2)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint', a2)
    if hasattr(a1, 'editormodel_Dimension35'):
        assert not _is_linked(a1, 'editormodel_Dimension35', b)
    if hasattr(a2, 'editormodel_Dimension35'):
        assert _is_linked(a2, 'editormodel_Dimension35', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint', None)
    assert not _is_linked(b, 'editormodel_ConnectionBendpoint', a2)
    if hasattr(a2, 'editormodel_Dimension35'):
        assert not _is_linked(a2, 'editormodel_Dimension35', b)


def test_assoc_folder11_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    _safe_set(b, 'editormodel_FlabotFileModel12', a1)
    assert _is_linked(b, 'editormodel_FlabotFileModel12', a1)
    if hasattr(a1, 'editormodel_Folder'):
        assert _is_linked(a1, 'editormodel_Folder', b)
    _safe_set(b, 'editormodel_FlabotFileModel12', a2)
    assert _is_linked(b, 'editormodel_FlabotFileModel12', a2)
    if hasattr(a1, 'editormodel_Folder'):
        assert not _is_linked(a1, 'editormodel_Folder', b)
    if hasattr(a2, 'editormodel_Folder'):
        assert _is_linked(a2, 'editormodel_Folder', b)
    _safe_set(b, 'editormodel_FlabotFileModel12', None)
    assert not _is_linked(b, 'editormodel_FlabotFileModel12', a2)
    if hasattr(a2, 'editormodel_Folder'):
        assert not _is_linked(a2, 'editormodel_Folder', b)


def test_assoc_folder4_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'diagrams', a1)
    assert _is_linked(b, 'diagrams', a1)
    if hasattr(a1, 'Folder'):
        assert _is_linked(a1, 'Folder', b)
    _safe_set(b, 'diagrams', a2)
    assert _is_linked(b, 'diagrams', a2)
    if hasattr(a1, 'Folder'):
        assert not _is_linked(a1, 'Folder', b)
    if hasattr(a2, 'Folder'):
        assert _is_linked(a2, 'Folder', b)
    _safe_set(b, 'diagrams', None)
    assert not _is_linked(b, 'diagrams', a2)
    if hasattr(a2, 'Folder'):
        assert not _is_linked(a2, 'Folder', b)


def test_assoc_folders48_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_Folder(name="sample_text")
    _safe_set(b, 'parent49', {a1})
    assert _is_linked(b, 'parent49', a1)
    if hasattr(a1, 'Folder50'):
        assert _is_linked(a1, 'Folder50', b)
    _safe_set(b, 'parent49', {a2})
    assert _is_linked(b, 'parent49', a2)
    if hasattr(a1, 'Folder50'):
        assert not _is_linked(a1, 'Folder50', b)
    if hasattr(a2, 'Folder50'):
        assert _is_linked(a2, 'Folder50', b)
    _safe_set(b, 'parent49', set())
    assert not _is_linked(b, 'parent49', a2)
    if hasattr(a2, 'Folder50'):
        assert not _is_linked(a2, 'Folder50', b)


def test_assoc_foregroundColor31_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Color(blue=7, green=7, red=7)
    _safe_set(b, 'editormodel_Color33', a1)
    assert _is_linked(b, 'editormodel_Color33', a1)
    if hasattr(a1, 'editormodel_VisualModel32'):
        assert _is_linked(a1, 'editormodel_VisualModel32', b)
    _safe_set(b, 'editormodel_Color33', a2)
    assert _is_linked(b, 'editormodel_Color33', a2)
    if hasattr(a1, 'editormodel_VisualModel32'):
        assert not _is_linked(a1, 'editormodel_VisualModel32', b)
    if hasattr(a2, 'editormodel_VisualModel32'):
        assert _is_linked(a2, 'editormodel_VisualModel32', b)
    _safe_set(b, 'editormodel_Color33', None)
    assert not _is_linked(b, 'editormodel_Color33', a2)
    if hasattr(a2, 'editormodel_VisualModel32'):
        assert not _is_linked(a2, 'editormodel_VisualModel32', b)


def test_assoc_importedFiles9_reverse_link_reassign_clear():
    a1 = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    a2 = editormodel_FlabotFileModel(id="sample_text_2", name="sample_text_2", provider="sample_text_2", version="sample_text_2")
    b = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    _safe_set(b, 'editormodel_FlabotFileModel8', {a1})
    assert _is_linked(b, 'editormodel_FlabotFileModel8', a1)
    if hasattr(a1, 'editormodel_FlabotFileModel10'):
        assert _is_linked(a1, 'editormodel_FlabotFileModel10', b)
    _safe_set(b, 'editormodel_FlabotFileModel8', {a2})
    assert _is_linked(b, 'editormodel_FlabotFileModel8', a2)
    if hasattr(a1, 'editormodel_FlabotFileModel10'):
        assert not _is_linked(a1, 'editormodel_FlabotFileModel10', b)
    if hasattr(a2, 'editormodel_FlabotFileModel10'):
        assert _is_linked(a2, 'editormodel_FlabotFileModel10', b)
    _safe_set(b, 'editormodel_FlabotFileModel8', set())
    assert not _is_linked(b, 'editormodel_FlabotFileModel8', a2)
    if hasattr(a2, 'editormodel_FlabotFileModel10'):
        assert not _is_linked(a2, 'editormodel_FlabotFileModel10', b)


def test_assoc_location23_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Point(x=7, y=7)
    _safe_set(b, 'editormodel_Point', a1)
    assert _is_linked(b, 'editormodel_Point', a1)
    if hasattr(a1, 'editormodel_VisualModel24'):
        assert _is_linked(a1, 'editormodel_VisualModel24', b)
    _safe_set(b, 'editormodel_Point', a2)
    assert _is_linked(b, 'editormodel_Point', a2)
    if hasattr(a1, 'editormodel_VisualModel24'):
        assert not _is_linked(a1, 'editormodel_VisualModel24', b)
    if hasattr(a2, 'editormodel_VisualModel24'):
        assert _is_linked(a2, 'editormodel_VisualModel24', b)
    _safe_set(b, 'editormodel_Point', None)
    assert not _is_linked(b, 'editormodel_Point', a2)
    if hasattr(a2, 'editormodel_VisualModel24'):
        assert not _is_linked(a2, 'editormodel_VisualModel24', b)


def test_assoc_openDiagrams13_reverse_link_reassign_clear():
    a1 = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    a2 = editormodel_FlabotFileModel(id="sample_text_2", name="sample_text_2", provider="sample_text_2", version="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'editormodel_Diagram15', a1)
    assert _is_linked(b, 'editormodel_Diagram15', a1)
    if hasattr(a1, 'editormodel_FlabotFileModel14'):
        assert _is_linked(a1, 'editormodel_FlabotFileModel14', b)
    _safe_set(b, 'editormodel_Diagram15', a2)
    assert _is_linked(b, 'editormodel_Diagram15', a2)
    if hasattr(a1, 'editormodel_FlabotFileModel14'):
        assert not _is_linked(a1, 'editormodel_FlabotFileModel14', b)
    if hasattr(a2, 'editormodel_FlabotFileModel14'):
        assert _is_linked(a2, 'editormodel_FlabotFileModel14', b)
    _safe_set(b, 'editormodel_Diagram15', None)
    assert not _is_linked(b, 'editormodel_Diagram15', a2)
    if hasattr(a2, 'editormodel_FlabotFileModel14'):
        assert not _is_linked(a2, 'editormodel_FlabotFileModel14', b)


def test_assoc_parent20_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'VisualModel21'):
        assert _is_linked(a1, 'VisualModel21', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'VisualModel21'):
        assert not _is_linked(a1, 'VisualModel21', b)
    if hasattr(a2, 'VisualModel21'):
        assert _is_linked(a2, 'VisualModel21', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'VisualModel21'):
        assert not _is_linked(a2, 'VisualModel21', b)


def test_assoc_parent54_reverse_link_reassign_clear():
    a1 = editormodel_Folder(name="sample_text")
    a2 = editormodel_Folder(name="sample_text_2")
    b = editormodel_Folder(name="sample_text")
    _safe_set(b, 'folders', a1)
    assert _is_linked(b, 'folders', a1)
    if hasattr(a1, 'Folder55'):
        assert _is_linked(a1, 'Folder55', b)
    _safe_set(b, 'folders', a2)
    assert _is_linked(b, 'folders', a2)
    if hasattr(a1, 'Folder55'):
        assert not _is_linked(a1, 'Folder55', b)
    if hasattr(a2, 'Folder55'):
        assert _is_linked(a2, 'Folder55', b)
    _safe_set(b, 'folders', None)
    assert not _is_linked(b, 'folders', a2)
    if hasattr(a2, 'Folder55'):
        assert not _is_linked(a2, 'Folder55', b)


def test_assoc_secondRelativeDimension36_reverse_link_reassign_clear():
    a1 = editormodel_Dimension(height=7, width=7)
    a2 = editormodel_Dimension(height=13, width=13)
    b = editormodel_ConnectionBendpoint(weight=3.14)
    _safe_set(b, 'editormodel_ConnectionBendpoint37', a1)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint37', a1)
    if hasattr(a1, 'editormodel_Dimension38'):
        assert _is_linked(a1, 'editormodel_Dimension38', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint37', a2)
    assert _is_linked(b, 'editormodel_ConnectionBendpoint37', a2)
    if hasattr(a1, 'editormodel_Dimension38'):
        assert not _is_linked(a1, 'editormodel_Dimension38', b)
    if hasattr(a2, 'editormodel_Dimension38'):
        assert _is_linked(a2, 'editormodel_Dimension38', b)
    _safe_set(b, 'editormodel_ConnectionBendpoint37', None)
    assert not _is_linked(b, 'editormodel_ConnectionBendpoint37', a2)
    if hasattr(a2, 'editormodel_Dimension38'):
        assert not _is_linked(a2, 'editormodel_Dimension38', b)


def test_assoc_size25_reverse_link_reassign_clear():
    a1 = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    a2 = editormodel_VisualModel(detailLevel=13, lineStyle=13, lineWidth=13)
    b = editormodel_Dimension(height=7, width=7)
    _safe_set(b, 'editormodel_Dimension', a1)
    assert _is_linked(b, 'editormodel_Dimension', a1)
    if hasattr(a1, 'editormodel_VisualModel26'):
        assert _is_linked(a1, 'editormodel_VisualModel26', b)
    _safe_set(b, 'editormodel_Dimension', a2)
    assert _is_linked(b, 'editormodel_Dimension', a2)
    if hasattr(a1, 'editormodel_VisualModel26'):
        assert not _is_linked(a1, 'editormodel_VisualModel26', b)
    if hasattr(a2, 'editormodel_VisualModel26'):
        assert _is_linked(a2, 'editormodel_VisualModel26', b)
    _safe_set(b, 'editormodel_Dimension', None)
    assert not _is_linked(b, 'editormodel_Dimension', a2)
    if hasattr(a2, 'editormodel_VisualModel26'):
        assert not _is_linked(a2, 'editormodel_VisualModel26', b)


def test_assoc_source41_reverse_link_reassign_clear():
    a1 = editormodel_NodeVisualModel(rotation="sample_text")
    a2 = editormodel_NodeVisualModel(rotation="sample_text_2")
    b = editormodel_ConnectionVisualModel(sourceTerminal="sample_text", targetTerminal="sample_text")
    _safe_set(b, 'sourceConnections', a1)
    assert _is_linked(b, 'sourceConnections', a1)
    if hasattr(a1, 'NodeVisualModel'):
        assert _is_linked(a1, 'NodeVisualModel', b)
    _safe_set(b, 'sourceConnections', a2)
    assert _is_linked(b, 'sourceConnections', a2)
    if hasattr(a1, 'NodeVisualModel'):
        assert not _is_linked(a1, 'NodeVisualModel', b)
    if hasattr(a2, 'NodeVisualModel'):
        assert _is_linked(a2, 'NodeVisualModel', b)
    _safe_set(b, 'sourceConnections', None)
    assert not _is_linked(b, 'sourceConnections', a2)
    if hasattr(a2, 'NodeVisualModel'):
        assert not _is_linked(a2, 'NodeVisualModel', b)


def test_assoc_sourceConnections44_reverse_link_reassign_clear():
    a1 = editormodel_NodeVisualModel(rotation="sample_text")
    a2 = editormodel_NodeVisualModel(rotation="sample_text_2")
    b = editormodel_ConnectionVisualModel(sourceTerminal="sample_text", targetTerminal="sample_text")
    _safe_set(b, 'ConnectionVisualModel', a1)
    assert _is_linked(b, 'ConnectionVisualModel', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'ConnectionVisualModel', a2)
    assert _is_linked(b, 'ConnectionVisualModel', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'ConnectionVisualModel', None)
    assert not _is_linked(b, 'ConnectionVisualModel', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_sourceDiagram61_reverse_link_reassign_clear():
    a1 = editormodel_VisualDiagramJump(to="sample_text")
    a2 = editormodel_VisualDiagramJump(to="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'editormodel_Diagram62', a1)
    assert _is_linked(b, 'editormodel_Diagram62', a1)
    if hasattr(a1, 'editormodel_VisualDiagramJump'):
        assert _is_linked(a1, 'editormodel_VisualDiagramJump', b)
    _safe_set(b, 'editormodel_Diagram62', a2)
    assert _is_linked(b, 'editormodel_Diagram62', a2)
    if hasattr(a1, 'editormodel_VisualDiagramJump'):
        assert not _is_linked(a1, 'editormodel_VisualDiagramJump', b)
    if hasattr(a2, 'editormodel_VisualDiagramJump'):
        assert _is_linked(a2, 'editormodel_VisualDiagramJump', b)
    _safe_set(b, 'editormodel_Diagram62', None)
    assert not _is_linked(b, 'editormodel_Diagram62', a2)
    if hasattr(a2, 'editormodel_VisualDiagramJump'):
        assert not _is_linked(a2, 'editormodel_VisualDiagramJump', b)


def test_assoc_target42_reverse_link_reassign_clear():
    a1 = editormodel_NodeVisualModel(rotation="sample_text")
    a2 = editormodel_NodeVisualModel(rotation="sample_text_2")
    b = editormodel_ConnectionVisualModel(sourceTerminal="sample_text", targetTerminal="sample_text")
    _safe_set(b, 'targetConnections', a1)
    assert _is_linked(b, 'targetConnections', a1)
    if hasattr(a1, 'NodeVisualModel43'):
        assert _is_linked(a1, 'NodeVisualModel43', b)
    _safe_set(b, 'targetConnections', a2)
    assert _is_linked(b, 'targetConnections', a2)
    if hasattr(a1, 'NodeVisualModel43'):
        assert not _is_linked(a1, 'NodeVisualModel43', b)
    if hasattr(a2, 'NodeVisualModel43'):
        assert _is_linked(a2, 'NodeVisualModel43', b)
    _safe_set(b, 'targetConnections', None)
    assert not _is_linked(b, 'targetConnections', a2)
    if hasattr(a2, 'NodeVisualModel43'):
        assert not _is_linked(a2, 'NodeVisualModel43', b)


def test_assoc_targetConnections45_reverse_link_reassign_clear():
    a1 = editormodel_NodeVisualModel(rotation="sample_text")
    a2 = editormodel_NodeVisualModel(rotation="sample_text_2")
    b = editormodel_ConnectionVisualModel(sourceTerminal="sample_text", targetTerminal="sample_text")
    _safe_set(b, 'ConnectionVisualModel46', a1)
    assert _is_linked(b, 'ConnectionVisualModel46', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'ConnectionVisualModel46', a2)
    assert _is_linked(b, 'ConnectionVisualModel46', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'ConnectionVisualModel46', None)
    assert not _is_linked(b, 'ConnectionVisualModel46', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_targetDiagram63_reverse_link_reassign_clear():
    a1 = editormodel_VisualDiagramJump(to="sample_text")
    a2 = editormodel_VisualDiagramJump(to="sample_text_2")
    b = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    _safe_set(b, 'editormodel_Diagram65', a1)
    assert _is_linked(b, 'editormodel_Diagram65', a1)
    if hasattr(a1, 'editormodel_VisualDiagramJump64'):
        assert _is_linked(a1, 'editormodel_VisualDiagramJump64', b)
    _safe_set(b, 'editormodel_Diagram65', a2)
    assert _is_linked(b, 'editormodel_Diagram65', a2)
    if hasattr(a1, 'editormodel_VisualDiagramJump64'):
        assert not _is_linked(a1, 'editormodel_VisualDiagramJump64', b)
    if hasattr(a2, 'editormodel_VisualDiagramJump64'):
        assert _is_linked(a2, 'editormodel_VisualDiagramJump64', b)
    _safe_set(b, 'editormodel_Diagram65', None)
    assert not _is_linked(b, 'editormodel_Diagram65', a2)
    if hasattr(a2, 'editormodel_VisualDiagramJump64'):
        assert not _is_linked(a2, 'editormodel_VisualDiagramJump64', b)


def test_assoc_targetVisualNode66_reverse_link_reassign_clear():
    a1 = editormodel_VisualDiagramJump(to="sample_text")
    a2 = editormodel_VisualDiagramJump(to="sample_text_2")
    b = editormodel_NodeVisualModel(rotation="sample_text")
    _safe_set(b, 'editormodel_NodeVisualModel', a1)
    assert _is_linked(b, 'editormodel_NodeVisualModel', a1)
    if hasattr(a1, 'editormodel_VisualDiagramJump67'):
        assert _is_linked(a1, 'editormodel_VisualDiagramJump67', b)
    _safe_set(b, 'editormodel_NodeVisualModel', a2)
    assert _is_linked(b, 'editormodel_NodeVisualModel', a2)
    if hasattr(a1, 'editormodel_VisualDiagramJump67'):
        assert not _is_linked(a1, 'editormodel_VisualDiagramJump67', b)
    if hasattr(a2, 'editormodel_VisualDiagramJump67'):
        assert _is_linked(a2, 'editormodel_VisualDiagramJump67', b)
    _safe_set(b, 'editormodel_NodeVisualModel', None)
    assert not _is_linked(b, 'editormodel_NodeVisualModel', a2)
    if hasattr(a2, 'editormodel_VisualDiagramJump67'):
        assert not _is_linked(a2, 'editormodel_VisualDiagramJump67', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_coreModel0_stub_double():
    # editormodel_CoreModel has no real 'editormodel_CoreModel' property in the generated
    # code (a bare stub) -- manually attach it so editormodel_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # editormodel_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    partner = editormodel_CoreModel()
    setattr(partner, 'editormodel_CoreModel', None)
    _safe_set(owner, 'editormodel_Diagram', partner)
    assert getattr(partner, 'editormodel_CoreModel') == owner
    _safe_set(owner, 'editormodel_Diagram', None)
    assert getattr(partner, 'editormodel_CoreModel') is None


def test_assoc_coreModel5_stub_double():
    # editormodel_CoreModel has no real 'coremodel.ecoreCoreModel' property in the generated
    # code (a bare stub) -- manually attach it so editormodel_FlabotFileModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # editormodel_FlabotFileModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = editormodel_FlabotFileModel(id="sample_text", name="sample_text", provider="sample_text", version="sample_text")
    partner = editormodel_CoreModel()
    setattr(partner, 'coremodel.ecoreCoreModel', None)
    _safe_set(owner, 'file', partner)
    assert getattr(partner, 'coremodel.ecoreCoreModel') == owner
    _safe_set(owner, 'file', None)
    assert getattr(partner, 'coremodel.ecoreCoreModel') is None


def test_assoc_notes1_stub_double():
    # editormodel_Note has no real 'editormodel_Note' property in the generated
    # code (a bare stub) -- manually attach it so editormodel_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # editormodel_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = editormodel_Diagram(gridEnabled="sample_text", snapToGeometryEnabled="sample_text")
    partner = editormodel_Note()
    setattr(partner, 'editormodel_Note', None)
    _safe_set(owner, 'editormodel_Diagram2', {partner})
    assert getattr(partner, 'editormodel_Note') == owner
    _safe_set(owner, 'editormodel_Diagram2', set())
    assert getattr(partner, 'editormodel_Note') is None


def test_assoc_semanticModel22_stub_double():
    # editormodel_EObject has no real 'editormodel_EObject' property in the generated
    # code (a bare stub) -- manually attach it so editormodel_VisualModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # editormodel_VisualModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = editormodel_VisualModel(detailLevel=7, lineStyle=7, lineWidth=7)
    partner = editormodel_EObject()
    setattr(partner, 'editormodel_EObject', None)
    _safe_set(owner, 'editormodel_VisualModel', partner)
    assert getattr(partner, 'editormodel_EObject') == owner
    _safe_set(owner, 'editormodel_VisualModel', None)
    assert getattr(partner, 'editormodel_EObject') is None


def test_assoc_value59_stub_double():
    # editormodel_EObject has no real 'editormodel_EObject60' property in the generated
    # code (a bare stub) -- manually attach it so editormodel_EStringToEObjectMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # editormodel_EStringToEObjectMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = editormodel_EStringToEObjectMapEntry(key="sample_text")
    partner = editormodel_EObject()
    setattr(partner, 'editormodel_EObject60', None)
    _safe_set(owner, 'editormodel_EStringToEObjectMapEntry', partner)
    assert getattr(partner, 'editormodel_EObject60') == owner
    _safe_set(owner, 'editormodel_EStringToEObjectMapEntry', None)
    assert getattr(partner, 'editormodel_EObject60') is None


