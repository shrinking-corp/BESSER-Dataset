from python_code import remes_ControlPath
from python_code import remes_EntryPoint
from python_code import remes_ExitPoint

def test_remes_ControlPath___init__():
    assert remes_ControlPath.__init__(remes_ControlPath('', ControlPath=remes_EntryPoint(), ControlPath32=remes_ExitPoint(), container=remes_EntryPoint(), container3=remes_ExitPoint()), '', ControlPath=remes_EntryPoint(), ControlPath32=remes_ExitPoint(), container=remes_EntryPoint(), container3=remes_ExitPoint()) == None


from python_code import ActionRoot
from python_code import LogicalRoot
from python_code import remes_Edge
from python_code import remes_EntryPoint
from python_code import remes_ExitPoint

def test_remes_Edge___init__():
    assert remes_Edge.__init__(remes_Edge('', '\x00', Edge=remes_EntryPoint(), remes_Edge=LogicalRoot(), exitEdges=remes_ExitPoint(), entryEdges=remes_EntryPoint(), remes_Edge44=ActionRoot(), Edge30=remes_ExitPoint()), '\x00\x00', '', Edge=remes_EntryPoint(), remes_Edge=LogicalRoot(), exitEdges=remes_ExitPoint(), entryEdges=remes_EntryPoint(), remes_Edge44=ActionRoot(), Edge30=remes_ExitPoint()) == None


from python_code import ActionRoot
from python_code import remes_EntryPoint
from python_code import remes_InitEdge
from python_code import remes_InitPoint

def test_remes_InitEdge___init__():
    assert remes_InitEdge.__init__(remes_InitEdge('', InitEdge=remes_InitPoint(), initEdge=remes_InitPoint(), remes_InitEdge=remes_EntryPoint(), remes_InitEdge49=ActionRoot()), '', InitEdge=remes_InitPoint(), initEdge=remes_InitPoint(), remes_InitEdge=remes_EntryPoint(), remes_InitEdge49=ActionRoot()) == None


from python_code import remes_Referable

def test_remes_Referable___init__():
    assert remes_Referable.__init__(remes_Referable(''), '') == None


from python_code import LogicalRoot
from python_code import remes_CompositeMode
from python_code import remes_SubMode

def test_remes_SubMode___init__():
    assert remes_SubMode.__init__(remes_SubMode('', False, SubMode=remes_CompositeMode(), subModes=remes_CompositeMode(), remes_SubMode=LogicalRoot()), '', False, SubMode=remes_CompositeMode(), subModes=remes_CompositeMode(), remes_SubMode=LogicalRoot()) == None

