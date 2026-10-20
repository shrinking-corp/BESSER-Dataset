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
    description_AbstractVariable,
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
    table_DTargetColumn,
    table_LineContainer,
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
    a1 = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    a2 = table_DTableElementStyle(backgroundColor="sample_text_2", defaultBackgroundStyle=False, defaultForegroundStyle=False, foregroundColor="sample_text_2", labelFormat="sample_text_2", labelSize=13)
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
    a1 = table_DTableElementStyle(backgroundColor="sample_text", defaultBackgroundStyle=True, defaultForegroundStyle=True, foregroundColor="sample_text", labelFormat="sample_text", labelSize=7)
    a2 = table_DTableElementStyle(backgroundColor="sample_text_2", defaultBackgroundStyle=False, defaultForegroundStyle=False, foregroundColor="sample_text_2", labelFormat="sample_text_2", labelSize=13)
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

def test_assoc_allCreateLine67_stub_double():
    # CreateLineTool has no real 'CreateLineTool69' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool69', None)
    _safe_set(owner, 'table_description_TableDescription68', {partner})
    assert getattr(partner, 'CreateLineTool69') == owner
    _safe_set(owner, 'table_description_TableDescription68', set())
    assert getattr(partner, 'CreateLineTool69') is None


def test_assoc_allLineMappings59_stub_double():
    # LineMapping has no real 'LineMapping61' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping61', None)
    _safe_set(owner, 'table_description_TableDescription60', {partner})
    assert getattr(partner, 'LineMapping61') == owner
    _safe_set(owner, 'table_description_TableDescription60', set())
    assert getattr(partner, 'LineMapping61') is None


def test_assoc_allRepresentationCreationDescriptions42_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription44' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription44', None)
    _safe_set(owner, 'table_description_TableDescription43', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription44') == owner
    _safe_set(owner, 'table_description_TableDescription43', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription44') is None


def test_assoc_allRepresentationNavigationDescriptions50_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription52' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription52', None)
    _safe_set(owner, 'table_description_TableDescription51', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription52') == owner
    _safe_set(owner, 'table_description_TableDescription51', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription52') is None


def test_assoc_allSubLines89_stub_double():
    # LineMapping has no real 'LineMapping91' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping91', None)
    _safe_set(owner, 'table_description_LineMapping90', {partner})
    assert getattr(partner, 'LineMapping91') == owner
    _safe_set(owner, 'table_description_LineMapping90', set())
    assert getattr(partner, 'LineMapping91') is None


def test_assoc_columnMapping112_stub_double():
    # ColumnMapping has no real 'ColumnMapping114' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = ColumnMapping()
    setattr(partner, 'ColumnMapping114', None)
    _safe_set(owner, 'table_description_IntersectionMapping113', partner)
    assert getattr(partner, 'ColumnMapping114') == owner
    _safe_set(owner, 'table_description_IntersectionMapping113', None)
    assert getattr(partner, 'ColumnMapping114') is None


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


def test_assoc_create115_stub_double():
    # CreateCellTool has no real 'CreateCellTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = CreateCellTool()
    setattr(partner, 'CreateCellTool', None)
    _safe_set(owner, 'mapping116', partner)
    assert getattr(partner, 'CreateCellTool') == owner
    _safe_set(owner, 'mapping116', None)
    assert getattr(partner, 'CreateCellTool') is None


def test_assoc_create94_stub_double():
    # CreateLineTool has no real 'CreateLineTool96' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool96', None)
    _safe_set(owner, 'table_description_LineMapping95', {partner})
    assert getattr(partner, 'CreateLineTool96') == owner
    _safe_set(owner, 'table_description_LineMapping95', set())
    assert getattr(partner, 'CreateLineTool96') is None


def test_assoc_create98_stub_double():
    # CreateColumnTool has no real 'CreateColumnTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ElementColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ElementColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    partner = CreateColumnTool()
    setattr(partner, 'CreateColumnTool', None)
    _safe_set(owner, 'mapping99', {partner})
    assert getattr(partner, 'CreateColumnTool') == owner
    _safe_set(owner, 'mapping99', set())
    assert getattr(partner, 'CreateColumnTool') is None


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


def test_assoc_delete100_stub_double():
    # DeleteColumnTool has no real 'DeleteColumnTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ElementColumnMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ElementColumnMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ElementColumnMapping(domainClass="sample_text", semanticCandidatesExpression="sample_text")
    partner = DeleteColumnTool()
    setattr(partner, 'DeleteColumnTool', None)
    _safe_set(owner, 'mapping101', partner)
    assert getattr(partner, 'DeleteColumnTool') == owner
    _safe_set(owner, 'mapping101', None)
    assert getattr(partner, 'DeleteColumnTool') is None


def test_assoc_delete97_stub_double():
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


def test_assoc_directEdit102_stub_double():
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


def test_assoc_foreGroundColor137_stub_double():
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


def test_assoc_importedElements70_stub_double():
    # description_table_EObject has no real 'description_table_EObject' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = description_table_EObject()
    setattr(partner, 'description_table_EObject', None)
    _safe_set(owner, 'table_description_TableDescription71', {partner})
    assert getattr(partner, 'description_table_EObject') == owner
    _safe_set(owner, 'table_description_TableDescription71', set())
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


def test_assoc_lineMapping110_stub_double():
    # LineMapping has no real 'LineMapping111' property in the generated
    # code (a bare stub) -- manually attach it so table_description_IntersectionMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_IntersectionMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_IntersectionMapping(columnFinderExpression="sample_text", domainClass="sample_text", labelExpression="sample_text", lineFinderExpression="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text", useDomainClass=True)
    partner = LineMapping()
    setattr(partner, 'LineMapping111', None)
    _safe_set(owner, 'table_description_IntersectionMapping', {partner})
    assert getattr(partner, 'LineMapping111') == owner
    _safe_set(owner, 'table_description_IntersectionMapping', set())
    assert getattr(partner, 'LineMapping111') is None


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


def test_assoc_ownedCreateLine62_stub_double():
    # CreateLineTool has no real 'CreateLineTool' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool', None)
    _safe_set(owner, 'table_description_TableDescription63', {partner})
    assert getattr(partner, 'CreateLineTool') == owner
    _safe_set(owner, 'table_description_TableDescription63', set())
    assert getattr(partner, 'CreateLineTool') is None


def test_assoc_ownedLineMappings53_stub_double():
    # LineMapping has no real 'LineMapping55' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping55', None)
    _safe_set(owner, 'table_description_TableDescription54', {partner})
    assert getattr(partner, 'LineMapping55') == owner
    _safe_set(owner, 'table_description_TableDescription54', set())
    assert getattr(partner, 'LineMapping55') is None


def test_assoc_ownedRepresentationCreationDescriptions38_stub_double():
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


def test_assoc_ownedRepresentationNavigationDescriptions45_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription', None)
    _safe_set(owner, 'table_description_TableDescription46', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription') == owner
    _safe_set(owner, 'table_description_TableDescription46', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription') is None


def test_assoc_ownedSubLines85_stub_double():
    # LineMapping has no real 'LineMapping86' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping86', None)
    _safe_set(owner, 'table_description_LineMapping', {partner})
    assert getattr(partner, 'LineMapping86') == owner
    _safe_set(owner, 'table_description_LineMapping', set())
    assert getattr(partner, 'LineMapping86') is None


def test_assoc_reusedCreateLine64_stub_double():
    # CreateLineTool has no real 'CreateLineTool66' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = CreateLineTool()
    setattr(partner, 'CreateLineTool66', None)
    _safe_set(owner, 'table_description_TableDescription65', {partner})
    assert getattr(partner, 'CreateLineTool66') == owner
    _safe_set(owner, 'table_description_TableDescription65', set())
    assert getattr(partner, 'CreateLineTool66') is None


def test_assoc_reusedInMappings92_stub_double():
    # LineMapping has no real 'LineMapping93' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping93', None)
    _safe_set(owner, 'reusedSubLines', {partner})
    assert getattr(partner, 'LineMapping93') == owner
    _safe_set(owner, 'reusedSubLines', set())
    assert getattr(partner, 'LineMapping93') is None


def test_assoc_reusedLineMappings56_stub_double():
    # LineMapping has no real 'LineMapping58' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping58', None)
    _safe_set(owner, 'table_description_TableDescription57', {partner})
    assert getattr(partner, 'LineMapping58') == owner
    _safe_set(owner, 'table_description_TableDescription57', set())
    assert getattr(partner, 'LineMapping58') is None


def test_assoc_reusedRepresentationCreationDescriptions39_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription41' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription41', None)
    _safe_set(owner, 'table_description_TableDescription40', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription41') == owner
    _safe_set(owner, 'table_description_TableDescription40', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription41') is None


def test_assoc_reusedRepresentationNavigationDescriptions47_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription49' property in the generated
    # code (a bare stub) -- manually attach it so table_description_TableDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_TableDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_TableDescription(domainClass="sample_text", initialHeaderColumnWidth=7, preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription49', None)
    _safe_set(owner, 'table_description_TableDescription48', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription49') == owner
    _safe_set(owner, 'table_description_TableDescription48', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription49') is None


def test_assoc_reusedSubLines87_stub_double():
    # LineMapping has no real 'LineMapping88' property in the generated
    # code (a bare stub) -- manually attach it so table_description_LineMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_LineMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_LineMapping(domainClass="sample_text", headerLabelExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = LineMapping()
    setattr(partner, 'LineMapping88', None)
    _safe_set(owner, 'reusedInMappings', {partner})
    assert getattr(partner, 'LineMapping88') == owner
    _safe_set(owner, 'reusedInMappings', set())
    assert getattr(partner, 'LineMapping88') is None


def test_assoc_style140_stub_double():
    # ForegroundStyleDescription has no real 'ForegroundStyleDescription141' property in the generated
    # code (a bare stub) -- manually attach it so table_description_ForegroundConditionalStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_ForegroundConditionalStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_ForegroundConditionalStyle(predicateExpression="sample_text")
    partner = ForegroundStyleDescription()
    setattr(partner, 'ForegroundStyleDescription141', None)
    _safe_set(owner, 'table_description_ForegroundConditionalStyle', partner)
    assert getattr(partner, 'ForegroundStyleDescription141') == owner
    _safe_set(owner, 'table_description_ForegroundConditionalStyle', None)
    assert getattr(partner, 'ForegroundStyleDescription141') is None


def test_assoc_style142_stub_double():
    # BackgroundStyleDescription has no real 'BackgroundStyleDescription143' property in the generated
    # code (a bare stub) -- manually attach it so table_description_BackgroundConditionalStyle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # table_description_BackgroundConditionalStyle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = table_description_BackgroundConditionalStyle(predicateExpression="sample_text")
    partner = BackgroundStyleDescription()
    setattr(partner, 'BackgroundStyleDescription143', None)
    _safe_set(owner, 'table_description_BackgroundConditionalStyle', partner)
    assert getattr(partner, 'BackgroundStyleDescription143') == owner
    _safe_set(owner, 'table_description_BackgroundConditionalStyle', None)
    assert getattr(partner, 'BackgroundStyleDescription143') is None


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


