from python_code import tree_DTreeElementSynchronizer

def test_tree_DTreeElementSynchronizer___init__():
    assert tree_DTreeElementSynchronizer.__init__(tree_DTreeElementSynchronizer()) == None

def test_tree_DTreeElementSynchronizer_refresh():
    assert tree_DTreeElementSynchronizer.refresh(tree_DTreeElementSynchronizer(), '') == None


from python_code import tree_description_TreeDescription

def test_tree_description_TreeDescription___init__():
    assert tree_description_TreeDescription.__init__(tree_description_TreeDescription('', '', tree_description_TreeDescription=set(), tree_description_TreeDescription15=set(), tree_description_TreeDescription17=set()), '', '', tree_description_TreeDescription=set(), tree_description_TreeDescription15=set(), tree_description_TreeDescription17=set()) == None


from python_code import PrecedingSiblingsVariables
from python_code import tool_ContainerViewVariable
from python_code import tool_DropContainerVariable
from python_code import tool_ElementDropVariable
from python_code import tree_description_TreeItemContainerDropTool

def test_tree_description_TreeItemContainerDropTool___init__():
    assert tree_description_TreeItemContainerDropTool.__init__(tree_description_TreeItemContainerDropTool('', tree_description_TreeItemContainerDropTool=tool_DropContainerVariable(), tree_description_TreeItemContainerDropTool54=tool_DropContainerVariable(), tree_description_TreeItemContainerDropTool57=tool_ElementDropVariable(), tree_description_TreeItemContainerDropTool60=tool_ContainerViewVariable(), tree_description_TreeItemContainerDropTool63=PrecedingSiblingsVariables()), '', tree_description_TreeItemContainerDropTool=tool_DropContainerVariable(), tree_description_TreeItemContainerDropTool54=tool_DropContainerVariable(), tree_description_TreeItemContainerDropTool57=tool_ElementDropVariable(), tree_description_TreeItemContainerDropTool60=tool_ContainerViewVariable(), tree_description_TreeItemContainerDropTool63=PrecedingSiblingsVariables()) == None


from python_code import PrecedingSiblingsVariables
from python_code import tool_ContainerViewVariable
from python_code import tool_DropContainerVariable
from python_code import tool_ElementDropVariable
from python_code import tree_description_TreeItemDragTool

def test_tree_description_TreeItemDragTool___init__():
    assert tree_description_TreeItemDragTool.__init__(tree_description_TreeItemDragTool('', tree_description_TreeItemDragTool=tool_DropContainerVariable(), tree_description_TreeItemDragTool41=tool_DropContainerVariable(), tree_description_TreeItemDragTool44=tool_ElementDropVariable(), tree_description_TreeItemDragTool46=tool_ContainerViewVariable(), tree_description_TreeItemDragTool48=set(), tree_description_TreeItemDragTool50=PrecedingSiblingsVariables()), '', tree_description_TreeItemDragTool=tool_DropContainerVariable(), tree_description_TreeItemDragTool41=tool_DropContainerVariable(), tree_description_TreeItemDragTool44=tool_ElementDropVariable(), tree_description_TreeItemDragTool46=tool_ContainerViewVariable(), tree_description_TreeItemDragTool48=set(), tree_description_TreeItemDragTool50=PrecedingSiblingsVariables()) == None

def test_tree_description_TreeItemDragTool_getBestTreeItemMapping():
    assert tree_description_TreeItemDragTool.getBestTreeItemMapping(tree_description_TreeItemDragTool('', tree_description_TreeItemDragTool=tool_DropContainerVariable(), tree_description_TreeItemDragTool41=tool_DropContainerVariable(), tree_description_TreeItemDragTool44=tool_ElementDropVariable(), tree_description_TreeItemDragTool46=tool_ContainerViewVariable(), tree_description_TreeItemDragTool48=set(), tree_description_TreeItemDragTool50=PrecedingSiblingsVariables())) == None


from python_code import TreeItemDeletionTool
from python_code import TreeItemMapping
from python_code import tree_description_TreeItemMapping

def test_tree_description_TreeItemMapping___init__():
    assert tree_description_TreeItemMapping.__init__(tree_description_TreeItemMapping('', '', '', tree_description_TreeItemMapping=set(), tree_description_TreeItemMapping21=set(), tree_description_TreeItemMapping24=TreeItemMapping(), mapping=TreeItemDeletionTool(), tree_description_TreeItemMapping28=set(), tree_description_TreeItemMapping31=set(), tree_description_TreeItemMapping33=set()), '', '', '', tree_description_TreeItemMapping=set(), tree_description_TreeItemMapping21=set(), tree_description_TreeItemMapping24=TreeItemMapping(), mapping=TreeItemDeletionTool(), tree_description_TreeItemMapping28=set(), tree_description_TreeItemMapping31=set(), tree_description_TreeItemMapping33=set()) == None


from python_code import TreeItemEditionTool
from python_code import tree_description_TreeItemUpdater

def test_tree_description_TreeItemUpdater___init__():
    assert tree_description_TreeItemUpdater.__init__(tree_description_TreeItemUpdater(tree_description_TreeItemUpdater=TreeItemEditionTool()), tree_description_TreeItemUpdater=TreeItemEditionTool()) == None

def test_tree_description_TreeItemUpdater_getCreateTreeItem():
    assert tree_description_TreeItemUpdater.getCreateTreeItem(tree_description_TreeItemUpdater(tree_description_TreeItemUpdater=TreeItemEditionTool())) == None

def test_tree_description_TreeItemUpdater_getLabelComputationExpression():
    assert tree_description_TreeItemUpdater.getLabelComputationExpression(tree_description_TreeItemUpdater(tree_description_TreeItemUpdater=TreeItemEditionTool())) == None


from python_code import tree_description_TreeMapping

def test_tree_description_TreeMapping___init__():
    assert tree_description_TreeMapping.__init__(tree_description_TreeMapping(''), '') == None


from python_code import tree_description_TreeVariable

def test_tree_description_TreeVariable___init__():
    assert tree_description_TreeVariable.__init__(tree_description_TreeVariable(''), '') == None

