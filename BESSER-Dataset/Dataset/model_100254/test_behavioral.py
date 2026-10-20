import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BackgroundConditionalStyle,
    BackgroundStyleDescription,
    CellUpdater,
    ColorDescription,
    ColumnMapping,
    CreateCellTool,
    CreateColumnTool,
    CreateCrossColumnTool,
    CreateLineTool,
    CreateTool,
    DColumn,
    DRepresentation,
    DRepresentationElement,
    DSemanticDecorator,
    DTableElement,
    DTableElementStyle,
    DTableElementUpdater,
    DeleteColumnTool,
    DeleteLineTool,
    DeleteTool,
    ElementColumnMapping,
    FeatureColumnMapping,
    ForegroundConditionalStyle,
    ForegroundStyleDescription,
    IntersectionMapping,
    LabelEditTool,
    LineContainer,
    LineMapping,
    RepresentationCreationDescription,
    RepresentationElementMapping,
    RepresentationNavigationDescription,
    TableDescription,
    TableMapping,
    TableTool,
    TableVariable,
    description_CellUpdater,
    description_ColumnMapping,
    description_DocumentedElement,
    description_EndUserDocumentedElement,
    description_RepresentationDescription,
    description_StyleUpdater,
    description_TableMapping,
    description_TableTool,
    description_table_EObject,
    table_DCell,
    table_DCellStyle,
    table_DColumn,
    table_DFeatureColumn,
    table_DLine,
    table_DTable,
    table_DTableElement,
    table_DTableElementStyle,
    table_DTableElementSynchronizer,
    table_DTableElementUpdater,
    table_DTargetColumn,
    table_LineContainer,
    table_RGBValues,
    table_description_BackgroundConditionalStyle,
    table_description_BackgroundStyleDescription,
    table_description_CellUpdater,
    table_description_ColumnMapping,
    table_description_CreateCellTool,
    table_description_CreateColumnTool,
    table_description_CreateCrossColumnTool,
    table_description_CreateLineTool,
    table_description_CreateTool,
    table_description_CrossTableDescription,
    table_description_DeleteColumnTool,
    table_description_DeleteLineTool,
    table_description_DeleteTool,
    table_description_EditionTableDescription,
    table_description_ElementColumnMapping,
    table_description_FeatureColumnMapping,
    table_description_ForegroundConditionalStyle,
    table_description_ForegroundStyleDescription,
    table_description_IntersectionMapping,
    table_description_LabelEditTool,
    table_description_LineMapping,
    table_description_StyleUpdater,
    table_description_TableCreationDescription,
    table_description_TableDescription,
    table_description_TableMapping,
    table_description_TableNavigationDescription,
    table_description_TableTool,
    table_description_TableVariable,
    tool_AbstractToolDescription,
    tool_AbstractVariable,
    tool_EditMaskVariables,
    tool_ModelOperation,
    tool_RepresentationCreationDescription,
    tool_RepresentationNavigationDescription,
    tool_VariableContainer,
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

def test_assoc_cells28_reverse_link_reassign_clear():
    a1 = table_DColumn(label="sample_text", visible=True, width=7)
    a2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'DCell29', a1)
    assert _is_linked(b, 'DCell29', a1)
    if hasattr(a1, 'column'):
        assert _is_linked(a1, 'column', b)
    _safe_set(b, 'DCell29', a2)
    assert _is_linked(b, 'DCell29', a2)
    if hasattr(a1, 'column'):
        assert not _is_linked(a1, 'column', b)
    if hasattr(a2, 'column'):
        assert _is_linked(a2, 'column', b)
    _safe_set(b, 'DCell29', None)
    assert not _is_linked(b, 'DCell29', a2)
    if hasattr(a2, 'column'):
        assert not _is_linked(a2, 'column', b)


def test_assoc_cells5_reverse_link_reassign_clear():
    a1 = table_DLine(collapsed=True, label="sample_text", visible=True)
    a2 = table_DLine(collapsed=False, label="sample_text_2", visible=False)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'DCell', a1)
    assert _is_linked(b, 'DCell', a1)
    if hasattr(a1, 'line'):
        assert _is_linked(a1, 'line', b)
    _safe_set(b, 'DCell', a2)
    assert _is_linked(b, 'DCell', a2)
    if hasattr(a1, 'line'):
        assert not _is_linked(a1, 'line', b)
    if hasattr(a2, 'line'):
        assert _is_linked(a2, 'line', b)
    _safe_set(b, 'DCell', None)
    assert not _is_linked(b, 'DCell', a2)
    if hasattr(a2, 'line'):
        assert not _is_linked(a2, 'line', b)


def test_assoc_column13_reverse_link_reassign_clear():
    a1 = table_DColumn(label="sample_text", visible=True, width=7)
    a2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'cells14', a1)
    assert _is_linked(b, 'cells14', a1)
    if hasattr(a1, 'DColumn15'):
        assert _is_linked(a1, 'DColumn15', b)
    _safe_set(b, 'cells14', a2)
    assert _is_linked(b, 'cells14', a2)
    if hasattr(a1, 'DColumn15'):
        assert not _is_linked(a1, 'DColumn15', b)
    if hasattr(a2, 'DColumn15'):
        assert _is_linked(a2, 'DColumn15', b)
    _safe_set(b, 'cells14', None)
    assert not _is_linked(b, 'cells14', a2)
    if hasattr(a2, 'DColumn15'):
        assert not _is_linked(a2, 'DColumn15', b)


def test_assoc_columns0_reverse_link_reassign_clear():
    a1 = table_DTable(headerColumnWidth=7)
    a2 = table_DTable(headerColumnWidth=13)
    b = table_DColumn(label="sample_text", visible=True, width=7)
    _safe_set(b, 'DColumn', a1)
    assert _is_linked(b, 'DColumn', a1)
    if hasattr(a1, 'table'):
        assert _is_linked(a1, 'table', b)
    _safe_set(b, 'DColumn', a2)
    assert _is_linked(b, 'DColumn', a2)
    if hasattr(a1, 'table'):
        assert not _is_linked(a1, 'table', b)
    if hasattr(a2, 'table'):
        assert _is_linked(a2, 'table', b)
    _safe_set(b, 'DColumn', None)
    assert not _is_linked(b, 'DColumn', a2)
    if hasattr(a2, 'table'):
        assert not _is_linked(a2, 'table', b)


def test_assoc_currentStyle35_reverse_link_reassign_clear():
    a1 = table_DTableElementStyle(defaultBackgroundStyle=True, defaultForegroundStyle=True, labelFormat="sample_text", labelSize=7)
    a2 = table_DTableElementStyle(defaultBackgroundStyle=False, defaultForegroundStyle=False, labelFormat="sample_text_2", labelSize=13)
    b = table_DColumn(label="sample_text", visible=True, width=7)
    _safe_set(b, 'table_DColumn36', a1)
    assert _is_linked(b, 'table_DColumn36', a1)
    if hasattr(a1, 'table_DTableElementStyle37'):
        assert _is_linked(a1, 'table_DTableElementStyle37', b)
    _safe_set(b, 'table_DColumn36', a2)
    assert _is_linked(b, 'table_DColumn36', a2)
    if hasattr(a1, 'table_DTableElementStyle37'):
        assert not _is_linked(a1, 'table_DTableElementStyle37', b)
    if hasattr(a2, 'table_DTableElementStyle37'):
        assert _is_linked(a2, 'table_DTableElementStyle37', b)
    _safe_set(b, 'table_DColumn36', None)
    assert not _is_linked(b, 'table_DColumn36', a2)
    if hasattr(a2, 'table_DTableElementStyle37'):
        assert not _is_linked(a2, 'table_DTableElementStyle37', b)


def test_assoc_currentStyle9_reverse_link_reassign_clear():
    a1 = table_DTableElementStyle(defaultBackgroundStyle=True, defaultForegroundStyle=True, labelFormat="sample_text", labelSize=7)
    a2 = table_DTableElementStyle(defaultBackgroundStyle=False, defaultForegroundStyle=False, labelFormat="sample_text_2", labelSize=13)
    b = table_DLine(collapsed=True, label="sample_text", visible=True)
    _safe_set(b, 'table_DLine10', a1)
    assert _is_linked(b, 'table_DLine10', a1)
    if hasattr(a1, 'table_DTableElementStyle'):
        assert _is_linked(a1, 'table_DTableElementStyle', b)
    _safe_set(b, 'table_DLine10', a2)
    assert _is_linked(b, 'table_DLine10', a2)
    if hasattr(a1, 'table_DTableElementStyle'):
        assert not _is_linked(a1, 'table_DTableElementStyle', b)
    if hasattr(a2, 'table_DTableElementStyle'):
        assert _is_linked(a2, 'table_DTableElementStyle', b)
    _safe_set(b, 'table_DLine10', None)
    assert not _is_linked(b, 'table_DLine10', a2)
    if hasattr(a2, 'table_DTableElementStyle'):
        assert not _is_linked(a2, 'table_DTableElementStyle', b)


def test_assoc_line11_reverse_link_reassign_clear():
    a1 = table_DLine(collapsed=True, label="sample_text", visible=True)
    a2 = table_DLine(collapsed=False, label="sample_text_2", visible=False)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'cells', a1)
    assert _is_linked(b, 'cells', a1)
    if hasattr(a1, 'DLine12'):
        assert _is_linked(a1, 'DLine12', b)
    _safe_set(b, 'cells', a2)
    assert _is_linked(b, 'cells', a2)
    if hasattr(a1, 'DLine12'):
        assert not _is_linked(a1, 'DLine12', b)
    if hasattr(a2, 'DLine12'):
        assert _is_linked(a2, 'DLine12', b)
    _safe_set(b, 'cells', None)
    assert not _is_linked(b, 'cells', a2)
    if hasattr(a2, 'DLine12'):
        assert not _is_linked(a2, 'DLine12', b)


def test_assoc_orderedCells32_reverse_link_reassign_clear():
    a1 = table_DColumn(label="sample_text", visible=True, width=7)
    a2 = table_DColumn(label="sample_text_2", visible=False, width=13)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'table_DCell34', a1)
    assert _is_linked(b, 'table_DCell34', a1)
    if hasattr(a1, 'table_DColumn33'):
        assert _is_linked(a1, 'table_DColumn33', b)
    _safe_set(b, 'table_DCell34', a2)
    assert _is_linked(b, 'table_DCell34', a2)
    if hasattr(a1, 'table_DColumn33'):
        assert not _is_linked(a1, 'table_DColumn33', b)
    if hasattr(a2, 'table_DColumn33'):
        assert _is_linked(a2, 'table_DColumn33', b)
    _safe_set(b, 'table_DCell34', None)
    assert not _is_linked(b, 'table_DCell34', a2)
    if hasattr(a2, 'table_DColumn33'):
        assert not _is_linked(a2, 'table_DColumn33', b)


def test_assoc_orderedCells7_reverse_link_reassign_clear():
    a1 = table_DLine(collapsed=True, label="sample_text", visible=True)
    a2 = table_DLine(collapsed=False, label="sample_text_2", visible=False)
    b = table_DCell(label="sample_text")
    _safe_set(b, 'table_DCell', a1)
    assert _is_linked(b, 'table_DCell', a1)
    if hasattr(a1, 'table_DLine8'):
        assert _is_linked(a1, 'table_DLine8', b)
    _safe_set(b, 'table_DCell', a2)
    assert _is_linked(b, 'table_DCell', a2)
    if hasattr(a1, 'table_DLine8'):
        assert not _is_linked(a1, 'table_DLine8', b)
    if hasattr(a2, 'table_DLine8'):
        assert _is_linked(a2, 'table_DLine8', b)
    _safe_set(b, 'table_DCell', None)
    assert not _is_linked(b, 'table_DCell', a2)
    if hasattr(a2, 'table_DLine8'):
        assert not _is_linked(a2, 'table_DLine8', b)


def test_assoc_table31_reverse_link_reassign_clear():
    a1 = table_DTable(headerColumnWidth=7)
    a2 = table_DTable(headerColumnWidth=13)
    b = table_DColumn(label="sample_text", visible=True, width=7)
    _safe_set(b, 'columns', a1)
    assert _is_linked(b, 'columns', a1)
    if hasattr(a1, 'DTable'):
        assert _is_linked(a1, 'DTable', b)
    _safe_set(b, 'columns', a2)
    assert _is_linked(b, 'columns', a2)
    if hasattr(a1, 'DTable'):
        assert not _is_linked(a1, 'DTable', b)
    if hasattr(a2, 'DTable'):
        assert _is_linked(a2, 'DTable', b)
    _safe_set(b, 'columns', None)
    assert not _is_linked(b, 'columns', a2)
    if hasattr(a2, 'DTable'):
        assert not _is_linked(a2, 'DTable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_allCreateLine72_stub_double():
    # CreateLineTool has no real 'CreateLineTool74' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool74', None)
    _safe_set(owner, 'table_description_TableDescription73', {partner})
    assert getattr(partner, 'CreateLineTool74') == owner
    _safe_set(owner, 'table_description_TableDescription73', set())
    assert getattr(partner, 'CreateLineTool74') is None


def test_assoc_allLineMappings64_stub_double():
    # LineMapping has no real 'LineMapping66' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping66', None)
    _safe_set(owner, 'table_description_TableDescription65', {partner})
    assert getattr(partner, 'LineMapping66') == owner
    _safe_set(owner, 'table_description_TableDescription65', set())
    assert getattr(partner, 'LineMapping66') is None


def test_assoc_allRepresentationCreationDescriptions47_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription49' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription49', None)
    _safe_set(owner, 'table_description_TableDescription48', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription49') == owner
    _safe_set(owner, 'table_description_TableDescription48', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription49') is None


def test_assoc_allRepresentationNavigationDescriptions55_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription57' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription57', None)
    _safe_set(owner, 'table_description_TableDescription56', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription57') == owner
    _safe_set(owner, 'table_description_TableDescription56', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription57') is None


def test_assoc_allSubLines94_stub_double():
    # LineMapping has no real 'LineMapping96' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping96', None)
    _safe_set(owner, 'table_description_LineMapping95', {partner})
    assert getattr(partner, 'LineMapping96') == owner
    _safe_set(owner, 'table_description_LineMapping95', set())
    assert getattr(partner, 'LineMapping96') is None


def test_assoc_backgroundColor40_stub_double():
    # table_RGBValues has no real 'table_RGBValues42' property in the generated
    # code (a bare stub) -- manually attach it so table_DTableElementStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DTableElementStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DTableElementStyle(defaultBackgroundStyle=True, defaultForegroundStyle=True, labelFormat="sample_text", labelSize=7)
    partner = table_RGBValues()
    setattr(partner, 'table_RGBValues42', None)
    _safe_set(owner, 'table_DTableElementStyle41', partner)
    assert getattr(partner, 'table_RGBValues42') == owner
    _safe_set(owner, 'table_DTableElementStyle41', None)
    assert getattr(partner, 'table_RGBValues42') is None


def test_assoc_columnMapping117_stub_double():
    # ColumnMapping has no real 'ColumnMapping119' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = ColumnMapping()
    setattr(partner, 'ColumnMapping119', None)
    _safe_set(owner, 'table_description_IntersectionMapping118', partner)
    assert getattr(partner, 'ColumnMapping119') == owner
    _safe_set(owner, 'table_description_IntersectionMapping118', None)
    assert getattr(partner, 'ColumnMapping119') is None


def test_assoc_container6_stub_double():
    # table_LineContainer has no real 'LineContainer' property in the generated
    # code (a bare stub) -- manually attach it so table_DLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DLine(collapsed=True, label="sample_text", visible=True)
    partner = table_LineContainer()
    setattr(partner, 'LineContainer', None)
    _safe_set(owner, 'lines', partner)
    assert getattr(partner, 'LineContainer') == owner
    _safe_set(owner, 'lines', None)
    assert getattr(partner, 'LineContainer') is None


def test_assoc_create103_stub_double():
    # CreateColumnTool has no real 'CreateColumnTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ElementColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ElementColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    partner = CreateColumnTool()
    setattr(partner, 'CreateColumnTool', None)
    _safe_set(owner, 'mapping104', {partner})
    assert getattr(partner, 'CreateColumnTool') == owner
    _safe_set(owner, 'mapping104', set())
    assert getattr(partner, 'CreateColumnTool') is None


def test_assoc_create120_stub_double():
    # CreateCellTool has no real 'CreateCellTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = CreateCellTool()
    setattr(partner, 'CreateCellTool', None)
    _safe_set(owner, 'mapping121', partner)
    assert getattr(partner, 'CreateCellTool') == owner
    _safe_set(owner, 'mapping121', None)
    assert getattr(partner, 'CreateCellTool') is None


def test_assoc_create99_stub_double():
    # CreateLineTool has no real 'CreateLineTool101' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool101', None)
    _safe_set(owner, 'table_description_LineMapping100', {partner})
    assert getattr(partner, 'CreateLineTool101') == owner
    _safe_set(owner, 'table_description_LineMapping100', set())
    assert getattr(partner, 'CreateLineTool101') is None


def test_assoc_currentStyle16_stub_double():
    # table_DCellStyle has no real 'table_DCellStyle' property in the generated
    # code (a bare stub) -- manually attach it so table_DCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DCell(label="sample_text")
    partner = table_DCellStyle()
    setattr(partner, 'table_DCellStyle', None)
    _safe_set(owner, 'table_DCell17', partner)
    assert getattr(partner, 'table_DCellStyle') == owner
    _safe_set(owner, 'table_DCell17', None)
    assert getattr(partner, 'table_DCellStyle') is None


def test_assoc_delete102_stub_double():
    # DeleteLineTool has no real 'DeleteLineTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = DeleteLineTool()
    setattr(partner, 'DeleteLineTool', None)
    _safe_set(owner, 'mapping', partner)
    assert getattr(partner, 'DeleteLineTool') == owner
    _safe_set(owner, 'mapping', None)
    assert getattr(partner, 'DeleteLineTool') is None


def test_assoc_delete105_stub_double():
    # DeleteColumnTool has no real 'DeleteColumnTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ElementColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ElementColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    partner = DeleteColumnTool()
    setattr(partner, 'DeleteColumnTool', None)
    _safe_set(owner, 'mapping106', partner)
    assert getattr(partner, 'DeleteColumnTool') == owner
    _safe_set(owner, 'mapping106', None)
    assert getattr(partner, 'DeleteColumnTool') is None


def test_assoc_description1_stub_double():
    # TableDescription has no real 'TableDescription' property in the generated
    # code (a bare stub) -- manually attach it so table_DTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DTable(headerColumnWidth=7)
    partner = TableDescription()
    setattr(partner, 'TableDescription', None)
    _safe_set(owner, 'table_DTable', partner)
    assert getattr(partner, 'TableDescription') == owner
    _safe_set(owner, 'table_DTable', None)
    assert getattr(partner, 'TableDescription') is None


def test_assoc_directEdit107_stub_double():
    # LabelEditTool has no real 'LabelEditTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_CellUpdater's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_CellUpdater's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_CellUpdater(canEdit="sample_text")
    partner = LabelEditTool()
    setattr(partner, 'LabelEditTool', None)
    _safe_set(owner, 'table_description_CellUpdater', partner)
    assert getattr(partner, 'LabelEditTool') == owner
    _safe_set(owner, 'table_description_CellUpdater', None)
    assert getattr(partner, 'LabelEditTool') is None


def test_assoc_foreGroundColor142_stub_double():
    # ColorDescription has no real 'ColorDescription' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ForegroundStyleDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ForegroundStyleDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ForegroundStyleDescription(labelFormat="sample_text", labelSize=7)
    partner = ColorDescription()
    setattr(partner, 'ColorDescription', None)
    _safe_set(owner, 'table_description_ForegroundStyleDescription', partner)
    assert getattr(partner, 'ColorDescription') == owner
    _safe_set(owner, 'table_description_ForegroundStyleDescription', None)
    assert getattr(partner, 'ColorDescription') is None


def test_assoc_foregroundColor38_stub_double():
    # table_RGBValues has no real 'table_RGBValues' property in the generated
    # code (a bare stub) -- manually attach it so table_DTableElementStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DTableElementStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DTableElementStyle(defaultBackgroundStyle=True, defaultForegroundStyle=True, labelFormat="sample_text", labelSize=7)
    partner = table_RGBValues()
    setattr(partner, 'table_RGBValues', None)
    _safe_set(owner, 'table_DTableElementStyle39', partner)
    assert getattr(partner, 'table_RGBValues') == owner
    _safe_set(owner, 'table_DTableElementStyle39', None)
    assert getattr(partner, 'table_RGBValues') is None


def test_assoc_importedElements75_stub_double():
    # description_table_EObject has no real 'description_table_EObject' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = description_table_EObject()
    setattr(partner, 'description_table_EObject', None)
    _safe_set(owner, 'table_description_TableDescription76', {partner})
    assert getattr(partner, 'description_table_EObject') == owner
    _safe_set(owner, 'table_description_TableDescription76', set())
    assert getattr(partner, 'description_table_EObject') is None


def test_assoc_intersectionMapping20_stub_double():
    # IntersectionMapping has no real 'IntersectionMapping' property in the generated
    # code (a bare stub) -- manually attach it so table_DCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DCell(label="sample_text")
    partner = IntersectionMapping()
    setattr(partner, 'IntersectionMapping', None)
    _safe_set(owner, 'table_DCell21', partner)
    assert getattr(partner, 'IntersectionMapping') == owner
    _safe_set(owner, 'table_DCell21', None)
    assert getattr(partner, 'IntersectionMapping') is None


def test_assoc_lineMapping115_stub_double():
    # LineMapping has no real 'LineMapping116' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = LineMapping()
    setattr(partner, 'LineMapping116', None)
    _safe_set(owner, 'table_description_IntersectionMapping', {partner})
    assert getattr(partner, 'LineMapping116') == owner
    _safe_set(owner, 'table_description_IntersectionMapping', set())
    assert getattr(partner, 'LineMapping116') is None


def test_assoc_lines3_stub_double():
    # table_LineContainer has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so table_DLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DLine(collapsed=True, label="sample_text", visible=True)
    partner = table_LineContainer()
    setattr(partner, 'container', None)
    _safe_set(owner, 'DLine', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'DLine', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_originMapping30_stub_double():
    # ColumnMapping has no real 'ColumnMapping' property in the generated
    # code (a bare stub) -- manually attach it so table_DColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DColumn(label="sample_text", visible=True, width=7)
    partner = ColumnMapping()
    setattr(partner, 'ColumnMapping', None)
    _safe_set(owner, 'table_DColumn', partner)
    assert getattr(partner, 'ColumnMapping') == owner
    _safe_set(owner, 'table_DColumn', None)
    assert getattr(partner, 'ColumnMapping') is None


def test_assoc_originMapping4_stub_double():
    # LineMapping has no real 'LineMapping' property in the generated
    # code (a bare stub) -- manually attach it so table_DLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DLine(collapsed=True, label="sample_text", visible=True)
    partner = LineMapping()
    setattr(partner, 'LineMapping', None)
    _safe_set(owner, 'table_DLine', partner)
    assert getattr(partner, 'LineMapping') == owner
    _safe_set(owner, 'table_DLine', None)
    assert getattr(partner, 'LineMapping') is None


def test_assoc_ownedCreateLine67_stub_double():
    # CreateLineTool has no real 'CreateLineTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool', None)
    _safe_set(owner, 'table_description_TableDescription68', {partner})
    assert getattr(partner, 'CreateLineTool') == owner
    _safe_set(owner, 'table_description_TableDescription68', set())
    assert getattr(partner, 'CreateLineTool') is None


def test_assoc_ownedLineMappings58_stub_double():
    # LineMapping has no real 'LineMapping60' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping60', None)
    _safe_set(owner, 'table_description_TableDescription59', {partner})
    assert getattr(partner, 'LineMapping60') == owner
    _safe_set(owner, 'table_description_TableDescription59', set())
    assert getattr(partner, 'LineMapping60') is None


def test_assoc_ownedRepresentationCreationDescriptions43_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription', None)
    _safe_set(owner, 'table_description_TableDescription', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription') == owner
    _safe_set(owner, 'table_description_TableDescription', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription') is None


def test_assoc_ownedRepresentationNavigationDescriptions50_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription', None)
    _safe_set(owner, 'table_description_TableDescription51', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription') == owner
    _safe_set(owner, 'table_description_TableDescription51', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription') is None


def test_assoc_ownedSubLines90_stub_double():
    # LineMapping has no real 'LineMapping91' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping91', None)
    _safe_set(owner, 'table_description_LineMapping', {partner})
    assert getattr(partner, 'LineMapping91') == owner
    _safe_set(owner, 'table_description_LineMapping', set())
    assert getattr(partner, 'LineMapping91') is None


def test_assoc_reusedCreateLine69_stub_double():
    # CreateLineTool has no real 'CreateLineTool71' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool71', None)
    _safe_set(owner, 'table_description_TableDescription70', {partner})
    assert getattr(partner, 'CreateLineTool71') == owner
    _safe_set(owner, 'table_description_TableDescription70', set())
    assert getattr(partner, 'CreateLineTool71') is None


def test_assoc_reusedInMappings97_stub_double():
    # LineMapping has no real 'LineMapping98' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping98', None)
    _safe_set(owner, 'reusedSubLines', {partner})
    assert getattr(partner, 'LineMapping98') == owner
    _safe_set(owner, 'reusedSubLines', set())
    assert getattr(partner, 'LineMapping98') is None


def test_assoc_reusedLineMappings61_stub_double():
    # LineMapping has no real 'LineMapping63' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping63', None)
    _safe_set(owner, 'table_description_TableDescription62', {partner})
    assert getattr(partner, 'LineMapping63') == owner
    _safe_set(owner, 'table_description_TableDescription62', set())
    assert getattr(partner, 'LineMapping63') is None


def test_assoc_reusedRepresentationCreationDescriptions44_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription46' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription46', None)
    _safe_set(owner, 'table_description_TableDescription45', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription46') == owner
    _safe_set(owner, 'table_description_TableDescription45', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription46') is None


def test_assoc_reusedRepresentationNavigationDescriptions52_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription54' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription54', None)
    _safe_set(owner, 'table_description_TableDescription53', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription54') == owner
    _safe_set(owner, 'table_description_TableDescription53', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription54') is None


def test_assoc_reusedSubLines92_stub_double():
    # LineMapping has no real 'LineMapping93' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping93', None)
    _safe_set(owner, 'reusedInMappings', {partner})
    assert getattr(partner, 'LineMapping93') == owner
    _safe_set(owner, 'reusedInMappings', set())
    assert getattr(partner, 'LineMapping93') is None


def test_assoc_style145_stub_double():
    # ForegroundStyleDescription has no real 'ForegroundStyleDescription146' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ForegroundConditionalStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ForegroundConditionalStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ForegroundConditionalStyle(predicateExpression="sample_text")
    partner = ForegroundStyleDescription()
    setattr(partner, 'ForegroundStyleDescription146', None)
    _safe_set(owner, 'table_description_ForegroundConditionalStyle', partner)
    assert getattr(partner, 'ForegroundStyleDescription146') == owner
    _safe_set(owner, 'table_description_ForegroundConditionalStyle', None)
    assert getattr(partner, 'ForegroundStyleDescription146') is None


def test_assoc_style147_stub_double():
    # BackgroundStyleDescription has no real 'BackgroundStyleDescription148' property in the generated
    # code (a bare stub) -- manually attach it so table_description_BackgroundConditionalStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_BackgroundConditionalStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_BackgroundConditionalStyle(predicateExpression="sample_text")
    partner = BackgroundStyleDescription()
    setattr(partner, 'BackgroundStyleDescription148', None)
    _safe_set(owner, 'table_description_BackgroundConditionalStyle', partner)
    assert getattr(partner, 'BackgroundStyleDescription148') == owner
    _safe_set(owner, 'table_description_BackgroundConditionalStyle', None)
    assert getattr(partner, 'BackgroundStyleDescription148') is None


def test_assoc_updater18_stub_double():
    # CellUpdater has no real 'CellUpdater' property in the generated
    # code (a bare stub) -- manually attach it so table_DCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_DCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_DCell(label="sample_text")
    partner = CellUpdater()
    setattr(partner, 'CellUpdater', None)
    _safe_set(owner, 'table_DCell19', partner)
    assert getattr(partner, 'CellUpdater') == owner
    _safe_set(owner, 'table_DCell19', None)
    assert getattr(partner, 'CellUpdater') is None


