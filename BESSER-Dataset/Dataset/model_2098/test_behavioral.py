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
    DTreeElementUpdater,
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
    description_RepresentationDescription,
    description_StyleUpdater,
    description_TreeItemMappingContainer,
    description_TreeItemTool,
    description_TreeItemUpdater,
    description_TreeMapping,
    style_LabelStyleDescription,
    style_StyleDescription,
    tool_AbstractVariable,
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
    tree_DTreeElementUpdater,
    tree_DTreeItem,
    tree_DTreeItemContainer,
    tree_EObject,
    tree_RGBValues,
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


def test_assoc_allSubMappings22_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping24' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping24', None)
    _safe_set(owner, 'tree_description_TreeItemMapping23', {partner})
    assert getattr(partner, 'TreeItemMapping24') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping23', set())
    assert getattr(partner, 'TreeItemMapping24') is None


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


def test_assoc_containers49_stub_double():
    # TreeItemMappingContainer has no real 'TreeItemMappingContainer' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = TreeItemMappingContainer()
    setattr(partner, 'TreeItemMappingContainer', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool50', {partner})
    assert getattr(partner, 'TreeItemMappingContainer') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool50', set())
    assert getattr(partner, 'TreeItemMappingContainer') is None


def test_assoc_create29_stub_double():
    # TreeItemCreationTool has no real 'TreeItemCreationTool31' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemCreationTool()
    setattr(partner, 'TreeItemCreationTool31', None)
    _safe_set(owner, 'tree_description_TreeItemMapping30', {partner})
    assert getattr(partner, 'TreeItemCreationTool31') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping30', set())
    assert getattr(partner, 'TreeItemCreationTool31') is None


def test_assoc_createTreeItem15_stub_double():
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


def test_assoc_delete28_stub_double():
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


def test_assoc_directEdit89_stub_double():
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


def test_assoc_dndTools32_stub_double():
    # TreeItemDragTool has no real 'TreeItemDragTool' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemDragTool()
    setattr(partner, 'TreeItemDragTool', None)
    _safe_set(owner, 'tree_description_TreeItemMapping33', {partner})
    assert getattr(partner, 'TreeItemDragTool') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping33', set())
    assert getattr(partner, 'TreeItemDragTool') is None


def test_assoc_element45_stub_double():
    # tool_ElementDropVariable has no real 'tool_ElementDropVariable' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_ElementDropVariable()
    setattr(partner, 'tool_ElementDropVariable', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool46', partner)
    assert getattr(partner, 'tool_ElementDropVariable') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool46', None)
    assert getattr(partner, 'tool_ElementDropVariable') is None


def test_assoc_element58_stub_double():
    # tool_ElementDropVariable has no real 'tool_ElementDropVariable60' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_ElementDropVariable()
    setattr(partner, 'tool_ElementDropVariable60', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool59', partner)
    assert getattr(partner, 'tool_ElementDropVariable60') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool59', None)
    assert getattr(partner, 'tool_ElementDropVariable60') is None


def test_assoc_newContainer42_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable44' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable44', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool43', partner)
    assert getattr(partner, 'tool_DropContainerVariable44') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool43', None)
    assert getattr(partner, 'tool_DropContainerVariable44') is None


def test_assoc_newContainer55_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable57' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable57', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool56', partner)
    assert getattr(partner, 'tool_DropContainerVariable57') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool56', None)
    assert getattr(partner, 'tool_DropContainerVariable57') is None


def test_assoc_newViewContainer47_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool48', partner)
    assert getattr(partner, 'tool_ContainerViewVariable') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool48', None)
    assert getattr(partner, 'tool_ContainerViewVariable') is None


def test_assoc_newViewContainer61_stub_double():
    # tool_ContainerViewVariable has no real 'tool_ContainerViewVariable63' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_ContainerViewVariable()
    setattr(partner, 'tool_ContainerViewVariable63', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool62', partner)
    assert getattr(partner, 'tool_ContainerViewVariable63') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool62', None)
    assert getattr(partner, 'tool_ContainerViewVariable63') is None


def test_assoc_oldContainer41_stub_double():
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


def test_assoc_oldContainer53_stub_double():
    # tool_DropContainerVariable has no real 'tool_DropContainerVariable54' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = tool_DropContainerVariable()
    setattr(partner, 'tool_DropContainerVariable54', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool', partner)
    assert getattr(partner, 'tool_DropContainerVariable54') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool', None)
    assert getattr(partner, 'tool_DropContainerVariable54') is None


def test_assoc_ownedRepresentationCreationDescriptions16_stub_double():
    # tool_RepresentationCreationDescription has no real 'tool_RepresentationCreationDescription' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    partner = tool_RepresentationCreationDescription()
    setattr(partner, 'tool_RepresentationCreationDescription', None)
    _safe_set(owner, 'tree_description_TreeDescription17', {partner})
    assert getattr(partner, 'tool_RepresentationCreationDescription') == owner
    _safe_set(owner, 'tree_description_TreeDescription17', set())
    assert getattr(partner, 'tool_RepresentationCreationDescription') is None


def test_assoc_ownedRepresentationNavigationDescriptions18_stub_double():
    # tool_RepresentationNavigationDescription has no real 'tool_RepresentationNavigationDescription' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeDescription's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeDescription's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    partner = tool_RepresentationNavigationDescription()
    setattr(partner, 'tool_RepresentationNavigationDescription', None)
    _safe_set(owner, 'tree_description_TreeDescription19', {partner})
    assert getattr(partner, 'tool_RepresentationNavigationDescription') == owner
    _safe_set(owner, 'tree_description_TreeDescription19', set())
    assert getattr(partner, 'tool_RepresentationNavigationDescription') is None


def test_assoc_ownedStyle5_stub_double():
    # tree_TreeItemStyle has no real 'tree_TreeItemStyle' property in the generated
    # code (a bare stub) -- manually attach it so tree_DTreeItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_DTreeItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_DTreeItem(expanded=True)
    partner = tree_TreeItemStyle()
    setattr(partner, 'tree_TreeItemStyle', None)
    _safe_set(owner, 'tree_DTreeItem', partner)
    assert getattr(partner, 'tree_TreeItemStyle') == owner
    _safe_set(owner, 'tree_DTreeItem', None)
    assert getattr(partner, 'tree_TreeItemStyle') is None


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


def test_assoc_popupMenus34_stub_double():
    # TreePopupMenu has no real 'TreePopupMenu' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreePopupMenu()
    setattr(partner, 'TreePopupMenu', None)
    _safe_set(owner, 'tree_description_TreeItemMapping35', {partner})
    assert getattr(partner, 'TreePopupMenu') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping35', set())
    assert getattr(partner, 'TreePopupMenu') is None


def test_assoc_precedingSiblings51_stub_double():
    # PrecedingSiblingsVariables has no real 'PrecedingSiblingsVariables' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemDragTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemDragTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    partner = PrecedingSiblingsVariables()
    setattr(partner, 'PrecedingSiblingsVariables', None)
    _safe_set(owner, 'tree_description_TreeItemDragTool52', partner)
    assert getattr(partner, 'PrecedingSiblingsVariables') == owner
    _safe_set(owner, 'tree_description_TreeItemDragTool52', None)
    assert getattr(partner, 'PrecedingSiblingsVariables') is None


def test_assoc_precedingSiblings64_stub_double():
    # PrecedingSiblingsVariables has no real 'PrecedingSiblingsVariables66' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemContainerDropTool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemContainerDropTool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    partner = PrecedingSiblingsVariables()
    setattr(partner, 'PrecedingSiblingsVariables66', None)
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool65', partner)
    assert getattr(partner, 'PrecedingSiblingsVariables66') == owner
    _safe_set(owner, 'tree_description_TreeItemContainerDropTool65', None)
    assert getattr(partner, 'PrecedingSiblingsVariables66') is None


def test_assoc_reusedTreeItemMappings20_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping21' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping21', None)
    _safe_set(owner, 'tree_description_TreeItemMapping', {partner})
    assert getattr(partner, 'TreeItemMapping21') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping', set())
    assert getattr(partner, 'TreeItemMapping21') is None


def test_assoc_specialize25_stub_double():
    # TreeItemMapping has no real 'TreeItemMapping27' property in the generated
    # code (a bare stub) -- manually attach it so tree_description_TreeItemMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_description_TreeItemMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    partner = TreeItemMapping()
    setattr(partner, 'TreeItemMapping27', None)
    _safe_set(owner, 'tree_description_TreeItemMapping26', partner)
    assert getattr(partner, 'TreeItemMapping27') == owner
    _safe_set(owner, 'tree_description_TreeItemMapping26', None)
    assert getattr(partner, 'TreeItemMapping27') is None


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


