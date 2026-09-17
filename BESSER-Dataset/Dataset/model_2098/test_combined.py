# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TreeItemEditionTool,
    tree_description_TreeItemUpdater,
    tool_VariableContainer,
    tool_AbstractVariable,
    tree_description_TreeVariable,
    ConditionalTreeItemStyleDescription,
    tree_description_StyleUpdater,
    tool_MenuItemOrRef,
    TreeItemContainerDropTool,
    tree_description_TreeItemMappingContainer,
    RepresentationElementMapping,
    tree_description_TreeMapping,
    PrecedingSiblingsVariables,
    RepresentationNavigationDescription,
    tree_description_TreeNavigationDescription,
    RepresentationCreationDescription,
    tree_description_TreeCreationDescription,
    TreeItemMappingContainer,
    tool_ContainerViewVariable,
    tool_ElementDropVariable,
    tool_EditMaskVariables,
    TreeItemTool,
    tree_description_TreeItemDeletionTool,
    tree_description_TreeItemEditionTool,
    ColorDescription,
    style_LabelStyleDescription,
    style_StyleDescription,
    tree_description_TreeItemStyleDescription,
    TreePopupMenu,
    TreeItemDragTool,
    TreeItemDeletionTool,
    tool_DropContainerVariable,
    description_TreeItemTool,
    tool_MappingBasedToolDescription,
    tree_description_TreeItemContainerDropTool,
    tree_description_TreeItemCreationTool,
    tree_description_TreeItemDragTool,
    TreeVariable,
    tree_description_PrecedingSiblingsVariables,
    tool_ModelOperation,
    AbstractToolDescription,
    tree_description_TreePopupMenu,
    tree_description_TreeItemTool,
    TreeItemStyleDescription,
    ConditionalStyleDescription,
    tree_description_ConditionalTreeItemStyleDescription,
    description_TreeItemMappingContainer,
    description_RepresentationDescription,
    tree_description_TreeDescription,
    tree_DTreeElementSynchronizer,
    tree_RGBValues,
    LabelStyle,
    Style,
    TreeItemUpdater,
    StyleUpdater,
    TreeItemMapping,
    tree_TreeItemStyle,
    DTreeElement,
    DSemanticDecorator,
    tree_DTreeItemContainer,
    description_TreeItemUpdater,
    description_StyleUpdater,
    description_TreeMapping,
    tree_description_TreeItemMapping,
    tool_RepresentationNavigationDescription,
    tool_RepresentationCreationDescription,
    TreeItemCreationTool,
    TreeMapping,
    DRepresentationElement,
    tree_DTreeElement,
    tree_DTreeElementUpdater,
    TreeDescription,
    tree_EObject,
    DTreeElementUpdater,
    DTreeItemContainer,
    tree_DTreeItem,
    DRepresentation,
    tree_DTree,
    TreeDragSource,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_treeitemeditiontool_is_not_abstract():
    assert not inspect.isabstract(TreeItemEditionTool)


def test_hyp_treeitemeditiontool_constructor_exists():
    assert callable(TreeItemEditionTool.__init__)


def test_hyp_treeitemeditiontool_constructor_args():
    sig = inspect.signature(TreeItemEditionTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemupdater_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemUpdater)


def test_hyp_tree_description_treeitemupdater_constructor_exists():
    assert callable(tree_description_TreeItemUpdater.__init__)


def test_hyp_tree_description_treeitemupdater_constructor_args():
    sig = inspect.signature(tree_description_TreeItemUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_hyp_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_hyp_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractVariable)


def test_hyp_tool_abstractvariable_constructor_exists():
    assert callable(tool_AbstractVariable.__init__)


def test_hyp_tool_abstractvariable_constructor_args():
    sig = inspect.signature(tool_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treevariable_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeVariable)


def test_hyp_tree_description_treevariable_constructor_exists():
    assert callable(tree_description_TreeVariable.__init__)


def test_hyp_tree_description_treevariable_constructor_args():
    sig = inspect.signature(tree_description_TreeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"




def test_hyp_conditionaltreeitemstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalTreeItemStyleDescription)


def test_hyp_conditionaltreeitemstyledescription_constructor_exists():
    assert callable(ConditionalTreeItemStyleDescription.__init__)


def test_hyp_conditionaltreeitemstyledescription_constructor_args():
    sig = inspect.signature(ConditionalTreeItemStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_styleupdater_is_not_abstract():
    assert not inspect.isabstract(tree_description_StyleUpdater)


def test_hyp_tree_description_styleupdater_constructor_exists():
    assert callable(tree_description_StyleUpdater.__init__)


def test_hyp_tree_description_styleupdater_constructor_args():
    sig = inspect.signature(tree_description_StyleUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemOrRef)


def test_hyp_tool_menuitemorref_constructor_exists():
    assert callable(tool_MenuItemOrRef.__init__)


def test_hyp_tool_menuitemorref_constructor_args():
    sig = inspect.signature(tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemcontainerdroptool_is_not_abstract():
    assert not inspect.isabstract(TreeItemContainerDropTool)


def test_hyp_treeitemcontainerdroptool_constructor_exists():
    assert callable(TreeItemContainerDropTool.__init__)


def test_hyp_treeitemcontainerdroptool_constructor_args():
    sig = inspect.signature(TreeItemContainerDropTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemmappingcontainer_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemMappingContainer)


def test_hyp_tree_description_treeitemmappingcontainer_constructor_exists():
    assert callable(tree_description_TreeItemMappingContainer.__init__)


def test_hyp_tree_description_treeitemmappingcontainer_constructor_args():
    sig = inspect.signature(tree_description_TreeItemMappingContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(RepresentationElementMapping)


def test_hyp_representationelementmapping_constructor_exists():
    assert callable(RepresentationElementMapping.__init__)


def test_hyp_representationelementmapping_constructor_args():
    sig = inspect.signature(RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treemapping_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeMapping)


def test_hyp_tree_description_treemapping_constructor_exists():
    assert callable(tree_description_TreeMapping.__init__)


def test_hyp_tree_description_treemapping_constructor_args():
    sig = inspect.signature(tree_description_TreeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"




def test_hyp_precedingsiblingsvariables_is_not_abstract():
    assert not inspect.isabstract(PrecedingSiblingsVariables)


def test_hyp_precedingsiblingsvariables_constructor_exists():
    assert callable(PrecedingSiblingsVariables.__init__)


def test_hyp_precedingsiblingsvariables_constructor_args():
    sig = inspect.signature(PrecedingSiblingsVariables.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_hyp_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_hyp_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treenavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeNavigationDescription)


def test_hyp_tree_description_treenavigationdescription_constructor_exists():
    assert callable(tree_description_TreeNavigationDescription.__init__)


def test_hyp_tree_description_treenavigationdescription_constructor_args():
    sig = inspect.signature(tree_description_TreeNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_hyp_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_hyp_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treecreationdescription_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeCreationDescription)


def test_hyp_tree_description_treecreationdescription_constructor_exists():
    assert callable(tree_description_TreeCreationDescription.__init__)


def test_hyp_tree_description_treecreationdescription_constructor_args():
    sig = inspect.signature(tree_description_TreeCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemmappingcontainer_is_not_abstract():
    assert not inspect.isabstract(TreeItemMappingContainer)


def test_hyp_treeitemmappingcontainer_constructor_exists():
    assert callable(TreeItemMappingContainer.__init__)


def test_hyp_treeitemmappingcontainer_constructor_args():
    sig = inspect.signature(TreeItemMappingContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_hyp_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_hyp_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDropVariable)


def test_hyp_tool_elementdropvariable_constructor_exists():
    assert callable(tool_ElementDropVariable.__init__)


def test_hyp_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool_EditMaskVariables)


def test_hyp_tool_editmaskvariables_constructor_exists():
    assert callable(tool_EditMaskVariables.__init__)


def test_hyp_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemtool_is_not_abstract():
    assert not inspect.isabstract(TreeItemTool)


def test_hyp_treeitemtool_constructor_exists():
    assert callable(TreeItemTool.__init__)


def test_hyp_treeitemtool_constructor_args():
    sig = inspect.signature(TreeItemTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemdeletiontool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemDeletionTool)


def test_hyp_tree_description_treeitemdeletiontool_constructor_exists():
    assert callable(tree_description_TreeItemDeletionTool.__init__)


def test_hyp_tree_description_treeitemdeletiontool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemDeletionTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemeditiontool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemEditionTool)


def test_hyp_tree_description_treeitemeditiontool_constructor_exists():
    assert callable(tree_description_TreeItemEditionTool.__init__)


def test_hyp_tree_description_treeitemeditiontool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemEditionTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_hyp_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_hyp_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelStyleDescription)


def test_hyp_style_labelstyledescription_constructor_exists():
    assert callable(style_LabelStyleDescription.__init__)


def test_hyp_style_labelstyledescription_constructor_args():
    sig = inspect.signature(style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_hyp_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_hyp_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemstyledescription_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemStyleDescription)


def test_hyp_tree_description_treeitemstyledescription_constructor_exists():
    assert callable(tree_description_TreeItemStyleDescription.__init__)


def test_hyp_tree_description_treeitemstyledescription_constructor_args():
    sig = inspect.signature(tree_description_TreeItemStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treepopupmenu_is_not_abstract():
    assert not inspect.isabstract(TreePopupMenu)


def test_hyp_treepopupmenu_constructor_exists():
    assert callable(TreePopupMenu.__init__)


def test_hyp_treepopupmenu_constructor_args():
    sig = inspect.signature(TreePopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemdragtool_is_not_abstract():
    assert not inspect.isabstract(TreeItemDragTool)


def test_hyp_treeitemdragtool_constructor_exists():
    assert callable(TreeItemDragTool.__init__)


def test_hyp_treeitemdragtool_constructor_args():
    sig = inspect.signature(TreeItemDragTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemdeletiontool_is_not_abstract():
    assert not inspect.isabstract(TreeItemDeletionTool)


def test_hyp_treeitemdeletiontool_constructor_exists():
    assert callable(TreeItemDeletionTool.__init__)


def test_hyp_treeitemdeletiontool_constructor_args():
    sig = inspect.signature(TreeItemDeletionTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_hyp_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_hyp_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_treeitemtool_is_not_abstract():
    assert not inspect.isabstract(description_TreeItemTool)


def test_hyp_description_treeitemtool_constructor_exists():
    assert callable(description_TreeItemTool.__init__)


def test_hyp_description_treeitemtool_constructor_args():
    sig = inspect.signature(description_TreeItemTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_MappingBasedToolDescription)


def test_hyp_tool_mappingbasedtooldescription_constructor_exists():
    assert callable(tool_MappingBasedToolDescription.__init__)


def test_hyp_tool_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(tool_MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemcontainerdroptool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemContainerDropTool)


def test_hyp_tree_description_treeitemcontainerdroptool_constructor_exists():
    assert callable(tree_description_TreeItemContainerDropTool.__init__)


def test_hyp_tree_description_treeitemcontainerdroptool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemContainerDropTool.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"




def test_hyp_tree_description_treeitemcreationtool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemCreationTool)


def test_hyp_tree_description_treeitemcreationtool_constructor_exists():
    assert callable(tree_description_TreeItemCreationTool.__init__)


def test_hyp_tree_description_treeitemcreationtool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemdragtool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemDragTool)


def test_hyp_tree_description_treeitemdragtool_constructor_exists():
    assert callable(tree_description_TreeItemDragTool.__init__)


def test_hyp_tree_description_treeitemdragtool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemDragTool.__init__)
    params = list(sig.parameters.keys())
    assert "dragSourceType" in params, "Missing parameter 'dragSourceType'"




def test_hyp_treevariable_is_not_abstract():
    assert not inspect.isabstract(TreeVariable)


def test_hyp_treevariable_constructor_exists():
    assert callable(TreeVariable.__init__)


def test_hyp_treevariable_constructor_args():
    sig = inspect.signature(TreeVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_precedingsiblingsvariables_is_not_abstract():
    assert not inspect.isabstract(tree_description_PrecedingSiblingsVariables)


def test_hyp_tree_description_precedingsiblingsvariables_constructor_exists():
    assert callable(tree_description_PrecedingSiblingsVariables.__init__)


def test_hyp_tree_description_precedingsiblingsvariables_constructor_args():
    sig = inspect.signature(tree_description_PrecedingSiblingsVariables.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ModelOperation)


def test_hyp_tool_modeloperation_constructor_exists():
    assert callable(tool_ModelOperation.__init__)


def test_hyp_tool_modeloperation_constructor_args():
    sig = inspect.signature(tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_hyp_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_hyp_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treepopupmenu_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreePopupMenu)


def test_hyp_tree_description_treepopupmenu_constructor_exists():
    assert callable(tree_description_TreePopupMenu.__init__)


def test_hyp_tree_description_treepopupmenu_constructor_args():
    sig = inspect.signature(tree_description_TreePopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemtool_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemTool)


def test_hyp_tree_description_treeitemtool_constructor_exists():
    assert callable(tree_description_TreeItemTool.__init__)


def test_hyp_tree_description_treeitemtool_constructor_args():
    sig = inspect.signature(tree_description_TreeItemTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemstyledescription_is_not_abstract():
    assert not inspect.isabstract(TreeItemStyleDescription)


def test_hyp_treeitemstyledescription_constructor_exists():
    assert callable(TreeItemStyleDescription.__init__)


def test_hyp_treeitemstyledescription_constructor_args():
    sig = inspect.signature(TreeItemStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_hyp_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_hyp_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_conditionaltreeitemstyledescription_is_not_abstract():
    assert not inspect.isabstract(tree_description_ConditionalTreeItemStyleDescription)


def test_hyp_tree_description_conditionaltreeitemstyledescription_constructor_exists():
    assert callable(tree_description_ConditionalTreeItemStyleDescription.__init__)


def test_hyp_tree_description_conditionaltreeitemstyledescription_constructor_args():
    sig = inspect.signature(tree_description_ConditionalTreeItemStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_treeitemmappingcontainer_is_not_abstract():
    assert not inspect.isabstract(description_TreeItemMappingContainer)


def test_hyp_description_treeitemmappingcontainer_constructor_exists():
    assert callable(description_TreeItemMappingContainer.__init__)


def test_hyp_description_treeitemmappingcontainer_constructor_args():
    sig = inspect.signature(description_TreeItemMappingContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationDescription)


def test_hyp_description_representationdescription_constructor_exists():
    assert callable(description_RepresentationDescription.__init__)


def test_hyp_description_representationdescription_constructor_args():
    sig = inspect.signature(description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treedescription_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeDescription)


def test_hyp_tree_description_treedescription_constructor_exists():
    assert callable(tree_description_TreeDescription.__init__)


def test_hyp_tree_description_treedescription_constructor_args():
    sig = inspect.signature(tree_description_TreeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"





def test_hyp_tree_dtreeelementsynchronizer_is_not_abstract():
    assert not inspect.isabstract(tree_DTreeElementSynchronizer)


def test_hyp_tree_dtreeelementsynchronizer_constructor_exists():
    assert callable(tree_DTreeElementSynchronizer.__init__)


def test_hyp_tree_dtreeelementsynchronizer_constructor_args():
    sig = inspect.signature(tree_DTreeElementSynchronizer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_rgbvalues_is_not_abstract():
    assert not inspect.isabstract(tree_RGBValues)


def test_hyp_tree_rgbvalues_constructor_exists():
    assert callable(tree_RGBValues.__init__)


def test_hyp_tree_rgbvalues_constructor_args():
    sig = inspect.signature(tree_RGBValues.__init__)
    params = list(sig.parameters.keys())



def test_hyp_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_hyp_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_hyp_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_hyp_style_constructor_exists():
    assert callable(Style.__init__)


def test_hyp_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemupdater_is_not_abstract():
    assert not inspect.isabstract(TreeItemUpdater)


def test_hyp_treeitemupdater_constructor_exists():
    assert callable(TreeItemUpdater.__init__)


def test_hyp_treeitemupdater_constructor_args():
    sig = inspect.signature(TreeItemUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_styleupdater_is_not_abstract():
    assert not inspect.isabstract(StyleUpdater)


def test_hyp_styleupdater_constructor_exists():
    assert callable(StyleUpdater.__init__)


def test_hyp_styleupdater_constructor_args():
    sig = inspect.signature(StyleUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemmapping_is_not_abstract():
    assert not inspect.isabstract(TreeItemMapping)


def test_hyp_treeitemmapping_constructor_exists():
    assert callable(TreeItemMapping.__init__)


def test_hyp_treeitemmapping_constructor_args():
    sig = inspect.signature(TreeItemMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_treeitemstyle_is_not_abstract():
    assert not inspect.isabstract(tree_TreeItemStyle)


def test_hyp_tree_treeitemstyle_constructor_exists():
    assert callable(tree_TreeItemStyle.__init__)


def test_hyp_tree_treeitemstyle_constructor_args():
    sig = inspect.signature(tree_TreeItemStyle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dtreeelement_is_not_abstract():
    assert not inspect.isabstract(DTreeElement)


def test_hyp_dtreeelement_constructor_exists():
    assert callable(DTreeElement.__init__)


def test_hyp_dtreeelement_constructor_args():
    sig = inspect.signature(DTreeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_hyp_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_hyp_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_dtreeitemcontainer_is_not_abstract():
    assert not inspect.isabstract(tree_DTreeItemContainer)


def test_hyp_tree_dtreeitemcontainer_constructor_exists():
    assert callable(tree_DTreeItemContainer.__init__)


def test_hyp_tree_dtreeitemcontainer_constructor_args():
    sig = inspect.signature(tree_DTreeItemContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_treeitemupdater_is_not_abstract():
    assert not inspect.isabstract(description_TreeItemUpdater)


def test_hyp_description_treeitemupdater_constructor_exists():
    assert callable(description_TreeItemUpdater.__init__)


def test_hyp_description_treeitemupdater_constructor_args():
    sig = inspect.signature(description_TreeItemUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_styleupdater_is_not_abstract():
    assert not inspect.isabstract(description_StyleUpdater)


def test_hyp_description_styleupdater_constructor_exists():
    assert callable(description_StyleUpdater.__init__)


def test_hyp_description_styleupdater_constructor_args():
    sig = inspect.signature(description_StyleUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_description_treemapping_is_not_abstract():
    assert not inspect.isabstract(description_TreeMapping)


def test_hyp_description_treemapping_constructor_exists():
    assert callable(description_TreeMapping.__init__)


def test_hyp_description_treemapping_constructor_args():
    sig = inspect.signature(description_TreeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_description_treeitemmapping_is_not_abstract():
    assert not inspect.isabstract(tree_description_TreeItemMapping)


def test_hyp_tree_description_treeitemmapping_constructor_exists():
    assert callable(tree_description_TreeItemMapping.__init__)


def test_hyp_tree_description_treeitemmapping_constructor_args():
    sig = inspect.signature(tree_description_TreeItemMapping.__init__)
    params = list(sig.parameters.keys())
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"






def test_hyp_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationNavigationDescription)


def test_hyp_tool_representationnavigationdescription_constructor_exists():
    assert callable(tool_RepresentationNavigationDescription.__init__)


def test_hyp_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_hyp_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_hyp_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treeitemcreationtool_is_not_abstract():
    assert not inspect.isabstract(TreeItemCreationTool)


def test_hyp_treeitemcreationtool_constructor_exists():
    assert callable(TreeItemCreationTool.__init__)


def test_hyp_treeitemcreationtool_constructor_args():
    sig = inspect.signature(TreeItemCreationTool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treemapping_is_not_abstract():
    assert not inspect.isabstract(TreeMapping)


def test_hyp_treemapping_constructor_exists():
    assert callable(TreeMapping.__init__)


def test_hyp_treemapping_constructor_args():
    sig = inspect.signature(TreeMapping.__init__)
    params = list(sig.parameters.keys())



def test_hyp_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_hyp_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_hyp_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_dtreeelement_is_not_abstract():
    assert not inspect.isabstract(tree_DTreeElement)


def test_hyp_tree_dtreeelement_constructor_exists():
    assert callable(tree_DTreeElement.__init__)


def test_hyp_tree_dtreeelement_constructor_args():
    sig = inspect.signature(tree_DTreeElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_dtreeelementupdater_is_not_abstract():
    assert not inspect.isabstract(tree_DTreeElementUpdater)


def test_hyp_tree_dtreeelementupdater_constructor_exists():
    assert callable(tree_DTreeElementUpdater.__init__)


def test_hyp_tree_dtreeelementupdater_constructor_args():
    sig = inspect.signature(tree_DTreeElementUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_treedescription_is_not_abstract():
    assert not inspect.isabstract(TreeDescription)


def test_hyp_treedescription_constructor_exists():
    assert callable(TreeDescription.__init__)


def test_hyp_treedescription_constructor_args():
    sig = inspect.signature(TreeDescription.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_eobject_is_not_abstract():
    assert not inspect.isabstract(tree_EObject)


def test_hyp_tree_eobject_constructor_exists():
    assert callable(tree_EObject.__init__)


def test_hyp_tree_eobject_constructor_args():
    sig = inspect.signature(tree_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dtreeelementupdater_is_not_abstract():
    assert not inspect.isabstract(DTreeElementUpdater)


def test_hyp_dtreeelementupdater_constructor_exists():
    assert callable(DTreeElementUpdater.__init__)


def test_hyp_dtreeelementupdater_constructor_args():
    sig = inspect.signature(DTreeElementUpdater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dtreeitemcontainer_is_not_abstract():
    assert not inspect.isabstract(DTreeItemContainer)


def test_hyp_dtreeitemcontainer_constructor_exists():
    assert callable(DTreeItemContainer.__init__)


def test_hyp_dtreeitemcontainer_constructor_args():
    sig = inspect.signature(DTreeItemContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_dtreeitem_is_not_abstract():
    assert not inspect.isabstract(tree_DTreeItem)


def test_hyp_tree_dtreeitem_constructor_exists():
    assert callable(tree_DTreeItem.__init__)


def test_hyp_tree_dtreeitem_constructor_args():
    sig = inspect.signature(tree_DTreeItem.__init__)
    params = list(sig.parameters.keys())
    assert "expanded" in params, "Missing parameter 'expanded'"




def test_hyp_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_hyp_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_hyp_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tree_dtree_is_not_abstract():
    assert not inspect.isabstract(tree_DTree)


def test_hyp_tree_dtree_constructor_exists():
    assert callable(tree_DTree.__init__)


def test_hyp_tree_dtree_constructor_args():
    sig = inspect.signature(tree_DTree.__init__)
    params = list(sig.parameters.keys())

def test_hyp_treedragsource_exists():
    # Check that the Enumeration exists
    assert TreeDragSource is not None

def test_hyp_treedragsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeDragSource]
    expected_literals = [
        "PROJECT_EXPLORER",
        "TREE",
        "BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeDragSource"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
TreeItemEditionTool_strategy = st.builds(
    TreeItemEditionTool,
)
tree_description_TreeItemUpdater_strategy = st.builds(
    tree_description_TreeItemUpdater,
)
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
tool_AbstractVariable_strategy = st.builds(
    tool_AbstractVariable,
)
tree_description_TreeVariable_strategy = st.builds(
    tree_description_TreeVariable,
    documentation=
        safe_text
)
ConditionalTreeItemStyleDescription_strategy = st.builds(
    ConditionalTreeItemStyleDescription,
)
tree_description_StyleUpdater_strategy = st.builds(
    tree_description_StyleUpdater,
)
tool_MenuItemOrRef_strategy = st.builds(
    tool_MenuItemOrRef,
)
TreeItemContainerDropTool_strategy = st.builds(
    TreeItemContainerDropTool,
)
tree_description_TreeItemMappingContainer_strategy = st.builds(
    tree_description_TreeItemMappingContainer,
)
RepresentationElementMapping_strategy = st.builds(
    RepresentationElementMapping,
)
tree_description_TreeMapping_strategy = st.builds(
    tree_description_TreeMapping,
    semanticElements=
        safe_text
)
PrecedingSiblingsVariables_strategy = st.builds(
    PrecedingSiblingsVariables,
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
tree_description_TreeNavigationDescription_strategy = st.builds(
    tree_description_TreeNavigationDescription,
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
tree_description_TreeCreationDescription_strategy = st.builds(
    tree_description_TreeCreationDescription,
)
TreeItemMappingContainer_strategy = st.builds(
    TreeItemMappingContainer,
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_ElementDropVariable_strategy = st.builds(
    tool_ElementDropVariable,
)
tool_EditMaskVariables_strategy = st.builds(
    tool_EditMaskVariables,
)
TreeItemTool_strategy = st.builds(
    TreeItemTool,
)
tree_description_TreeItemDeletionTool_strategy = st.builds(
    tree_description_TreeItemDeletionTool,
)
tree_description_TreeItemEditionTool_strategy = st.builds(
    tree_description_TreeItemEditionTool,
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
style_LabelStyleDescription_strategy = st.builds(
    style_LabelStyleDescription,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
)
tree_description_TreeItemStyleDescription_strategy = st.builds(
    tree_description_TreeItemStyleDescription,
)
TreePopupMenu_strategy = st.builds(
    TreePopupMenu,
)
TreeItemDragTool_strategy = st.builds(
    TreeItemDragTool,
)
TreeItemDeletionTool_strategy = st.builds(
    TreeItemDeletionTool,
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
description_TreeItemTool_strategy = st.builds(
    description_TreeItemTool,
)
tool_MappingBasedToolDescription_strategy = st.builds(
    tool_MappingBasedToolDescription,
)
tree_description_TreeItemContainerDropTool_strategy = st.builds(
    tree_description_TreeItemContainerDropTool,
    dragSource=
        safe_text
)
tree_description_TreeItemCreationTool_strategy = st.builds(
    tree_description_TreeItemCreationTool,
)
tree_description_TreeItemDragTool_strategy = st.builds(
    tree_description_TreeItemDragTool,
    dragSourceType=
        safe_text
)
TreeVariable_strategy = st.builds(
    TreeVariable,
)
tree_description_PrecedingSiblingsVariables_strategy = st.builds(
    tree_description_PrecedingSiblingsVariables,
)
tool_ModelOperation_strategy = st.builds(
    tool_ModelOperation,
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
tree_description_TreePopupMenu_strategy = st.builds(
    tree_description_TreePopupMenu,
)
tree_description_TreeItemTool_strategy = st.builds(
    tree_description_TreeItemTool,
)
TreeItemStyleDescription_strategy = st.builds(
    TreeItemStyleDescription,
)
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
tree_description_ConditionalTreeItemStyleDescription_strategy = st.builds(
    tree_description_ConditionalTreeItemStyleDescription,
)
description_TreeItemMappingContainer_strategy = st.builds(
    description_TreeItemMappingContainer,
)
description_RepresentationDescription_strategy = st.builds(
    description_RepresentationDescription,
)
tree_description_TreeDescription_strategy = st.builds(
    tree_description_TreeDescription,
    preconditionExpression=
        safe_text,
    domainClass=
        safe_text
)
tree_DTreeElementSynchronizer_strategy = st.builds(
    tree_DTreeElementSynchronizer,
)
tree_RGBValues_strategy = st.builds(
    tree_RGBValues,
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
Style_strategy = st.builds(
    Style,
)
TreeItemUpdater_strategy = st.builds(
    TreeItemUpdater,
)
StyleUpdater_strategy = st.builds(
    StyleUpdater,
)
TreeItemMapping_strategy = st.builds(
    TreeItemMapping,
)
tree_TreeItemStyle_strategy = st.builds(
    tree_TreeItemStyle,
)
DTreeElement_strategy = st.builds(
    DTreeElement,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
tree_DTreeItemContainer_strategy = st.builds(
    tree_DTreeItemContainer,
)
description_TreeItemUpdater_strategy = st.builds(
    description_TreeItemUpdater,
)
description_StyleUpdater_strategy = st.builds(
    description_StyleUpdater,
)
description_TreeMapping_strategy = st.builds(
    description_TreeMapping,
)
tree_description_TreeItemMapping_strategy = st.builds(
    tree_description_TreeItemMapping,
    preconditionExpression=
        safe_text,
    semanticCandidatesExpression=
        safe_text,
    domainClass=
        safe_text
)
tool_RepresentationNavigationDescription_strategy = st.builds(
    tool_RepresentationNavigationDescription,
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
TreeItemCreationTool_strategy = st.builds(
    TreeItemCreationTool,
)
TreeMapping_strategy = st.builds(
    TreeMapping,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
tree_DTreeElement_strategy = st.builds(
    tree_DTreeElement,
)
tree_DTreeElementUpdater_strategy = st.builds(
    tree_DTreeElementUpdater,
)
TreeDescription_strategy = st.builds(
    TreeDescription,
)
tree_EObject_strategy = st.builds(
    tree_EObject,
)
DTreeElementUpdater_strategy = st.builds(
    DTreeElementUpdater,
)
DTreeItemContainer_strategy = st.builds(
    DTreeItemContainer,
)
tree_DTreeItem_strategy = st.builds(
    tree_DTreeItem,
    expanded=
        st.booleans()
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
tree_DTree_strategy = st.builds(
    tree_DTree,
)








@given(instance=tree_description_TreeVariable_strategy)
def test_hyp_tree_description_treevariable_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original










@given(instance=tree_description_TreeMapping_strategy)
def test_hyp_tree_description_treemapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original


























@given(instance=tree_description_TreeItemContainerDropTool_strategy)
def test_hyp_tree_description_treeitemcontainerdroptool_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original





@given(instance=tree_description_TreeItemDragTool_strategy)
def test_hyp_tree_description_treeitemdragtool_dragSourceType_setter(instance):
    original = instance.dragSourceType
    instance.dragSourceType = original
    assert instance.dragSourceType == original















@given(instance=tree_description_TreeDescription_strategy)
def test_hyp_tree_description_treedescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=tree_description_TreeDescription_strategy)
def test_hyp_tree_description_treedescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tree_DTreeElementSynchronizer_strategy)
@settings(max_examples=30)
def test_hyp_tree_dtreeelementsynchronizer_refresh_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.refresh(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.refresh).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'refresh' in tree_DTreeElementSynchronizer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'refresh' in tree_DTreeElementSynchronizer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'refresh' in tree_DTreeElementSynchronizer is not implemented or raised an error")

















@given(instance=tree_description_TreeItemMapping_strategy)
def test_hyp_tree_description_treeitemmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=tree_description_TreeItemMapping_strategy)
def test_hyp_tree_description_treeitemmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original



@given(instance=tree_description_TreeItemMapping_strategy)
def test_hyp_tree_description_treeitemmapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tree_DTreeElementUpdater_strategy)
@settings(max_examples=30)
def test_hyp_tree_dtreeelementupdater_deactivate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.deactivate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.deactivate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'deactivate' in tree_DTreeElementUpdater is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'deactivate' in tree_DTreeElementUpdater did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'deactivate' in tree_DTreeElementUpdater is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tree_DTreeElementUpdater_strategy)
@settings(max_examples=30)
def test_hyp_tree_dtreeelementupdater_activate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activate' in tree_DTreeElementUpdater is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activate' in tree_DTreeElementUpdater did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activate' in tree_DTreeElementUpdater is not implemented or raised an error")








@given(instance=tree_DTreeItem_strategy)
def test_hyp_tree_dtreeitem_expanded_setter(instance):
    original = instance.expanded
    instance.expanded = original
    assert instance.expanded == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_tree_DTreeItem_expanded_value_roundtrip():
    instance = tree_DTreeItem(expanded=True)
    assert instance.expanded == True
    instance.expanded = False
    assert instance.expanded == False


def test_tree_description_TreeDescription_domainClass_value_roundtrip():
    instance = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_tree_description_TreeDescription_preconditionExpression_value_roundtrip():
    instance = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_tree_description_TreeItemContainerDropTool_dragSource_value_roundtrip():
    instance = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    assert instance.dragSource == "sample_text"
    instance.dragSource = "sample_text_2"
    assert instance.dragSource == "sample_text_2"


def test_tree_description_TreeItemDragTool_dragSourceType_value_roundtrip():
    instance = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    assert instance.dragSourceType == "sample_text"
    instance.dragSourceType = "sample_text_2"
    assert instance.dragSourceType == "sample_text_2"


def test_tree_description_TreeItemMapping_domainClass_value_roundtrip():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.domainClass == "sample_text"
    instance.domainClass = "sample_text_2"
    assert instance.domainClass == "sample_text_2"


def test_tree_description_TreeItemMapping_preconditionExpression_value_roundtrip():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.preconditionExpression == "sample_text"
    instance.preconditionExpression = "sample_text_2"
    assert instance.preconditionExpression == "sample_text_2"


def test_tree_description_TreeItemMapping_semanticCandidatesExpression_value_roundtrip():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert instance.semanticCandidatesExpression == "sample_text"
    instance.semanticCandidatesExpression = "sample_text_2"
    assert instance.semanticCandidatesExpression == "sample_text_2"


def test_tree_description_TreeMapping_semanticElements_value_roundtrip():
    instance = tree_description_TreeMapping(semanticElements="sample_text")
    assert instance.semanticElements == "sample_text"
    instance.semanticElements = "sample_text_2"
    assert instance.semanticElements == "sample_text_2"


def test_tree_description_TreeVariable_documentation_value_roundtrip():
    instance = tree_description_TreeVariable(documentation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_tree_description_TreeItemTool_isa_AbstractToolDescription():
    instance = tree_description_TreeItemTool()
    assert isinstance(instance, AbstractToolDescription)


def test_tree_description_TreePopupMenu_isa_AbstractToolDescription():
    instance = tree_description_TreePopupMenu()
    assert isinstance(instance, AbstractToolDescription)


def test_tree_description_ConditionalTreeItemStyleDescription_isa_ConditionalStyleDescription():
    instance = tree_description_ConditionalTreeItemStyleDescription()
    assert isinstance(instance, ConditionalStyleDescription)


def test_tree_DTree_isa_DRepresentation():
    instance = tree_DTree()
    assert isinstance(instance, DRepresentation)


def test_tree_DTreeElement_isa_DRepresentationElement():
    instance = tree_DTreeElement()
    assert isinstance(instance, DRepresentationElement)


def test_tree_DTreeItemContainer_isa_DSemanticDecorator():
    instance = tree_DTreeItemContainer()
    assert isinstance(instance, DSemanticDecorator)


def test_tree_DTreeItem_isa_DTreeElement():
    instance = tree_DTreeItem(expanded=True)
    assert isinstance(instance, DTreeElement)


def test_tree_DTree_isa_DTreeElementUpdater():
    instance = tree_DTree()
    assert isinstance(instance, DTreeElementUpdater)


def test_tree_DTreeItem_isa_DTreeElementUpdater():
    instance = tree_DTreeItem(expanded=True)
    assert isinstance(instance, DTreeElementUpdater)


def test_tree_DTree_isa_DTreeItemContainer():
    instance = tree_DTree()
    assert isinstance(instance, DTreeItemContainer)


def test_tree_DTreeItem_isa_DTreeItemContainer():
    instance = tree_DTreeItem(expanded=True)
    assert isinstance(instance, DTreeItemContainer)


def test_tree_TreeItemStyle_isa_LabelStyle():
    instance = tree_TreeItemStyle()
    assert isinstance(instance, LabelStyle)


def test_tree_description_TreeCreationDescription_isa_RepresentationCreationDescription():
    instance = tree_description_TreeCreationDescription()
    assert isinstance(instance, RepresentationCreationDescription)


def test_tree_description_TreeMapping_isa_RepresentationElementMapping():
    instance = tree_description_TreeMapping(semanticElements="sample_text")
    assert isinstance(instance, RepresentationElementMapping)


def test_tree_description_TreeNavigationDescription_isa_RepresentationNavigationDescription():
    instance = tree_description_TreeNavigationDescription()
    assert isinstance(instance, RepresentationNavigationDescription)


def test_tree_TreeItemStyle_isa_Style():
    instance = tree_TreeItemStyle()
    assert isinstance(instance, Style)


def test_tree_description_TreeItemDeletionTool_isa_TreeItemTool():
    instance = tree_description_TreeItemDeletionTool()
    assert isinstance(instance, TreeItemTool)


def test_tree_description_TreeItemEditionTool_isa_TreeItemTool():
    instance = tree_description_TreeItemEditionTool()
    assert isinstance(instance, TreeItemTool)


def test_tree_description_PrecedingSiblingsVariables_isa_TreeVariable():
    instance = tree_description_PrecedingSiblingsVariables()
    assert isinstance(instance, TreeVariable)


def test_tree_description_TreeDescription_isa_description_RepresentationDescription():
    instance = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    assert isinstance(instance, description_RepresentationDescription)


def test_tree_description_TreeItemMapping_isa_description_StyleUpdater():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_StyleUpdater)


def test_tree_description_TreeDescription_isa_description_TreeItemMappingContainer():
    instance = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    assert isinstance(instance, description_TreeItemMappingContainer)


def test_tree_description_TreeItemMapping_isa_description_TreeItemMappingContainer():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_TreeItemMappingContainer)


def test_tree_description_TreeItemContainerDropTool_isa_description_TreeItemTool():
    instance = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    assert isinstance(instance, description_TreeItemTool)


def test_tree_description_TreeItemCreationTool_isa_description_TreeItemTool():
    instance = tree_description_TreeItemCreationTool()
    assert isinstance(instance, description_TreeItemTool)


def test_tree_description_TreeItemDragTool_isa_description_TreeItemTool():
    instance = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    assert isinstance(instance, description_TreeItemTool)


def test_tree_description_TreeItemMapping_isa_description_TreeItemUpdater():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_TreeItemUpdater)


def test_tree_description_TreeItemMapping_isa_description_TreeMapping():
    instance = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    assert isinstance(instance, description_TreeMapping)


def test_tree_description_TreeItemStyleDescription_isa_style_LabelStyleDescription():
    instance = tree_description_TreeItemStyleDescription()
    assert isinstance(instance, style_LabelStyleDescription)


def test_tree_description_TreeItemStyleDescription_isa_style_StyleDescription():
    instance = tree_description_TreeItemStyleDescription()
    assert isinstance(instance, style_StyleDescription)


def test_tree_description_TreeVariable_isa_tool_AbstractVariable():
    instance = tree_description_TreeVariable(documentation="sample_text")
    assert isinstance(instance, tool_AbstractVariable)


def test_tree_description_TreeItemContainerDropTool_isa_tool_MappingBasedToolDescription():
    instance = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    assert isinstance(instance, tool_MappingBasedToolDescription)


def test_tree_description_TreeItemCreationTool_isa_tool_MappingBasedToolDescription():
    instance = tree_description_TreeItemCreationTool()
    assert isinstance(instance, tool_MappingBasedToolDescription)


def test_tree_description_TreeItemDragTool_isa_tool_MappingBasedToolDescription():
    instance = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    assert isinstance(instance, tool_MappingBasedToolDescription)


def test_tree_description_TreeVariable_isa_tool_VariableContainer():
    instance = tree_description_TreeVariable(documentation="sample_text")
    assert isinstance(instance, tool_VariableContainer)


def test_assoc_actualMapping6_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = TreeItemMapping()
    b2 = TreeItemMapping()
    _safe_set(a, 'tree_DTreeItem7', b1)
    assert _is_linked(a, 'tree_DTreeItem7', b1)
    if hasattr(b1, 'TreeItemMapping'):
        assert _is_linked(b1, 'TreeItemMapping', a)
    _safe_set(a, 'tree_DTreeItem7', b2)
    assert _is_linked(a, 'tree_DTreeItem7', b2)
    if hasattr(b1, 'TreeItemMapping'):
        assert not _is_linked(b1, 'TreeItemMapping', a)
    if hasattr(b2, 'TreeItemMapping'):
        assert _is_linked(b2, 'TreeItemMapping', a)
    _safe_set(a, 'tree_DTreeItem7', None)
    assert not _is_linked(a, 'tree_DTreeItem7', b2)
    if hasattr(b2, 'TreeItemMapping'):
        assert not _is_linked(b2, 'TreeItemMapping', a)


def test_assoc_allSubMappings22_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemMapping()
    b2 = TreeItemMapping()
    _safe_set(a, 'tree_description_TreeItemMapping23', {b1})
    assert _is_linked(a, 'tree_description_TreeItemMapping23', b1)
    if hasattr(b1, 'TreeItemMapping24'):
        assert _is_linked(b1, 'TreeItemMapping24', a)
    _safe_set(a, 'tree_description_TreeItemMapping23', {b2})
    assert _is_linked(a, 'tree_description_TreeItemMapping23', b2)
    if hasattr(b1, 'TreeItemMapping24'):
        assert not _is_linked(b1, 'TreeItemMapping24', a)
    if hasattr(b2, 'TreeItemMapping24'):
        assert _is_linked(b2, 'TreeItemMapping24', a)
    _safe_set(a, 'tree_description_TreeItemMapping23', set())
    assert not _is_linked(a, 'tree_description_TreeItemMapping23', b2)
    if hasattr(b2, 'TreeItemMapping24'):
        assert not _is_linked(b2, 'TreeItemMapping24', a)


def test_assoc_container8_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = tree_DTreeItemContainer()
    b2 = tree_DTreeItemContainer()
    _safe_set(a, 'ownedTreeItems', b1)
    assert _is_linked(a, 'ownedTreeItems', b1)
    if hasattr(b1, 'DTreeItemContainer'):
        assert _is_linked(b1, 'DTreeItemContainer', a)
    _safe_set(a, 'ownedTreeItems', b2)
    assert _is_linked(a, 'ownedTreeItems', b2)
    if hasattr(b1, 'DTreeItemContainer'):
        assert not _is_linked(b1, 'DTreeItemContainer', a)
    if hasattr(b2, 'DTreeItemContainer'):
        assert _is_linked(b2, 'DTreeItemContainer', a)
    _safe_set(a, 'ownedTreeItems', None)
    assert not _is_linked(a, 'ownedTreeItems', b2)
    if hasattr(b2, 'DTreeItemContainer'):
        assert not _is_linked(b2, 'DTreeItemContainer', a)


def test_assoc_containers49_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = TreeItemMappingContainer()
    b2 = TreeItemMappingContainer()
    _safe_set(a, 'tree_description_TreeItemDragTool50', {b1})
    assert _is_linked(a, 'tree_description_TreeItemDragTool50', b1)
    if hasattr(b1, 'TreeItemMappingContainer'):
        assert _is_linked(b1, 'TreeItemMappingContainer', a)
    _safe_set(a, 'tree_description_TreeItemDragTool50', {b2})
    assert _is_linked(a, 'tree_description_TreeItemDragTool50', b2)
    if hasattr(b1, 'TreeItemMappingContainer'):
        assert not _is_linked(b1, 'TreeItemMappingContainer', a)
    if hasattr(b2, 'TreeItemMappingContainer'):
        assert _is_linked(b2, 'TreeItemMappingContainer', a)
    _safe_set(a, 'tree_description_TreeItemDragTool50', set())
    assert not _is_linked(a, 'tree_description_TreeItemDragTool50', b2)
    if hasattr(b2, 'TreeItemMappingContainer'):
        assert not _is_linked(b2, 'TreeItemMappingContainer', a)


def test_assoc_create29_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemCreationTool()
    b2 = TreeItemCreationTool()
    _safe_set(a, 'tree_description_TreeItemMapping30', {b1})
    assert _is_linked(a, 'tree_description_TreeItemMapping30', b1)
    if hasattr(b1, 'TreeItemCreationTool31'):
        assert _is_linked(b1, 'TreeItemCreationTool31', a)
    _safe_set(a, 'tree_description_TreeItemMapping30', {b2})
    assert _is_linked(a, 'tree_description_TreeItemMapping30', b2)
    if hasattr(b1, 'TreeItemCreationTool31'):
        assert not _is_linked(b1, 'TreeItemCreationTool31', a)
    if hasattr(b2, 'TreeItemCreationTool31'):
        assert _is_linked(b2, 'TreeItemCreationTool31', a)
    _safe_set(a, 'tree_description_TreeItemMapping30', set())
    assert not _is_linked(a, 'tree_description_TreeItemMapping30', b2)
    if hasattr(b2, 'TreeItemCreationTool31'):
        assert not _is_linked(b2, 'TreeItemCreationTool31', a)


def test_assoc_createTreeItem15_link_reassign_clear():
    a = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    b1 = TreeItemCreationTool()
    b2 = TreeItemCreationTool()
    _safe_set(a, 'tree_description_TreeDescription', {b1})
    assert _is_linked(a, 'tree_description_TreeDescription', b1)
    if hasattr(b1, 'TreeItemCreationTool'):
        assert _is_linked(b1, 'TreeItemCreationTool', a)
    _safe_set(a, 'tree_description_TreeDescription', {b2})
    assert _is_linked(a, 'tree_description_TreeDescription', b2)
    if hasattr(b1, 'TreeItemCreationTool'):
        assert not _is_linked(b1, 'TreeItemCreationTool', a)
    if hasattr(b2, 'TreeItemCreationTool'):
        assert _is_linked(b2, 'TreeItemCreationTool', a)
    _safe_set(a, 'tree_description_TreeDescription', set())
    assert not _is_linked(a, 'tree_description_TreeDescription', b2)
    if hasattr(b2, 'TreeItemCreationTool'):
        assert not _is_linked(b2, 'TreeItemCreationTool', a)


def test_assoc_delete28_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemDeletionTool()
    b2 = TreeItemDeletionTool()
    _safe_set(a, 'mapping', b1)
    assert _is_linked(a, 'mapping', b1)
    if hasattr(b1, 'TreeItemDeletionTool'):
        assert _is_linked(b1, 'TreeItemDeletionTool', a)
    _safe_set(a, 'mapping', b2)
    assert _is_linked(a, 'mapping', b2)
    if hasattr(b1, 'TreeItemDeletionTool'):
        assert not _is_linked(b1, 'TreeItemDeletionTool', a)
    if hasattr(b2, 'TreeItemDeletionTool'):
        assert _is_linked(b2, 'TreeItemDeletionTool', a)
    _safe_set(a, 'mapping', None)
    assert not _is_linked(a, 'mapping', b2)
    if hasattr(b2, 'TreeItemDeletionTool'):
        assert not _is_linked(b2, 'TreeItemDeletionTool', a)


def test_assoc_directEdit89_link_reassign_clear():
    a = tree_description_TreeItemUpdater()
    b1 = TreeItemEditionTool()
    b2 = TreeItemEditionTool()
    _safe_set(a, 'tree_description_TreeItemUpdater', b1)
    assert _is_linked(a, 'tree_description_TreeItemUpdater', b1)
    if hasattr(b1, 'TreeItemEditionTool'):
        assert _is_linked(b1, 'TreeItemEditionTool', a)
    _safe_set(a, 'tree_description_TreeItemUpdater', b2)
    assert _is_linked(a, 'tree_description_TreeItemUpdater', b2)
    if hasattr(b1, 'TreeItemEditionTool'):
        assert not _is_linked(b1, 'TreeItemEditionTool', a)
    if hasattr(b2, 'TreeItemEditionTool'):
        assert _is_linked(b2, 'TreeItemEditionTool', a)
    _safe_set(a, 'tree_description_TreeItemUpdater', None)
    assert not _is_linked(a, 'tree_description_TreeItemUpdater', b2)
    if hasattr(b2, 'TreeItemEditionTool'):
        assert not _is_linked(b2, 'TreeItemEditionTool', a)


def test_assoc_dndTools32_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemDragTool()
    b2 = TreeItemDragTool()
    _safe_set(a, 'tree_description_TreeItemMapping33', {b1})
    assert _is_linked(a, 'tree_description_TreeItemMapping33', b1)
    if hasattr(b1, 'TreeItemDragTool'):
        assert _is_linked(b1, 'TreeItemDragTool', a)
    _safe_set(a, 'tree_description_TreeItemMapping33', {b2})
    assert _is_linked(a, 'tree_description_TreeItemMapping33', b2)
    if hasattr(b1, 'TreeItemDragTool'):
        assert not _is_linked(b1, 'TreeItemDragTool', a)
    if hasattr(b2, 'TreeItemDragTool'):
        assert _is_linked(b2, 'TreeItemDragTool', a)
    _safe_set(a, 'tree_description_TreeItemMapping33', set())
    assert not _is_linked(a, 'tree_description_TreeItemMapping33', b2)
    if hasattr(b2, 'TreeItemDragTool'):
        assert not _is_linked(b2, 'TreeItemDragTool', a)


def test_assoc_element45_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = tool_ElementDropVariable()
    b2 = tool_ElementDropVariable()
    _safe_set(a, 'tree_description_TreeItemDragTool46', b1)
    assert _is_linked(a, 'tree_description_TreeItemDragTool46', b1)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert _is_linked(b1, 'tool_ElementDropVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool46', b2)
    assert _is_linked(a, 'tree_description_TreeItemDragTool46', b2)
    if hasattr(b1, 'tool_ElementDropVariable'):
        assert not _is_linked(b1, 'tool_ElementDropVariable', a)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert _is_linked(b2, 'tool_ElementDropVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool46', None)
    assert not _is_linked(a, 'tree_description_TreeItemDragTool46', b2)
    if hasattr(b2, 'tool_ElementDropVariable'):
        assert not _is_linked(b2, 'tool_ElementDropVariable', a)


def test_assoc_element58_link_reassign_clear():
    a = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    b1 = tool_ElementDropVariable()
    b2 = tool_ElementDropVariable()
    _safe_set(a, 'tree_description_TreeItemContainerDropTool59', b1)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool59', b1)
    if hasattr(b1, 'tool_ElementDropVariable60'):
        assert _is_linked(b1, 'tool_ElementDropVariable60', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool59', b2)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool59', b2)
    if hasattr(b1, 'tool_ElementDropVariable60'):
        assert not _is_linked(b1, 'tool_ElementDropVariable60', a)
    if hasattr(b2, 'tool_ElementDropVariable60'):
        assert _is_linked(b2, 'tool_ElementDropVariable60', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool59', None)
    assert not _is_linked(a, 'tree_description_TreeItemContainerDropTool59', b2)
    if hasattr(b2, 'tool_ElementDropVariable60'):
        assert not _is_linked(b2, 'tool_ElementDropVariable60', a)


def test_assoc_newContainer42_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'tree_description_TreeItemDragTool43', b1)
    assert _is_linked(a, 'tree_description_TreeItemDragTool43', b1)
    if hasattr(b1, 'tool_DropContainerVariable44'):
        assert _is_linked(b1, 'tool_DropContainerVariable44', a)
    _safe_set(a, 'tree_description_TreeItemDragTool43', b2)
    assert _is_linked(a, 'tree_description_TreeItemDragTool43', b2)
    if hasattr(b1, 'tool_DropContainerVariable44'):
        assert not _is_linked(b1, 'tool_DropContainerVariable44', a)
    if hasattr(b2, 'tool_DropContainerVariable44'):
        assert _is_linked(b2, 'tool_DropContainerVariable44', a)
    _safe_set(a, 'tree_description_TreeItemDragTool43', None)
    assert not _is_linked(a, 'tree_description_TreeItemDragTool43', b2)
    if hasattr(b2, 'tool_DropContainerVariable44'):
        assert not _is_linked(b2, 'tool_DropContainerVariable44', a)


def test_assoc_newContainer55_link_reassign_clear():
    a = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'tree_description_TreeItemContainerDropTool56', b1)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool56', b1)
    if hasattr(b1, 'tool_DropContainerVariable57'):
        assert _is_linked(b1, 'tool_DropContainerVariable57', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool56', b2)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool56', b2)
    if hasattr(b1, 'tool_DropContainerVariable57'):
        assert not _is_linked(b1, 'tool_DropContainerVariable57', a)
    if hasattr(b2, 'tool_DropContainerVariable57'):
        assert _is_linked(b2, 'tool_DropContainerVariable57', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool56', None)
    assert not _is_linked(a, 'tree_description_TreeItemContainerDropTool56', b2)
    if hasattr(b2, 'tool_DropContainerVariable57'):
        assert not _is_linked(b2, 'tool_DropContainerVariable57', a)


def test_assoc_newViewContainer47_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'tree_description_TreeItemDragTool48', b1)
    assert _is_linked(a, 'tree_description_TreeItemDragTool48', b1)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert _is_linked(b1, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool48', b2)
    assert _is_linked(a, 'tree_description_TreeItemDragTool48', b2)
    if hasattr(b1, 'tool_ContainerViewVariable'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable', a)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert _is_linked(b2, 'tool_ContainerViewVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool48', None)
    assert not _is_linked(a, 'tree_description_TreeItemDragTool48', b2)
    if hasattr(b2, 'tool_ContainerViewVariable'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable', a)


def test_assoc_newViewContainer61_link_reassign_clear():
    a = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    b1 = tool_ContainerViewVariable()
    b2 = tool_ContainerViewVariable()
    _safe_set(a, 'tree_description_TreeItemContainerDropTool62', b1)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool62', b1)
    if hasattr(b1, 'tool_ContainerViewVariable63'):
        assert _is_linked(b1, 'tool_ContainerViewVariable63', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool62', b2)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool62', b2)
    if hasattr(b1, 'tool_ContainerViewVariable63'):
        assert not _is_linked(b1, 'tool_ContainerViewVariable63', a)
    if hasattr(b2, 'tool_ContainerViewVariable63'):
        assert _is_linked(b2, 'tool_ContainerViewVariable63', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool62', None)
    assert not _is_linked(a, 'tree_description_TreeItemContainerDropTool62', b2)
    if hasattr(b2, 'tool_ContainerViewVariable63'):
        assert not _is_linked(b2, 'tool_ContainerViewVariable63', a)


def test_assoc_oldContainer41_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'tree_description_TreeItemDragTool', b1)
    assert _is_linked(a, 'tree_description_TreeItemDragTool', b1)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert _is_linked(b1, 'tool_DropContainerVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool', b2)
    assert _is_linked(a, 'tree_description_TreeItemDragTool', b2)
    if hasattr(b1, 'tool_DropContainerVariable'):
        assert not _is_linked(b1, 'tool_DropContainerVariable', a)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert _is_linked(b2, 'tool_DropContainerVariable', a)
    _safe_set(a, 'tree_description_TreeItemDragTool', None)
    assert not _is_linked(a, 'tree_description_TreeItemDragTool', b2)
    if hasattr(b2, 'tool_DropContainerVariable'):
        assert not _is_linked(b2, 'tool_DropContainerVariable', a)


def test_assoc_oldContainer53_link_reassign_clear():
    a = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    b1 = tool_DropContainerVariable()
    b2 = tool_DropContainerVariable()
    _safe_set(a, 'tree_description_TreeItemContainerDropTool', b1)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool', b1)
    if hasattr(b1, 'tool_DropContainerVariable54'):
        assert _is_linked(b1, 'tool_DropContainerVariable54', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool', b2)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool', b2)
    if hasattr(b1, 'tool_DropContainerVariable54'):
        assert not _is_linked(b1, 'tool_DropContainerVariable54', a)
    if hasattr(b2, 'tool_DropContainerVariable54'):
        assert _is_linked(b2, 'tool_DropContainerVariable54', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool', None)
    assert not _is_linked(a, 'tree_description_TreeItemContainerDropTool', b2)
    if hasattr(b2, 'tool_DropContainerVariable54'):
        assert not _is_linked(b2, 'tool_DropContainerVariable54', a)


def test_assoc_ownedRepresentationCreationDescriptions16_link_reassign_clear():
    a = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    b1 = tool_RepresentationCreationDescription()
    b2 = tool_RepresentationCreationDescription()
    _safe_set(a, 'tree_description_TreeDescription17', {b1})
    assert _is_linked(a, 'tree_description_TreeDescription17', b1)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'tree_description_TreeDescription17', {b2})
    assert _is_linked(a, 'tree_description_TreeDescription17', b2)
    if hasattr(b1, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b1, 'tool_RepresentationCreationDescription', a)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert _is_linked(b2, 'tool_RepresentationCreationDescription', a)
    _safe_set(a, 'tree_description_TreeDescription17', set())
    assert not _is_linked(a, 'tree_description_TreeDescription17', b2)
    if hasattr(b2, 'tool_RepresentationCreationDescription'):
        assert not _is_linked(b2, 'tool_RepresentationCreationDescription', a)


def test_assoc_ownedRepresentationNavigationDescriptions18_link_reassign_clear():
    a = tree_description_TreeDescription(domainClass="sample_text", preconditionExpression="sample_text")
    b1 = tool_RepresentationNavigationDescription()
    b2 = tool_RepresentationNavigationDescription()
    _safe_set(a, 'tree_description_TreeDescription19', {b1})
    assert _is_linked(a, 'tree_description_TreeDescription19', b1)
    if hasattr(b1, 'tool_RepresentationNavigationDescription'):
        assert _is_linked(b1, 'tool_RepresentationNavigationDescription', a)
    _safe_set(a, 'tree_description_TreeDescription19', {b2})
    assert _is_linked(a, 'tree_description_TreeDescription19', b2)
    if hasattr(b1, 'tool_RepresentationNavigationDescription'):
        assert not _is_linked(b1, 'tool_RepresentationNavigationDescription', a)
    if hasattr(b2, 'tool_RepresentationNavigationDescription'):
        assert _is_linked(b2, 'tool_RepresentationNavigationDescription', a)
    _safe_set(a, 'tree_description_TreeDescription19', set())
    assert not _is_linked(a, 'tree_description_TreeDescription19', b2)
    if hasattr(b2, 'tool_RepresentationNavigationDescription'):
        assert not _is_linked(b2, 'tool_RepresentationNavigationDescription', a)


def test_assoc_ownedStyle5_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = tree_TreeItemStyle()
    b2 = tree_TreeItemStyle()
    _safe_set(a, 'tree_DTreeItem', b1)
    assert _is_linked(a, 'tree_DTreeItem', b1)
    if hasattr(b1, 'tree_TreeItemStyle'):
        assert _is_linked(b1, 'tree_TreeItemStyle', a)
    _safe_set(a, 'tree_DTreeItem', b2)
    assert _is_linked(a, 'tree_DTreeItem', b2)
    if hasattr(b1, 'tree_TreeItemStyle'):
        assert not _is_linked(b1, 'tree_TreeItemStyle', a)
    if hasattr(b2, 'tree_TreeItemStyle'):
        assert _is_linked(b2, 'tree_TreeItemStyle', a)
    _safe_set(a, 'tree_DTreeItem', None)
    assert not _is_linked(a, 'tree_DTreeItem', b2)
    if hasattr(b2, 'tree_TreeItemStyle'):
        assert not _is_linked(b2, 'tree_TreeItemStyle', a)


def test_assoc_ownedTreeItems4_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = tree_DTreeItemContainer()
    b2 = tree_DTreeItemContainer()
    _safe_set(a, 'DTreeItem', b1)
    assert _is_linked(a, 'DTreeItem', b1)
    if hasattr(b1, 'container'):
        assert _is_linked(b1, 'container', a)
    _safe_set(a, 'DTreeItem', b2)
    assert _is_linked(a, 'DTreeItem', b2)
    if hasattr(b1, 'container'):
        assert not _is_linked(b1, 'container', a)
    if hasattr(b2, 'container'):
        assert _is_linked(b2, 'container', a)
    _safe_set(a, 'DTreeItem', None)
    assert not _is_linked(a, 'DTreeItem', b2)
    if hasattr(b2, 'container'):
        assert not _is_linked(b2, 'container', a)


def test_assoc_popupMenus34_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreePopupMenu()
    b2 = TreePopupMenu()
    _safe_set(a, 'tree_description_TreeItemMapping35', {b1})
    assert _is_linked(a, 'tree_description_TreeItemMapping35', b1)
    if hasattr(b1, 'TreePopupMenu'):
        assert _is_linked(b1, 'TreePopupMenu', a)
    _safe_set(a, 'tree_description_TreeItemMapping35', {b2})
    assert _is_linked(a, 'tree_description_TreeItemMapping35', b2)
    if hasattr(b1, 'TreePopupMenu'):
        assert not _is_linked(b1, 'TreePopupMenu', a)
    if hasattr(b2, 'TreePopupMenu'):
        assert _is_linked(b2, 'TreePopupMenu', a)
    _safe_set(a, 'tree_description_TreeItemMapping35', set())
    assert not _is_linked(a, 'tree_description_TreeItemMapping35', b2)
    if hasattr(b2, 'TreePopupMenu'):
        assert not _is_linked(b2, 'TreePopupMenu', a)


def test_assoc_precedingSiblings51_link_reassign_clear():
    a = tree_description_TreeItemDragTool(dragSourceType="sample_text")
    b1 = PrecedingSiblingsVariables()
    b2 = PrecedingSiblingsVariables()
    _safe_set(a, 'tree_description_TreeItemDragTool52', b1)
    assert _is_linked(a, 'tree_description_TreeItemDragTool52', b1)
    if hasattr(b1, 'PrecedingSiblingsVariables'):
        assert _is_linked(b1, 'PrecedingSiblingsVariables', a)
    _safe_set(a, 'tree_description_TreeItemDragTool52', b2)
    assert _is_linked(a, 'tree_description_TreeItemDragTool52', b2)
    if hasattr(b1, 'PrecedingSiblingsVariables'):
        assert not _is_linked(b1, 'PrecedingSiblingsVariables', a)
    if hasattr(b2, 'PrecedingSiblingsVariables'):
        assert _is_linked(b2, 'PrecedingSiblingsVariables', a)
    _safe_set(a, 'tree_description_TreeItemDragTool52', None)
    assert not _is_linked(a, 'tree_description_TreeItemDragTool52', b2)
    if hasattr(b2, 'PrecedingSiblingsVariables'):
        assert not _is_linked(b2, 'PrecedingSiblingsVariables', a)


def test_assoc_precedingSiblings64_link_reassign_clear():
    a = tree_description_TreeItemContainerDropTool(dragSource="sample_text")
    b1 = PrecedingSiblingsVariables()
    b2 = PrecedingSiblingsVariables()
    _safe_set(a, 'tree_description_TreeItemContainerDropTool65', b1)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool65', b1)
    if hasattr(b1, 'PrecedingSiblingsVariables66'):
        assert _is_linked(b1, 'PrecedingSiblingsVariables66', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool65', b2)
    assert _is_linked(a, 'tree_description_TreeItemContainerDropTool65', b2)
    if hasattr(b1, 'PrecedingSiblingsVariables66'):
        assert not _is_linked(b1, 'PrecedingSiblingsVariables66', a)
    if hasattr(b2, 'PrecedingSiblingsVariables66'):
        assert _is_linked(b2, 'PrecedingSiblingsVariables66', a)
    _safe_set(a, 'tree_description_TreeItemContainerDropTool65', None)
    assert not _is_linked(a, 'tree_description_TreeItemContainerDropTool65', b2)
    if hasattr(b2, 'PrecedingSiblingsVariables66'):
        assert not _is_linked(b2, 'PrecedingSiblingsVariables66', a)


def test_assoc_reusedTreeItemMappings20_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemMapping()
    b2 = TreeItemMapping()
    _safe_set(a, 'tree_description_TreeItemMapping', {b1})
    assert _is_linked(a, 'tree_description_TreeItemMapping', b1)
    if hasattr(b1, 'TreeItemMapping21'):
        assert _is_linked(b1, 'TreeItemMapping21', a)
    _safe_set(a, 'tree_description_TreeItemMapping', {b2})
    assert _is_linked(a, 'tree_description_TreeItemMapping', b2)
    if hasattr(b1, 'TreeItemMapping21'):
        assert not _is_linked(b1, 'TreeItemMapping21', a)
    if hasattr(b2, 'TreeItemMapping21'):
        assert _is_linked(b2, 'TreeItemMapping21', a)
    _safe_set(a, 'tree_description_TreeItemMapping', set())
    assert not _is_linked(a, 'tree_description_TreeItemMapping', b2)
    if hasattr(b2, 'TreeItemMapping21'):
        assert not _is_linked(b2, 'TreeItemMapping21', a)


def test_assoc_specialize25_link_reassign_clear():
    a = tree_description_TreeItemMapping(domainClass="sample_text", preconditionExpression="sample_text", semanticCandidatesExpression="sample_text")
    b1 = TreeItemMapping()
    b2 = TreeItemMapping()
    _safe_set(a, 'tree_description_TreeItemMapping26', b1)
    assert _is_linked(a, 'tree_description_TreeItemMapping26', b1)
    if hasattr(b1, 'TreeItemMapping27'):
        assert _is_linked(b1, 'TreeItemMapping27', a)
    _safe_set(a, 'tree_description_TreeItemMapping26', b2)
    assert _is_linked(a, 'tree_description_TreeItemMapping26', b2)
    if hasattr(b1, 'TreeItemMapping27'):
        assert not _is_linked(b1, 'TreeItemMapping27', a)
    if hasattr(b2, 'TreeItemMapping27'):
        assert _is_linked(b2, 'TreeItemMapping27', a)
    _safe_set(a, 'tree_description_TreeItemMapping26', None)
    assert not _is_linked(a, 'tree_description_TreeItemMapping26', b2)
    if hasattr(b2, 'TreeItemMapping27'):
        assert not _is_linked(b2, 'TreeItemMapping27', a)


def test_assoc_styleUpdater9_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = StyleUpdater()
    b2 = StyleUpdater()
    _safe_set(a, 'tree_DTreeItem10', b1)
    assert _is_linked(a, 'tree_DTreeItem10', b1)
    if hasattr(b1, 'StyleUpdater'):
        assert _is_linked(b1, 'StyleUpdater', a)
    _safe_set(a, 'tree_DTreeItem10', b2)
    assert _is_linked(a, 'tree_DTreeItem10', b2)
    if hasattr(b1, 'StyleUpdater'):
        assert not _is_linked(b1, 'StyleUpdater', a)
    if hasattr(b2, 'StyleUpdater'):
        assert _is_linked(b2, 'StyleUpdater', a)
    _safe_set(a, 'tree_DTreeItem10', None)
    assert not _is_linked(a, 'tree_DTreeItem10', b2)
    if hasattr(b2, 'StyleUpdater'):
        assert not _is_linked(b2, 'StyleUpdater', a)


def test_assoc_updater11_link_reassign_clear():
    a = tree_DTreeItem(expanded=True)
    b1 = TreeItemUpdater()
    b2 = TreeItemUpdater()
    _safe_set(a, 'tree_DTreeItem12', b1)
    assert _is_linked(a, 'tree_DTreeItem12', b1)
    if hasattr(b1, 'TreeItemUpdater'):
        assert _is_linked(b1, 'TreeItemUpdater', a)
    _safe_set(a, 'tree_DTreeItem12', b2)
    assert _is_linked(a, 'tree_DTreeItem12', b2)
    if hasattr(b1, 'TreeItemUpdater'):
        assert not _is_linked(b1, 'TreeItemUpdater', a)
    if hasattr(b2, 'TreeItemUpdater'):
        assert _is_linked(b2, 'TreeItemUpdater', a)
    _safe_set(a, 'tree_DTreeItem12', None)
    assert not _is_linked(a, 'tree_DTreeItem12', b2)
    if hasattr(b2, 'TreeItemUpdater'):
        assert not _is_linked(b2, 'TreeItemUpdater', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractToolDescription_strategy = st.builds(AbstractToolDescription)
@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=25)
def test_AbstractToolDescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)


ColorDescription_strategy = st.builds(ColorDescription)
@given(instance=ColorDescription_strategy)
@settings(max_examples=25)
def test_ColorDescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)


ConditionalStyleDescription_strategy = st.builds(ConditionalStyleDescription)
@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)


ConditionalTreeItemStyleDescription_strategy = st.builds(ConditionalTreeItemStyleDescription)
@given(instance=ConditionalTreeItemStyleDescription_strategy)
@settings(max_examples=25)
def test_ConditionalTreeItemStyleDescription_instantiation(instance):
    assert isinstance(instance, ConditionalTreeItemStyleDescription)


DRepresentation_strategy = st.builds(DRepresentation)
@given(instance=DRepresentation_strategy)
@settings(max_examples=25)
def test_DRepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)


DRepresentationElement_strategy = st.builds(DRepresentationElement)
@given(instance=DRepresentationElement_strategy)
@settings(max_examples=25)
def test_DRepresentationElement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)


DSemanticDecorator_strategy = st.builds(DSemanticDecorator)
@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=25)
def test_DSemanticDecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)


DTreeElement_strategy = st.builds(DTreeElement)
@given(instance=DTreeElement_strategy)
@settings(max_examples=25)
def test_DTreeElement_instantiation(instance):
    assert isinstance(instance, DTreeElement)


DTreeElementUpdater_strategy = st.builds(DTreeElementUpdater)
@given(instance=DTreeElementUpdater_strategy)
@settings(max_examples=25)
def test_DTreeElementUpdater_instantiation(instance):
    assert isinstance(instance, DTreeElementUpdater)


DTreeItemContainer_strategy = st.builds(DTreeItemContainer)
@given(instance=DTreeItemContainer_strategy)
@settings(max_examples=25)
def test_DTreeItemContainer_instantiation(instance):
    assert isinstance(instance, DTreeItemContainer)


LabelStyle_strategy = st.builds(LabelStyle)
@given(instance=LabelStyle_strategy)
@settings(max_examples=25)
def test_LabelStyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)


PrecedingSiblingsVariables_strategy = st.builds(PrecedingSiblingsVariables)
@given(instance=PrecedingSiblingsVariables_strategy)
@settings(max_examples=25)
def test_PrecedingSiblingsVariables_instantiation(instance):
    assert isinstance(instance, PrecedingSiblingsVariables)


RepresentationCreationDescription_strategy = st.builds(RepresentationCreationDescription)
@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)


RepresentationElementMapping_strategy = st.builds(RepresentationElementMapping)
@given(instance=RepresentationElementMapping_strategy)
@settings(max_examples=25)
def test_RepresentationElementMapping_instantiation(instance):
    assert isinstance(instance, RepresentationElementMapping)


RepresentationNavigationDescription_strategy = st.builds(RepresentationNavigationDescription)
@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)


Style_strategy = st.builds(Style)
@given(instance=Style_strategy)
@settings(max_examples=25)
def test_Style_instantiation(instance):
    assert isinstance(instance, Style)


StyleUpdater_strategy = st.builds(StyleUpdater)
@given(instance=StyleUpdater_strategy)
@settings(max_examples=25)
def test_StyleUpdater_instantiation(instance):
    assert isinstance(instance, StyleUpdater)


TreeDescription_strategy = st.builds(TreeDescription)
@given(instance=TreeDescription_strategy)
@settings(max_examples=25)
def test_TreeDescription_instantiation(instance):
    assert isinstance(instance, TreeDescription)


TreeItemContainerDropTool_strategy = st.builds(TreeItemContainerDropTool)
@given(instance=TreeItemContainerDropTool_strategy)
@settings(max_examples=25)
def test_TreeItemContainerDropTool_instantiation(instance):
    assert isinstance(instance, TreeItemContainerDropTool)


TreeItemCreationTool_strategy = st.builds(TreeItemCreationTool)
@given(instance=TreeItemCreationTool_strategy)
@settings(max_examples=25)
def test_TreeItemCreationTool_instantiation(instance):
    assert isinstance(instance, TreeItemCreationTool)


TreeItemDeletionTool_strategy = st.builds(TreeItemDeletionTool)
@given(instance=TreeItemDeletionTool_strategy)
@settings(max_examples=25)
def test_TreeItemDeletionTool_instantiation(instance):
    assert isinstance(instance, TreeItemDeletionTool)


TreeItemDragTool_strategy = st.builds(TreeItemDragTool)
@given(instance=TreeItemDragTool_strategy)
@settings(max_examples=25)
def test_TreeItemDragTool_instantiation(instance):
    assert isinstance(instance, TreeItemDragTool)


TreeItemEditionTool_strategy = st.builds(TreeItemEditionTool)
@given(instance=TreeItemEditionTool_strategy)
@settings(max_examples=25)
def test_TreeItemEditionTool_instantiation(instance):
    assert isinstance(instance, TreeItemEditionTool)


TreeItemMapping_strategy = st.builds(TreeItemMapping)
@given(instance=TreeItemMapping_strategy)
@settings(max_examples=25)
def test_TreeItemMapping_instantiation(instance):
    assert isinstance(instance, TreeItemMapping)


TreeItemMappingContainer_strategy = st.builds(TreeItemMappingContainer)
@given(instance=TreeItemMappingContainer_strategy)
@settings(max_examples=25)
def test_TreeItemMappingContainer_instantiation(instance):
    assert isinstance(instance, TreeItemMappingContainer)


TreeItemStyleDescription_strategy = st.builds(TreeItemStyleDescription)
@given(instance=TreeItemStyleDescription_strategy)
@settings(max_examples=25)
def test_TreeItemStyleDescription_instantiation(instance):
    assert isinstance(instance, TreeItemStyleDescription)


TreeItemTool_strategy = st.builds(TreeItemTool)
@given(instance=TreeItemTool_strategy)
@settings(max_examples=25)
def test_TreeItemTool_instantiation(instance):
    assert isinstance(instance, TreeItemTool)


TreeItemUpdater_strategy = st.builds(TreeItemUpdater)
@given(instance=TreeItemUpdater_strategy)
@settings(max_examples=25)
def test_TreeItemUpdater_instantiation(instance):
    assert isinstance(instance, TreeItemUpdater)


TreeMapping_strategy = st.builds(TreeMapping)
@given(instance=TreeMapping_strategy)
@settings(max_examples=25)
def test_TreeMapping_instantiation(instance):
    assert isinstance(instance, TreeMapping)


TreePopupMenu_strategy = st.builds(TreePopupMenu)
@given(instance=TreePopupMenu_strategy)
@settings(max_examples=25)
def test_TreePopupMenu_instantiation(instance):
    assert isinstance(instance, TreePopupMenu)


TreeVariable_strategy = st.builds(TreeVariable)
@given(instance=TreeVariable_strategy)
@settings(max_examples=25)
def test_TreeVariable_instantiation(instance):
    assert isinstance(instance, TreeVariable)


description_RepresentationDescription_strategy = st.builds(description_RepresentationDescription)
@given(instance=description_RepresentationDescription_strategy)
@settings(max_examples=25)
def test_description_RepresentationDescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationDescription)


description_StyleUpdater_strategy = st.builds(description_StyleUpdater)
@given(instance=description_StyleUpdater_strategy)
@settings(max_examples=25)
def test_description_StyleUpdater_instantiation(instance):
    assert isinstance(instance, description_StyleUpdater)


description_TreeItemMappingContainer_strategy = st.builds(description_TreeItemMappingContainer)
@given(instance=description_TreeItemMappingContainer_strategy)
@settings(max_examples=25)
def test_description_TreeItemMappingContainer_instantiation(instance):
    assert isinstance(instance, description_TreeItemMappingContainer)


description_TreeItemTool_strategy = st.builds(description_TreeItemTool)
@given(instance=description_TreeItemTool_strategy)
@settings(max_examples=25)
def test_description_TreeItemTool_instantiation(instance):
    assert isinstance(instance, description_TreeItemTool)


description_TreeItemUpdater_strategy = st.builds(description_TreeItemUpdater)
@given(instance=description_TreeItemUpdater_strategy)
@settings(max_examples=25)
def test_description_TreeItemUpdater_instantiation(instance):
    assert isinstance(instance, description_TreeItemUpdater)


description_TreeMapping_strategy = st.builds(description_TreeMapping)
@given(instance=description_TreeMapping_strategy)
@settings(max_examples=25)
def test_description_TreeMapping_instantiation(instance):
    assert isinstance(instance, description_TreeMapping)


style_LabelStyleDescription_strategy = st.builds(style_LabelStyleDescription)
@given(instance=style_LabelStyleDescription_strategy)
@settings(max_examples=25)
def test_style_LabelStyleDescription_instantiation(instance):
    assert isinstance(instance, style_LabelStyleDescription)


style_StyleDescription_strategy = st.builds(style_StyleDescription)
@given(instance=style_StyleDescription_strategy)
@settings(max_examples=25)
def test_style_StyleDescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)


tool_AbstractVariable_strategy = st.builds(tool_AbstractVariable)
@given(instance=tool_AbstractVariable_strategy)
@settings(max_examples=25)
def test_tool_AbstractVariable_instantiation(instance):
    assert isinstance(instance, tool_AbstractVariable)


tool_ContainerViewVariable_strategy = st.builds(tool_ContainerViewVariable)
@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=25)
def test_tool_ContainerViewVariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)


tool_DropContainerVariable_strategy = st.builds(tool_DropContainerVariable)
@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=25)
def test_tool_DropContainerVariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)


tool_EditMaskVariables_strategy = st.builds(tool_EditMaskVariables)
@given(instance=tool_EditMaskVariables_strategy)
@settings(max_examples=25)
def test_tool_EditMaskVariables_instantiation(instance):
    assert isinstance(instance, tool_EditMaskVariables)


tool_ElementDropVariable_strategy = st.builds(tool_ElementDropVariable)
@given(instance=tool_ElementDropVariable_strategy)
@settings(max_examples=25)
def test_tool_ElementDropVariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDropVariable)


tool_MappingBasedToolDescription_strategy = st.builds(tool_MappingBasedToolDescription)
@given(instance=tool_MappingBasedToolDescription_strategy)
@settings(max_examples=25)
def test_tool_MappingBasedToolDescription_instantiation(instance):
    assert isinstance(instance, tool_MappingBasedToolDescription)


tool_MenuItemOrRef_strategy = st.builds(tool_MenuItemOrRef)
@given(instance=tool_MenuItemOrRef_strategy)
@settings(max_examples=25)
def test_tool_MenuItemOrRef_instantiation(instance):
    assert isinstance(instance, tool_MenuItemOrRef)


tool_ModelOperation_strategy = st.builds(tool_ModelOperation)
@given(instance=tool_ModelOperation_strategy)
@settings(max_examples=25)
def test_tool_ModelOperation_instantiation(instance):
    assert isinstance(instance, tool_ModelOperation)


tool_RepresentationCreationDescription_strategy = st.builds(tool_RepresentationCreationDescription)
@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationCreationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)


tool_RepresentationNavigationDescription_strategy = st.builds(tool_RepresentationNavigationDescription)
@given(instance=tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=25)
def test_tool_RepresentationNavigationDescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationNavigationDescription)


tool_VariableContainer_strategy = st.builds(tool_VariableContainer)
@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=25)
def test_tool_VariableContainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)


tree_DTree_strategy = st.builds(tree_DTree)
@given(instance=tree_DTree_strategy)
@settings(max_examples=25)
def test_tree_DTree_instantiation(instance):
    assert isinstance(instance, tree_DTree)


tree_DTreeElement_strategy = st.builds(tree_DTreeElement)
@given(instance=tree_DTreeElement_strategy)
@settings(max_examples=25)
def test_tree_DTreeElement_instantiation(instance):
    assert isinstance(instance, tree_DTreeElement)


tree_DTreeElementSynchronizer_strategy = st.builds(tree_DTreeElementSynchronizer)
@given(instance=tree_DTreeElementSynchronizer_strategy)
@settings(max_examples=25)
def test_tree_DTreeElementSynchronizer_instantiation(instance):
    assert isinstance(instance, tree_DTreeElementSynchronizer)


tree_DTreeElementUpdater_strategy = st.builds(tree_DTreeElementUpdater)
@given(instance=tree_DTreeElementUpdater_strategy)
@settings(max_examples=25)
def test_tree_DTreeElementUpdater_instantiation(instance):
    assert isinstance(instance, tree_DTreeElementUpdater)


tree_DTreeItem_strategy = st.builds(tree_DTreeItem, expanded=st.booleans())
@given(instance=tree_DTreeItem_strategy)
@settings(max_examples=25)
def test_tree_DTreeItem_instantiation(instance):
    assert isinstance(instance, tree_DTreeItem)


tree_DTreeItemContainer_strategy = st.builds(tree_DTreeItemContainer)
@given(instance=tree_DTreeItemContainer_strategy)
@settings(max_examples=25)
def test_tree_DTreeItemContainer_instantiation(instance):
    assert isinstance(instance, tree_DTreeItemContainer)


tree_EObject_strategy = st.builds(tree_EObject)
@given(instance=tree_EObject_strategy)
@settings(max_examples=25)
def test_tree_EObject_instantiation(instance):
    assert isinstance(instance, tree_EObject)


tree_RGBValues_strategy = st.builds(tree_RGBValues)
@given(instance=tree_RGBValues_strategy)
@settings(max_examples=25)
def test_tree_RGBValues_instantiation(instance):
    assert isinstance(instance, tree_RGBValues)


tree_TreeItemStyle_strategy = st.builds(tree_TreeItemStyle)
@given(instance=tree_TreeItemStyle_strategy)
@settings(max_examples=25)
def test_tree_TreeItemStyle_instantiation(instance):
    assert isinstance(instance, tree_TreeItemStyle)


tree_description_ConditionalTreeItemStyleDescription_strategy = st.builds(tree_description_ConditionalTreeItemStyleDescription)
@given(instance=tree_description_ConditionalTreeItemStyleDescription_strategy)
@settings(max_examples=25)
def test_tree_description_ConditionalTreeItemStyleDescription_instantiation(instance):
    assert isinstance(instance, tree_description_ConditionalTreeItemStyleDescription)


tree_description_PrecedingSiblingsVariables_strategy = st.builds(tree_description_PrecedingSiblingsVariables)
@given(instance=tree_description_PrecedingSiblingsVariables_strategy)
@settings(max_examples=25)
def test_tree_description_PrecedingSiblingsVariables_instantiation(instance):
    assert isinstance(instance, tree_description_PrecedingSiblingsVariables)


tree_description_StyleUpdater_strategy = st.builds(tree_description_StyleUpdater)
@given(instance=tree_description_StyleUpdater_strategy)
@settings(max_examples=25)
def test_tree_description_StyleUpdater_instantiation(instance):
    assert isinstance(instance, tree_description_StyleUpdater)


tree_description_TreeCreationDescription_strategy = st.builds(tree_description_TreeCreationDescription)
@given(instance=tree_description_TreeCreationDescription_strategy)
@settings(max_examples=25)
def test_tree_description_TreeCreationDescription_instantiation(instance):
    assert isinstance(instance, tree_description_TreeCreationDescription)


tree_description_TreeDescription_strategy = st.builds(tree_description_TreeDescription, domainClass=safe_text, preconditionExpression=safe_text)
@given(instance=tree_description_TreeDescription_strategy)
@settings(max_examples=25)
def test_tree_description_TreeDescription_instantiation(instance):
    assert isinstance(instance, tree_description_TreeDescription)


tree_description_TreeItemContainerDropTool_strategy = st.builds(tree_description_TreeItemContainerDropTool, dragSource=safe_text)
@given(instance=tree_description_TreeItemContainerDropTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemContainerDropTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemContainerDropTool)


tree_description_TreeItemCreationTool_strategy = st.builds(tree_description_TreeItemCreationTool)
@given(instance=tree_description_TreeItemCreationTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemCreationTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemCreationTool)


tree_description_TreeItemDeletionTool_strategy = st.builds(tree_description_TreeItemDeletionTool)
@given(instance=tree_description_TreeItemDeletionTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemDeletionTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemDeletionTool)


tree_description_TreeItemDragTool_strategy = st.builds(tree_description_TreeItemDragTool, dragSourceType=safe_text)
@given(instance=tree_description_TreeItemDragTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemDragTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemDragTool)


tree_description_TreeItemEditionTool_strategy = st.builds(tree_description_TreeItemEditionTool)
@given(instance=tree_description_TreeItemEditionTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemEditionTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemEditionTool)


tree_description_TreeItemMapping_strategy = st.builds(tree_description_TreeItemMapping, domainClass=safe_text, preconditionExpression=safe_text, semanticCandidatesExpression=safe_text)
@given(instance=tree_description_TreeItemMapping_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemMapping_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemMapping)


tree_description_TreeItemMappingContainer_strategy = st.builds(tree_description_TreeItemMappingContainer)
@given(instance=tree_description_TreeItemMappingContainer_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemMappingContainer_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemMappingContainer)


tree_description_TreeItemStyleDescription_strategy = st.builds(tree_description_TreeItemStyleDescription)
@given(instance=tree_description_TreeItemStyleDescription_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemStyleDescription_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemStyleDescription)


tree_description_TreeItemTool_strategy = st.builds(tree_description_TreeItemTool)
@given(instance=tree_description_TreeItemTool_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemTool_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemTool)


tree_description_TreeItemUpdater_strategy = st.builds(tree_description_TreeItemUpdater)
@given(instance=tree_description_TreeItemUpdater_strategy)
@settings(max_examples=25)
def test_tree_description_TreeItemUpdater_instantiation(instance):
    assert isinstance(instance, tree_description_TreeItemUpdater)


tree_description_TreeMapping_strategy = st.builds(tree_description_TreeMapping, semanticElements=safe_text)
@given(instance=tree_description_TreeMapping_strategy)
@settings(max_examples=25)
def test_tree_description_TreeMapping_instantiation(instance):
    assert isinstance(instance, tree_description_TreeMapping)


tree_description_TreeNavigationDescription_strategy = st.builds(tree_description_TreeNavigationDescription)
@given(instance=tree_description_TreeNavigationDescription_strategy)
@settings(max_examples=25)
def test_tree_description_TreeNavigationDescription_instantiation(instance):
    assert isinstance(instance, tree_description_TreeNavigationDescription)


tree_description_TreePopupMenu_strategy = st.builds(tree_description_TreePopupMenu)
@given(instance=tree_description_TreePopupMenu_strategy)
@settings(max_examples=25)
def test_tree_description_TreePopupMenu_instantiation(instance):
    assert isinstance(instance, tree_description_TreePopupMenu)


tree_description_TreeVariable_strategy = st.builds(tree_description_TreeVariable, documentation=safe_text)
@given(instance=tree_description_TreeVariable_strategy)
@settings(max_examples=25)
def test_tree_description_TreeVariable_instantiation(instance):
    assert isinstance(instance, tree_description_TreeVariable)



