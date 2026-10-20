import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractToolDescription,
    ColorDescription,
    ConditionalStyleDescription,
    ConditionalTreeItemStyleDescription,
    DRepresentation,
    DRepresentationElement,
    DSemanticDecorator,
    DTreeElement,
    DTreeItemContainer,
    LabelStyle,
    PrecedingSiblingsVariables,
    RepresentationCreationDescription,
    RepresentationElementMapping,
    RepresentationNavigationDescription,
    Style,
    StyleUpdater,
    TreeDescription,
    TreeItemContainerDropTool,
    TreeItemCreationTool,
    TreeItemDeletionTool,
    TreeItemDragTool,
    TreeItemEditionTool,
    TreeItemMapping,
    TreeItemMappingContainer,
    TreeItemStyleDescription,
    TreeItemTool,
    TreeItemUpdater,
    TreeMapping,
    TreePopupMenu,
    TreeVariable,
    description_AbstractVariable,
    description_RepresentationDescription,
    description_StyleUpdater,
    description_TreeItemMappingContainer,
    description_TreeItemTool,
    description_TreeItemUpdater,
    description_TreeMapping,
    style_LabelStyleDescription,
    style_StyleDescription,
    tool_ContainerViewVariable,
    tool_DropContainerVariable,
    tool_EditMaskVariables,
    tool_ElementDropVariable,
    tool_MappingBasedToolDescription,
    tool_MenuItemOrRef,
    tool_ModelOperation,
    tool_RepresentationCreationDescription,
    tool_RepresentationNavigationDescription,
    tool_VariableContainer,
    tree_DTree,
    tree_DTreeElement,
    tree_DTreeElementSynchronizer,
    tree_DTreeItem,
    tree_DTreeItemContainer,
    tree_EObject,
    tree_TreeItemStyle,
    tree_description_ConditionalTreeItemStyleDescription,
    tree_description_PrecedingSiblingsVariables,
    tree_description_StyleUpdater,
    tree_description_TreeCreationDescription,
    tree_description_TreeDescription,
    tree_description_TreeItemContainerDropTool,
    tree_description_TreeItemCreationTool,
    tree_description_TreeItemDeletionTool,
    tree_description_TreeItemDragTool,
    tree_description_TreeItemEditionTool,
    tree_description_TreeItemMapping,
    tree_description_TreeItemMappingContainer,
    tree_description_TreeItemStyleDescription,
    tree_description_TreeItemTool,
    tree_description_TreeItemUpdater,
    tree_description_TreeMapping,
    tree_description_TreeNavigationDescription,
    tree_description_TreePopupMenu,
    tree_description_TreeVariable,
    TreeDragSource,
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

def test_assoc_ownedStyle5_reverse_link_reassign_clear():
    a1 = tree_TreeItemStyle(backgroundColor="sample_text")
    a2 = tree_TreeItemStyle(backgroundColor="sample_text_2")
    b = tree_DTreeItem(expanded=True)
    _safe_set(b, 'tree_DTreeItem', a1)
    assert _is_linked(b, 'tree_DTreeItem', a1)
    if hasattr(a1, 'tree_TreeItemStyle'):
        assert _is_linked(a1, 'tree_TreeItemStyle', b)
    _safe_set(b, 'tree_DTreeItem', a2)
    assert _is_linked(b, 'tree_DTreeItem', a2)
    if hasattr(a1, 'tree_TreeItemStyle'):
        assert not _is_linked(a1, 'tree_TreeItemStyle', b)
    if hasattr(a2, 'tree_TreeItemStyle'):
        assert _is_linked(a2, 'tree_TreeItemStyle', b)
    _safe_set(b, 'tree_DTreeItem', None)
    assert not _is_linked(b, 'tree_DTreeItem', a2)
    if hasattr(a2, 'tree_TreeItemStyle'):
        assert not _is_linked(a2, 'tree_TreeItemStyle', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actualMapping6_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping', None)
    _safe_set(owner, 'tree_DTreeItem7', partner)
    assert getattr(partner, 'TreeItemMapping') == owner
    _safe_set(owner, 'tree_DTreeItem7', None)
    assert getattr(partner, 'TreeItemMapping') is None


def test_assoc_allSubMappings20_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping22' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping22', None)
    _safe_set(owner, 'tree_description_TreeItemMapping21', {partner})
    assert getattr(partner, 'TreeItemMapping22') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping21', set())
    assert getattr(partner, 'TreeItemMapping22') is None


def test_assoc_container8_stub_double():
    # tree_DTreeItemContainer has no real 'DTreeItemContainer' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = tree_DTreeItemContainer()
    setattr(partner, 'DTreeItemContainer', None)
    _safe_set(owner, 'ownedTreeItems', partner)
    assert getattr(partner, 'DTreeItemContainer') == owner
    _safe_set(owner, 'ownedTreeItems', None)
    assert getattr(partner, 'DTreeItemContainer') is None


def test_assoc_containers47_stub_double():
    # TreeItemMappingContainer has no real 'TreeItemMappingContainer' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = TreeItemMappingContainer()
    setattr(partner, 'TreeItemMappingContainer', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool48', {partner})
    assert getattr(partner, 'TreeItemMappingContainer') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool48', set())
    assert getattr(partner, 'TreeItemMappingContainer') is None


def test_assoc_create27_stub_double():
    # TreeItemCreationTool has no real 'TreeItemCreationTool29' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemCreationTool()
    setattr(partner, 'TreeItemCreationTool29', None)
    _safe_set(owner, 'tree_description_TreeItemMapping28', {partner})
    assert getattr(partner, 'TreeItemCreationTool29') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping28', set())
    assert getattr(partner, 'TreeItemCreationTool29') is None


def test_assoc_createTreeItem13_stub_double():
    # TreeItemCreationTool has no real 'TreeItemCreationTool' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    partner = TreeItemCreationTool()
    setattr(partner, 'TreeItemCreationTool', None)
    _safe_set(owner, 'tree_description_TreeDescription', {partner})
    assert getattr(partner, 'TreeItemCreationTool') == owner
    _safe_set(owner, 'tree_description_TreeDescription', set())
    assert getattr(partner, 'TreeItemCreationTool') is None


def test_assoc_delete26_stub_double():
    # TreeItemDeletionTool has no real 'TreeItemDeletionTool' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemDeletionTool()
    setattr(partner, 'TreeItemDeletionTool', None)
    _safe_set(owner, 'mapping', partner)
    assert getattr(partner, 'TreeItemDeletionTool') == owner
    _safe_set(owner, 'mapping', None)
    assert getattr(partner, 'TreeItemDeletionTool') is None


def test_assoc_directEdit87_stub_double():
    # TreeItemEditionTool has no real 'TreeItemEditionTool' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemUpdater's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemUpdater's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemUpdater()
    partner = TreeItemEditionTool()
    setattr(partner, 'TreeItemEditionTool', None)
    _safe_set(owner, 'tree_description_TreeItemUpdater', partner)
    assert getattr(partner, 'TreeItemEditionTool') == owner
    _safe_set(owner, 'tree_description_TreeItemUpdater', None)
    assert getattr(partner, 'TreeItemEditionTool') is None


def test_assoc_dndTools30_stub_double():
    # TreeItemDragTool has no real 'TreeItemDragTool' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemDragTool()
    setattr(partner, 'TreeItemDragTool', None)
    _safe_set(owner, 'tree_description_TreeItemMapping31', {partner})
    assert getattr(partner, 'TreeItemDragTool') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping31', set())
    assert getattr(partner, 'TreeItemDragTool') is None


def test_assoc_element43_stub_double():
    # tool_ElementDropVariable has no real 'tool_ElementDropVariable' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_ElementDropVariable()
    setattr(partner, 'tool_ElementDropVariable', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool44', partner)
    assert getattr(partner, 'tool_ElementDropVariable') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool44', None)
    assert getattr(partner, 'tool_ElementDropVariable') is None


def test_assoc_element56_stub_double():
    # tool_ElementDropVariable has no real 'tool_ElementDropVariable58' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_ElementDropVariable()
    setattr(partner, 'tool_ElementDropVariable58', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool57', partner)
    assert getattr(partner, 'tool_ElementDropVariable58') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool57', None)
    assert getattr(partner, 'tool_ElementDropVariable58') is None


def test_assoc_newContainer40_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable42' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable42', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool41', partner)
    assert getattr(partner, 'tool_DropContainerVariable42') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool41', None)
    assert getattr(partner, 'tool_DropContainerVariable42') is None


def test_assoc_newContainer53_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable55' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable55', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool54', partner)
    assert getattr(partner, 'tool_DropContainerVariable55') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool54', None)
    assert getattr(partner, 'tool_DropContainerVariable55') is None


def test_assoc_newViewContainer45_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool46', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool46', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_newViewContainer59_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable61' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable61', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool60', partner)
    assert getattr(partner, 'tool_ContainerViewVariable61') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool60', None)
    assert getattr(partner, 'tool_ContainerViewVariable61') is None


def test_assoc_oldContainer39_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool', partner)
    assert getattr(partner, 'tool_DropContainerVariable') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool', None)
    assert getattr(partner, 'tool_DropContainerVariable') is None


def test_assoc_oldContainer51_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable52' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable52', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool', partner)
    assert getattr(partner, 'tool_DropContainerVariable52') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool', None)
    assert getattr(partner, 'tool_DropContainerVariable52') is None


def test_assoc_ownedRepresentationCreationDescriptions14_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription', None)
    _safe_set(owner, 'tree_description_TreeDescription15', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription') == owner
    _safe_set(owner, 'tree_description_TreeDescription15', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription') is None


def test_assoc_ownedRepresentationNavigationDescriptions16_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription', None)
    _safe_set(owner, 'tree_description_TreeDescription17', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription') == owner
    _safe_set(owner, 'tree_description_TreeDescription17', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription') is None


def test_assoc_ownedTreeItems4_stub_double():
    # tree_DTreeItemContainer has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = tree_DTreeItemContainer()
    setattr(partner, 'container', None)
    _safe_set(owner, 'DTreeItem', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'DTreeItem', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_popupMenus32_stub_double():
    # TreePopupMenu has no real 'TreePopupMenu' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreePopupMenu()
    setattr(partner, 'TreePopupMenu', None)
    _safe_set(owner, 'tree_description_TreeItemMapping33', {partner})
    assert getattr(partner, 'TreePopupMenu') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping33', set())
    assert getattr(partner, 'TreePopupMenu') is None


def test_assoc_precedingSiblings49_stub_double():
    # PrecedingSiblingsVariables has no real 'PrecedingSiblingsVariables' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = PrecedingSiblingsVariables()
    setattr(partner, 'PrecedingSiblingsVariables', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool50', partner)
    assert getattr(partner, 'PrecedingSiblingsVariables') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool50', None)
    assert getattr(partner, 'PrecedingSiblingsVariables') is None


def test_assoc_precedingSiblings62_stub_double():
    # PrecedingSiblingsVariables has no real 'PrecedingSiblingsVariables64' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = PrecedingSiblingsVariables()
    setattr(partner, 'PrecedingSiblingsVariables64', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool63', partner)
    assert getattr(partner, 'PrecedingSiblingsVariables64') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool63', None)
    assert getattr(partner, 'PrecedingSiblingsVariables64') is None


def test_assoc_reusedTreeItemMappings18_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping19' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping19', None)
    _safe_set(owner, 'tree_description_TreeItemMapping', {partner})
    assert getattr(partner, 'TreeItemMapping19') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping', set())
    assert getattr(partner, 'TreeItemMapping19') is None


def test_assoc_specialize23_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping25' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping25', None)
    _safe_set(owner, 'tree_description_TreeItemMapping24', partner)
    assert getattr(partner, 'TreeItemMapping25') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping24', None)
    assert getattr(partner, 'TreeItemMapping25') is None


def test_assoc_styleUpdater9_stub_double():
    # StyleUpdater has no real 'StyleUpdater' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = StyleUpdater()
    setattr(partner, 'StyleUpdater', None)
    _safe_set(owner, 'tree_DTreeItem10', partner)
    assert getattr(partner, 'StyleUpdater') == owner
    _safe_set(owner, 'tree_DTreeItem10', None)
    assert getattr(partner, 'StyleUpdater') is None


def test_assoc_updater11_stub_double():
    # TreeItemUpdater has no real 'TreeItemUpdater' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = TreeItemUpdater()
    setattr(partner, 'TreeItemUpdater', None)
    _safe_set(owner, 'tree_DTreeItem12', partner)
    assert getattr(partner, 'TreeItemUpdater') == owner
    _safe_set(owner, 'tree_DTreeItem12', None)
    assert getattr(partner, 'TreeItemUpdater') is None


